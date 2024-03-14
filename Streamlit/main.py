import streamlit as st
import requests

# URL de tu función en la nube
cloud_function_url = "https://us-central1-silicon-carver-416314.cloudfunctions.net/Prueba"

# Definir los parámetros específicos para cada modelo
modelo_params = {
    "Predicción de cargo por tráfico": ["Zona de inicio (1 a 265)", "Zona de finalización (1 a 265)", "Distancia estimada (millas)", "Tiempo estimado (minutos)"],
    "Predicción de tarifa": ["Tiempo estimado (minutos)", "Distancia estimada (millas)"]}

# Definir una función para realizar la solicitud HTTPS
def invoke_cloud_function(params, selected_modelo):
    try:
        data = {
            "selected_modelo": selected_modelo,
            "modelo_params": params
        }
        response = requests.post(cloud_function_url, json=data)
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            prediction_str = str(prediction)
            prediction_str = prediction_str.replace('[', '').replace(']','')
            prediccion = round(float(prediction_str),2)
            if data["selected_modelo"] == "Predicción de cargo por tráfico":
                st.write(f'El recargo por tráfico aproximado para este viaje será de USD {prediccion}.')
            else:
                st.write(f'La tarifa aproximada para este viaje será de U$D {prediccion}')
        else:
            st.write("Error al activar la función:", response.status_code)
    except Exception as e:
        st.write("Error:", e)

# Interfaz de usuario en Streamlit
def main():
    st.title("Sistema de predicción")
    st.write("Selecciona un modelo con los parámetros correspondientes para la predicción:")
    
    modelos = list(modelo_params.keys())
    selected_modelo = st.selectbox("Selecciona el modelo", modelos)
    
    params = {}
    for param_name in modelo_params[selected_modelo]:
        params[param_name] = st.text_input(f"{param_name}", "")
    
    if st.button("Predicción"):
        invoke_cloud_function(params, selected_modelo)

if __name__ == "__main__":
    main()
