import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def my_function():
    return 'PROYECTO INDIVIDUAL Nº1 Machine Learning Operations (MLOps)'

@app.get('/')
def determinar_efectivo_():
    df = pd.read_parquet("C:\Users\Acer\Downloads\green_tripdata_2023-12.parquet", engine='fastparquet')
    tar_credito = round((df[df['modalidad_pago'] == 1].count()/(df.shape[0])*100).reset_index(), 2)
    tar_credito.iloc[17, :].values[1]