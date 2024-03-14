import joblib
import numpy as np
import json
import gcsfs

# Ruta del modelo en GCS
# model_path = "gs://modelos_taxis_ny/prediccion_congestion.joblib"

# Función para cargar el modelo desde GCS
def load_model_from_gcs(model_path):
    fs = gcsfs.GCSFileSystem()
    with fs.open(model_path, 'rb') as f:
        model = joblib.load(f)
    return model

# Función de la nube
def predict(request):
    request_json = request.get_json()
    if request_json and 'selected_modelo' in request_json:
        selected_modelo = request_json['selected_modelo']
        modelo_params = request_json['modelo_params']
        # Cargar el modelo desde GCS
        if selected_modelo == 'Predicción de cargo por tráfico':
            nombre_modelo = 'prediccion_congestion.joblib'
            salida_modelo = 'El cargo por tráfico para el viaje solicitado es de, aproximadamente, USD'
        else:
            nombre_modelo = 'prediccion_precio.joblib'
            salida_modelo = 'La tarifa para el viaje solicitado es de, aproximadamente, USD'
        model_path = f"gs://modelos_taxis_ny/{nombre_modelo}"
        model = load_model_from_gcs(model_path)
        # Realizar la predicción
        prediction = model.predict(np.array(list(modelo_params.values())).reshape(1, -1))
        return json.dumps({"prediction": prediction.tolist()})
    else:
        return 'Error: No se especificó el modelo o los parámetros.', 400

