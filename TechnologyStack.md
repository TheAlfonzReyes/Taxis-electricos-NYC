# Tech Stack

Este análisis detalla las razones de la utilizacion de cada tecnología en el proyecto.

# 
1. Python:

    Por qué: es un lenguaje versátil ampliamente utilizado en ciencia de datos debido a sus extensas bibliotecas para manipulación, análisis y aprendizaje automático de datos. Librerías como NumPy, Pandas, scikit-learn y TensorFlow brindan herramientas integrales para limpieza de datos, preprocesamiento, desarrollo y evaluación de modelos.

    Para qué: usamos Python para todas las etapas de nuestro proyecto, incluyendo ingesta de datos, limpieza, exploración, ingeniería de características, desarrollo y evaluación de modelos. Utilizamos cuadernos Jupyter para exploración y análisis interactivos.

# 
2. SQL:

    Por qué: gestiona eficientemente los datos almacenados en bases de datos. Lo usamos porque permite estructurar nuestros datos, crear tablas, definir relaciones entre ellas y ejecutar consultas para recuperar información específica.

    Para qué: Utilizamos SQL para extraer datos relevantes de nuestras bases de datos e importarlos a Python para un análisis y modelado posterior. También podemos usar SQL dentro de herramientas como BigQuery para analizar directamente conjuntos de datos más grandes.

# 
3. Google Cloud Composer:

    Por qué: orquestación de flujos de trabajo a gran escala: Composer facilita la gestión de flujos de trabajo complejos con Apache Airflow en Google Cloud. Su interfaz intuitiva y escalable permite la automatización de tareas repetitivas y la creación de pipelines de datos eficientes.

    Para qué: agilidad y control, esta herramienta permite la programación y monitorización de flujos de trabajo, la gestión de dependencias entre tareas y la escalabilidad automática para satisfacer las necesidades del proyecto. Su integración con otras tecnologías de Google Cloud facilita la creación de pipelines de datos completos y la gestión de recursos en la nube.

# 
4. Google Cloud Functions

    Por qué: la simplicidad y eficiencia de GCF elimina la necesidad de aprovisionar y administrar servidores, simplificando la gestión y optimizando costos. Su escalabilidad automática se adapta a la demanda sin intervención manual, lo que lo convierte en una solución flexible y eficiente.

    Para qué: es ideal para ejecutar tareas puntuales como procesamiento versatilmente en tiempo real, ejecución asincrónica, envío de notificaciones o automatización de scripts. Su integración con otras tecnologías de Google Cloud facilita la creación de flujos de trabajo complejos sin necesidad de servidores.

# 
5. Google Cloud Storage:

    Por qué: ofrece una plataforma escalable y rentable para almacenar grandes conjuntos de datos, resultados intermedios y modelos entrenados. Su alta disponibilidad y durabilidad garantizan un acceso seguro y protección contra la pérdida de datos.

    Para qué: para almacenar datos sin procesar, conjuntos de datos preprocesados, modelos entrenados y otros artefactos en Cloud Storage. Aprovechando su integración con otros servicios de Google Cloud para una despliegue y acceso de datos sin problemas.

# 
6. Google Cloud BigQuery:

    Por qué: un almacén de datos escalable optimizado para análisis de datos a gran escala utilizando consultas similares a SQL. Permite una exploración y análisis eficientes de conjuntos de datos a escala de petabytes sin necesidad de administrar la infraestructura.

    Para qué: para almacenar y analizar directamente conjuntos de datos masivos, especialmente cuando se necesitan consultas ad-hoc frecuentes o agregaciones a gran escala. También podemos aprovechar BigQuery ML para el entrenamiento e implementación in situ de modelos de aprendizaje automático en nuestros datos.

# 
7. Power BI: 

    Por qué: permite visualizaciones de datos de forma intuitiva, creando informes interactivos y visualizaciones atractivas de sus datos, facilitando la comprensión y el análisis de información compleja.

    Para qué: principalmente, por la toma de decisiones basada en datos. Esta herramienta nos facilita la exploración y el análisis de datos, la identificación de tendencias y patrones, y la toma de decisiones informadas. Su integración con diferentes fuentes de datos permite obtener una visión completa del negocio.

# 
PD: Este documento es de ruta potencial y las herramientas específicas, su uso pueden variar según los requisitos específicos de nuestro proyecto y las características de los datos. Consideramos evaluar y ajustar en función de nuestras necesidades reales y experimentar con diferentes combinaciones para encontrar el flujo de trabajo óptimo para nuestras tareas de ciencia de datos.
# 