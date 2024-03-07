from google.cloud import storage
import pandas as pd
import pyarrow
import tempfile
import warnings
warnings.filterwarnings("ignore")

"""
def verificar_archivo_existente(bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    return (bucket, blob, blob.exists())
"""

def verificar_archivo_existente_2(bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    for blob in bucket.list_blobs():
        if blob.name.endswith(file_name):
            return True
    return False

def etl_taxis(event, context):
    # Crea una instancia del cliente de Cloud Storage
    client = storage.Client()
    bucket_name = event['bucket']
    archivo_nombre = event['name']
    # print('Antes del print')
    # print(f'Existe: {verificar_archivo_existente_2('dataets-limpios-taxis', archivo_nombre)}')

    if verificar_archivo_existente_2('dataets-limpios-taxis', archivo_nombre):
        print(f'El archivo {archivo_nombre} ya existe en el bucket {bucket_name}. No se realizará el procesamiento.')
        return
        

    # Obtiene una instancia del bucket
    bucket = client.get_bucket(bucket_name)

    # Obtiene una referencia al objeto Blob
    blob = bucket.blob(archivo_nombre)

    # Crea un archivo temporal local para descargar el archivo Parquet
    local_tempfile = tempfile.NamedTemporaryFile(delete=False)
    blob.download_to_filename(local_tempfile.name)

    # Lee el archivo Parquet desde el archivo local
    df = pd.read_parquet(local_tempfile.name, engine='pyarrow')
    
    nuevos_nombres = {'tpep_pickup_datetime': 'inicio_viaje', 'tpep_dropoff_datetime': 'fin_viaje', 'passenger_count': 'pasajeros',
                  'trip_distance': 'distancia', 'PULocationID': 'zona_inicio', 'DOLocationID': 'zona_fin', 'fare_amount': 'tarifa_medida',
                  'total_amount': 'tarifa_total', 'congestion_surcharge': 'recargo_trafico', 'payment_type': 'modalidad_pago',
                  'tip_amount': 'propina', 'lpep_pickup_datetime': 'inicio_viaje', 'lpep_dropoff_datetime': 'fin_viaje'}

    df.rename(columns=nuevos_nombres, inplace=True)

    columnas_a_borrar = []
    
    for columna in df.columns:
        if columna not in nuevos_nombres.values():
            columnas_a_borrar.append(columna)
    
    df = df.drop(columnas_a_borrar, axis=1)
    
    def positivos(valor:float|int) -> float|int:
        if type(valor) == float:
            return float(abs(valor))
        else:
            return int(abs(valor))
    
    for columna in df.columns[2:]:
        df[columna] = df[columna].apply(positivos)
    

    def revision_nulos(data:pd.DataFrame) -> dict:
        porcentaje_nulos_dict = {}
        for columna in data.columns:
            nulos = data[columna].isnull().sum()
            total = len(data[columna])
            porcentaje = round(nulos/total*100,2)
            porcentaje_nulos_dict[columna] = porcentaje
            # print(f'\nColumna: {columna:<20}      Cantidad de nulos: {nulos:<7}      Porcentaje de nulos: {str(porcentaje) + " %":<8}\n')
        return porcentaje_nulos_dict

    nulos_dict = revision_nulos(df)
    
    def reemplazar_nan_float(valor:float) -> float:
        if pd.isnull(valor):
            return float(-1)
        else:
            return float(valor)

    def reemplazar_nan_int(valor:float) -> int:
        if pd.isnull(valor):
            return int(-1)
        else:
            return int(valor)

    def mediana_columna_float(data:pd.Series) -> float:
        return float(round(data.median(), 2))

    def mediana_columna_int(data:pd.Series) -> int:
        return int(data.median())

    def reemplazar_nan_mediana_int(columna:str, data:pd.DataFrame) -> None:
        mediana = mediana_columna_int(data[columna][~data[columna].isnull()])
        def mediana_f(valor:float) -> int:
            if pd.isnull(valor):
                return int(mediana)
            else:
                return int(valor)
        data[columna] = data[columna].apply(mediana_f)

    def reemplazar_nan_mediana_float(columna:str, data:pd.DataFrame) -> None:
        mediana = mediana_columna_float(data[columna][~data[columna].isnull()])
        def mediana_f(valor:float) -> float:
            if pd.isnull(valor):
                return float(mediana)
            else:
                return float(valor)
        data[columna] = data[columna].apply(mediana_f)



    for columna in df.columns[2:]:
        if df[columna].isnull().sum() == 0:
            continue
        else:
            if columna == 'zona_inicio' or columna == 'zona_fin':
                df[columna] = df[columna].apply(reemplazar_nan_int)
            elif columna == 'pasajeros':
                if nulos_dict[columna] >= 10:
                    df[columna] = df[columna].apply(reemplazar_nan_int)
                else:
                    reemplazar_nan_mediana_int(columna, df)
            else:
                if nulos_dict[columna] >= 10:
                    df[columna] = df[columna].apply(reemplazar_nan_float)
                else:
                    reemplazar_nan_mediana_float(columna, df)
    
    def revision_duplicados(data:pd.DataFrame) -> None:
        duplicados = data.duplicated().sum()
        total = len(data)
        porcentaje = round(duplicados/total*100,2)
        # print(f'\nCantidad de duplicados: {duplicados:<7}      Porcentaje de duplicados: {str(porcentaje) + " %":<8}\n')
        if duplicados > 0:
            data = data.drop_duplicates()
            # print(f'Se eliminaron {duplicados} registros duplicados.')
    
    revision_duplicados(df)

    def limite_pasajeros(cantidad:int) -> int:
        if cantidad > 4:
            return int(-1)
        else:
            return int(cantidad)

    df['pasajeros'] = df['pasajeros'].apply(limite_pasajeros)

    df = df.drop(df['distancia'][df['distancia'] > 20].index)
    df = df.drop(df[(df['tarifa_medida']>0) & (df['distancia']==0)].index)
    df = df.drop(df[(df['tarifa_medida']>300) & (df['distancia']<20)].index)
    df = df.drop(df[(df['tarifa_medida']>100) & (df['distancia']<5)].index)
    df['modalidad_pago'][df['modalidad_pago'] == 2] = -1




    ruta = 'gs://dataets-limpios-taxis/'

    df.to_parquet(ruta + 'limpio_' + archivo_nombre, engine='pyarrow')


    


    # Limpia el archivo temporal local después de usarlo
    local_tempfile.close()


    