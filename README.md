# <h1 align="center">**`NYC Taxis`** <br> Estudio de viabilidad para la implementacion de una flota de taxis ELectricos en New York</h1>

<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/carro.jpeg"  >
</p>

## **Contexto**

El presente proyecto busca simular una consultora de análisis de datos la cual tiene como objetivo dar acompañamiento en la toma de decisiones de negocio a una empresa de servicios de transporte de pasajeros en New York, que actualmente se encuentra operando en el sector de micros de media y larga distancia y está interesada en invertir en el sector de transporte de pasajeros con automóviles. 

Con una visión de un futuro menos contaminado, ajustarse a las tendencias actuales y tener buena rentabilidad, se busca decidir que tipo de vehiculo seria el ideal: 100% electrico, Hibrido enchufable, otras alternativas ecologicas, o convencional. Para tomar decisiones bien fundamentadas los datos son extraídos de las recolecciones hechas por NYC Taxi and Limousine Commission y otros organismos de NYC, au pagina web es
[Comision de taxis y limusinas de NY](https://www.nyc.gov/site/tlc/index.page)

El proyecto se divide en tres Sprint, de una semana cada uno, se implemento la metodologia agil de Scrum, se lleva a cabao cada viener una reunion con el Product Owner para dar los avances, el equipo de trabajo esta conformado por 5 integrantes:

<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/integrantes.png" width=400 height=250 >
</p>

Los entregables del primer Sprint con el responsable y fechas se pueden visualizar en el siguiente diagrama Gantt
<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/gant1.png" width=400 height=250 >
</p>

## **Sprint 1**

* El primer paso es hacer un Estudio a profundidad de la situacion actual, evaluar hipotesis tales como: los 
  carros electricos deberian ser la primera opcion a tomar en cuenta, los vehiculos verdes son mas eficientes en 
  rendimiento.
  
* Se define el objetivo general como:
  Estudiar grandes volumenes de datos para evaliuar la viabilidad de implementar una flota de vehiculos con   
  consumo de energia alternativaObjetivos y alcance general del proyecto
  
* Entrando ya con la ejecucion del proyecto, se realiza un EDA preliminar, donde evalua por ejemplo la 
  disponibilidad de cargadores electricos en la ciudad, para ver si hay suficiente disponibilidad, en el siguiente   mapa se observa la distribucion.

<h1 align = "center">Mapa de New York, distribucion de estaciones de carga electrica</h1>
<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/mapa.png" width=300 height=200 alt = "Mapa de New York" >
</p>

*`Cómo se observa en el mapa, hay disponibilidad uniforme de estaciones de carga eléctrica para vehículos`.*

Se realizó una matriz de correlacion referente al rendimiento de los vehiculos hibridos enchufables.

<h1 align = "center">Matriz de correlacion rendimiento vehiculos hibridos enchufables</h1>
<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/matriz_rendimiento_hibridos.png" width=500 height=350>
</p>

*`No hay correlacion significativa entre las variables`.*

En el siguiente enlace se puede ver el EDA de todos los datasets [EDA](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/tree/main/4.%20EDA-ETL)

* Se definen tres KPI's
  1. Millas promedio por galón de combustible
     Presmisa: Aumentar en un 5% las millas recorridas por galón con respecto al semestre anterior.

  2. Tiempo de carga promedio.
     Premisa: Disminuir en un 3% el tiempo de carga de todos los vehiculos.

  3. Satisfaccion del cliente
     Premisa: Aumentar un 5% la cantidad de reseñas positivas por semestre

* A continuacion, se define el Stack Tecnológico
<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/Stack_tecnologico.png" width=300 height=200>
</p>


- Diccionario del proyecto [Data Dictionary](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Data%20Dictionary.pdf)


## **Sprint 2**
Para la segunda semana se monta la infraestructura del proyecto, con pipelines para realizar el proceso de ETL automatizado, la impementacion se hace a traves de ![Google Cloud](https://img.shields.io/badge/-Google%20Cloud-333333?style=flat&logo=google-cloud)

El Workflow es el siguiente:

`Cloud Storage`

En este data lake  se van almacenar los datasets en bruto, para ello se crea un bucket que es un contenedor de almacenamiento, en el siguiente link se visualiza [Bucket](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/bucket.png)

`Cloud Functions`

En estas funciones estan los Scripts que realizan el ETL a cada Dataset, se puede ver un ejemplo en el siguiente link [Cloud function ETL](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/5.%20Cloud%20functions/ETL.py)
Cada vez que se carga un archivo en el storaged de dispara un activador que va a llamar a la cloud function y se automatiza el proceso de ETL, una vez esta hecho el ETL se crea otra cloud function para enviar automaticamente el dataset limpio a bigquerry, esa funcion se puede visualizar aqui [Cloud function Big Querry](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/5.%20Cloud%20functions/big_querry.py)

`Big Query`
En esta herramienta de big data donde se van a almacenar todos los datos para posteriormemte hacer consultas, la estructura se puede ver aqui
[Big Query](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/big_querry.png)

## **Sprint 3**
Para la tercera semana como entregables principales se tiene el dashboard interactivo y el modelo de Machine Learning: el primero fue elaborado con la herramienta ![Power BI](https://img.shields.io/badge/-Power%20BI-333333?style=flat&logo=powerbi&logoColor=white), los modelos de Machine learnig fueron elaborados con Arboles de desicion y redes neuronales.

`Dashboard`
El dashboard de una manera interactiva muestra mediante sus graficos informacion relevante de los precios de  vehiculos, rendimiento segun su tipo: ya sean hibridos enchifables, 100% electricos o convencionales, algunas hallazgos son:
1. Gasto en dolares de cada tipo de vehiculo para una autonomia de 450 km:
  * hibrido: 56.45
  * carro 100& electrico 67.5
   *carro convencional : 60.75
2. Hay suficientes estaciones de carga distribuidos a lo largo de la ciudad de New York.
3. EL vehiculo que mas se adecua a las necesidades de la empresa es el Toyota prius Prime.
4. La autonomia combinada de dicho carro es 589 millas y su precio es 28775 dolares.

<h1 align = "center">Toyota prius Prime</h1>
<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/toyota-prius-prime-hibrido-enchufable-201626742_3.webp" width=300 height=200 alt = "Mapa de New York" >
</p>


`Modelo de Machine Learning`
* Tráfico
En el proyecto se busca predecir el cargo por trafico que puede tener un servicio de taxi tomando en cuenta los siguientes parametros: punto de partida, de llegada, tiempo de viaje (min) y distancia recorrida (millas), el moselo seleccionado es un árbol de decision, ya que permite predecir una variable numerica discreta, como lo es el tipo de cargo que tiene un servicio dependiendo del trafico:

  1. Sin trafico = 0
  2. Con trafico = 2
  
para visualizar la creacion del modelo se púede ver en el siguiente link [ML predicion de cargo por trafico](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Modelos%20ML/modelo_cargo_congestion.ipynb)


* Precio del servicio
Se busca predecir el costo de un servicio sin cargos en dolares, para ello se decidio implementar un modelo de árbol de regresion el cual permite predecir variables que son continuas, los parametyros de entrenamiento son: distancia recorrida (millas) y tiempo de viaje (min).-
para visualizar la creacion del modelo se púede ver en el siguiente link [ML predicion de precio de servicio](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Modelos%20ML/modelo_predecir_precio.ipynb)

`Deploy`


Una vez entrenados los modelos de ML, se subieron a un bucket de GCP y se creó una Cloud Function que abre un modelo entrenado y realiza la predicción en base a una solicitud HTTP. La solicitud se está ejecutando desde la plataforma Stremlit; se selecciona el modelo de predicción desde un menú desplegable y se le pasan los parámetros correspondientes.

Internamente, la Cloud Function recibe el nombre del modelo y los parámetros en formato json, abre el modelo seleccionado y devuelve la predicción hacia Streamlit. En el script de la app se reciben los datos, también en formato json, y se muestran al usuario como una cadena de texto. El script de Streamlit contiene un diccionario en el que se especfican tanto el modelo seleccionado como los parámetros y la configuración de la app. La solicitud se realiza hacia la URL de la Cloud Function. hacer clic para visualizar [Cloud Function](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/5.%20Cloud%20functions/streamlit_funtion.py)



En cuanto al funcionamiento de la app (deploy), en cada parámetro se especifica la unidad del mismo. El usuario debe pasar solo valores numéricos. La zona de inicio y zona de fin se identifican con un número entero del 1 al 265 y dicho número está relacionado con la distribución geográfica de los barrios de NYC.
El deployment se realiza directamente desde Streamlit, vinculando un script alojado en este repositorio. Para visualizar el archivo Streamlit hacer clic en el siguiente link [Streamlit](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Streamlit/main.py)

## **Link del Deploy** 
[Sistema de prediccion](https://probando.streamlit.app/)


