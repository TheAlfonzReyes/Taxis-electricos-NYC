# <h1 align="center">**`NYC Taxis`**</h1>

<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/carro.jpeg"  >
</p>

## **Contexto**

El presente proyecto busca simula una consultora de análisis de datos la cual tiene como objetivo dar acompañamiento en la toma de desciciones de negocio a una empresa de servicios de transporte de pasajeros en New York, que actualmente se encuentra operando en el sector de micros de media y larga distancia y está interesada en invertir en el sector de transporte de pasajeros con automóviles. 

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

<h1 align = "center">Mapa de New York</h1>
<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/mapa.png" width=300 height=200 alt = "Mapa de New York" >
</p>


*Cómo se observa en el mapa, hay disponibilidad uniforme de estaciones de carga eléctrica para vehículos.*
 en el siguiente enlace se puede ver el EDA de todos los datasets [EDA](https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/tree/main/4.%20EDA-ETL)

* Se definen tres KPI's
  1. Millas promedio por galón de combustible
     Presmisa: Aumentar en un 5% las millas recorridas por galón con respecto al semestre anterior.

  2. Tiempo de carga promedio.
     Premisa: Disminuir en un 3% el tiempo de carga de todos los vehiculos.

  3. Satisfaccion del cliente
     Premisa: Aumentar un 5% la cantidad de reseñas positivas por semestre

* A continuacion, se define el Stack Tecnológico
<p align="center">
<img src="https://github.com/TheAlfonzReyes/Taxis-electricos-NYC/blob/main/Variables_entorno/Stack_tecnologico.png">
</p>
