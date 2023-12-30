### Proyecto Final
## ML para el Éxito en el Mundo de League of Legends

> [!NOTE]
> ### CODERHOUSE
> - Curso: Data Science
> - Comisión: 42390
> - Profesor: Jorge Ruiz
> - Tutores:
>   - Aldana Ruscitti
>   - Facundo Juliá
>   - Erica Destefano



## Indice
1. Introducción
    - [1.1 Contexto y Justificación del Trabajo](#11-contexto-y-justificación-del-análisis)
    - [1.2 Objetivos](#12-objetivos-del-análisis)
    - [1.3 Enfoque y Método a Seguir](#13-enfoque-y-método-a-seguir)
    - [1.4 Planificación del Trabajo](#14-planificación-del-trabajo)
    - [1.5 Breve Sumario de Productos Obtenidos](#15-breve-sumario-de-productos-obtenidos)

2. Contexto de League of Legends
    - [2.1 Descripción del Juego](#21-descripción-general)
    - [2.2 Relevancia de la Predicción de Partidas en LoL](#datos-en-league-of-legends)

3. Datos en League of Legends
    - [3.1 Base de Datos Utilizada](#31-base-de-datos-utilizada)
    - [3.2 Descripción de las Variables](#32-descripción-de-las-variables)
    - [3.3 Preprocesamiento de Datos](#33-preprocesamiento-de-datos)
    - [3.4 Optimización y Características en el Análisis Estratégico](#34-optimización-y-características-en-el-análisis-estratégico-feature-engineering)
    - [3.5 Hipótesis](#35-hipótesis-notebook)

4. Herramientas y Métodos de Machine Learning en LoL
    - [4.1 Selección de Modelos](#41-selección-de-modelos--ver)
    - [4.2 Construcción y Entrenamiento de Modelos](#42-construcción-y-entrenamiento-de-modelos)
    - [4.3 Métricas de Evaluación de Modelos](#43-métricas-de-evaluación-de-modelos)

5. Resumen de analisis
    - [5.1 Unificación de Modelos para Mejor Rendimiento](#51-unificación-de-modelos-para-mejor-rendimiento--notebook)

---
## Introducción y Contexto
### 1.1 Contexto y Justificación del Análisis

League of Legends, desarrollado por Riot Games, ha emergido como un fenómeno global en el ámbito de los deportes electrónicos. Este juego en línea de estrategia y acción ha experimentado un crecimiento meteórico, atrayendo a millones de jugadores y espectadores en todo el mundo. Con su base de usuarios que ha superado los 155 millones en 2021, League of Legends se ha convertido en una potencia indiscutible en la industria.

El juego se centra en la estrategia y la colaboración en equipo, con cada campeón poseyendo roles y habilidades únicas. La acumulación de oro y experiencia durante las partidas permite a los jugadores mejorar y fortalecer a sus campeones, añadiendo capas de complejidad y toma de decisiones estratégicas.

El crecimiento exponencial de League of Legends se refleja no solo en su base de jugadores, sino también en la audiencia de torneos de élite, como el Campeonato Mundial. Desde 2010, con aproximadamente 1 millón de usuarios conectados diariamente, hasta 2021, con más de 31 millones, el juego ha experimentado un aumento astronómico en la participación diaria.

### 1.2 Objetivos del Análisis
El propósito de este análisis es examinar detenidamente un conjunto de datos que comprende partidas clasificatorias Diamante de League of Legends en los primeros 10 minutos. Con alrededor de 10,000 partidas y jugadores de niveles similares, el objetivo es proporcionar información valiosa para equipos que buscan optimizar su rendimiento y estrategias en el juego.
1. **Evaluar el Impacto de Estadísticas Clave**: Analizar en profundidad las estadísticas cruciales de las partidas clasificatorias Diamante en los primeros 10 minutos, como asesinatos, muertes, oro, experiencia, y nivel, para entender su relación con los resultados de las partidas.
2. **Identificar Patrones y Tendencias**: Descubrir patrones y tendencias emergentes en los datos que puedan ofrecer información estratégica. Esto podría incluir correlaciones entre la colocación de objetos como Warding totems, el desempeño individual, y la ventaja económica, entre otros.
3. **Desarrollar Insights Accionables**: Traducir los hallazgos del análisis en insights accionables para equipos de League of Legends. Estos insights podrían abordar tácticas específicas, roles críticos en la partida, o la importancia de ciertos objetivos, contribuyendo así a la mejora del rendimiento en partidas clasificatorias Diamante.

### 1.3 Enfoque y Método a Seguir
Para alcanzar nuestros objetivos, se utilizará un enfoque analítico de datos, explorando estadísticas específicas de las partidas clasificatorias Diamante. Este análisis proporcionará percepciones clave sobre patrones y tendencias que podrían influir en el resultado de las partidas.

### 1.4 Planificación del Trabajo
La planificación del proyecto incluirá tareas específicas, desde la adquisición y limpieza de datos hasta la implementación de modelos de machine learning. Un calendario detallado se establecerá para garantizar una ejecución eficiente y cumplir con los plazos establecidos.

### 1.5 Breve Sumario de Productos Obtenidos
Los resultados de este análisis proporcionarán información valiosa que puede utilizarse para mejorar el rendimiento y las estrategias de los equipos en las partidas clasificatorias Diamante de League of Legends.

## Contexto de League of Legends
### 2.1 Descripción General
League of Legends (LoL), creado por Riot Games, es un juego en línea de estrategia y acción que ha dejado una marca indeleble en el mundo de los deportes electrónicos. Este fenómeno global atrae a jugadores de todo el mundo a competir en partidas altamente estratégicas y emocionantes.

![mapa](https://www.pinnacle.com/Cms_Data/Contents/Guest/Media/esports2017/Article-Images/LoL/2019/2019-How-to-improve-your-lol-predictions/Esports-Hero-Esports-How-to-improve-your-LoL-predictions.jpg)

El juego se desarrolla en un campo de batalla virtual donde dos equipos, cada uno conformado por cinco jugadores, compiten por la victoria. Cada jugador asume el papel de un "campeón", un personaje único con habilidades y roles específicos. La clave del éxito radica en la coordinación del equipo, la elección de estrategias efectivas y la adaptabilidad durante las partidas.

![historial](/static/img/Historial.png)

El crecimiento fenomenal de League of Legends se refleja en cifras impresionantes. Desde sus inicios en 2009, el juego ha experimentado un aumento espectacular en su base de usuarios, superando los 155 millones en 2021. Este crecimiento no se limita solo a jugadores, ya que los espectadores de torneos importantes también han aumentado significativamente.

## Datos en League of Legends
### 3.1 Base de Datos Utilizada
El análisis se basa en un conjunto de datos recopilados de partidas clasificatorias Diamante de League of Legends. Estos datos proporcionan una instantánea de las estadísticas clave durante los primeros 10 minutos de cada partida, permitiendo una exploración detallada de los factores que influyen en la victoria o derrota del equipo azul.

El conjunto de datos utilizado en este proyecto proviene de Kaggle, una reconocida plataforma para compartir conjuntos de datos y participar en desafíos de ciencia de datos. El dataset específico, titulado "League of Legends Diamond Ranked Games (10 min)", fue creado y compartido por el autor YI LAN MA.

### 3.2 Descripción de las Variables
El conjunto de datos contiene diversas variables que capturan diferentes aspectos del desempeño de los equipos. A continuación, se presenta una breve descripción de algunas de las variables más relevantes:
- **Wins**: Número de victorias del equipo azul (1 si ganó, 0 si perdió).
- **WardsPlaced**: Cantidad de "Warding totems" colocados por el equipo.
- **Kills**: Número de asesinatos realizados por el equipo.
- **TowersDestroyed**: Torres destruidas por el equipo.
- **Dragons**: Número de dragones asegurados por el equipo.
- **Heralds**: Número de Herald asegurados por el equipo.
- **TotalGold**: Oro total obtenido por el equipo en los primeros 10 minutos.
- **ExperienceDiff**: Diferencia total de experiencia entre el equipo y el equipo contrario.

Esta es solo una selección de variables; el conjunto de datos completo abarca diversas métricas que proporcionan una visión completa del rendimiento de los equipos en la fase inicial de la partida.

### 3.3 Preprocesamiento de Datos ([Notebook](/notebooks/000_Wranging.ipynb))
Antes de realizar el análisis exploratorio, se llevó a cabo un proceso de preprocesamiento de datos para garantizar la calidad y coherencia de la información. Este proceso incluyó:
- **Manejo de Datos Faltantes**: Verificación y tratamiento de cualquier dato faltante para evitar sesgos en el análisis.
- **Normalización de Variables**: Ajuste de escalas para variables que podrían tener magnitudes diferentes.
- **Codificación de Variables Categóricas**: Convertir variables categóricas en un formato adecuado para el análisis. 

![correlacion](/static/img/correlacion_total.png)


### 3.4 Optimización y Características en el Análisis Estratégico ([Notebook](/notebooks/005_Features.ipynb))
La elección de conjuntos de características en feature engineering es clave para alinearlos con objetivos específicos y conocimiento del juego. Integrar múltiples aspectos del juego mejora la capacidad del modelo para capturar interacciones complejas entre variables. Esta estrategia no solo mejora el rendimiento del modelo, sino que también fortalece la interpretación de resultados al considerar diversas dimensiones del rendimiento y estrategia del equipo. La sinergia entre la elección cuidadosa de features y el entendimiento del contexto del juego es crucial para construir modelos más robustos y contextualmente relevantes.

#### Conjunto de Características de Visión:
1. **Features**:
    - WardsPlaced
    - WardsDestroyed
    - EliteMonsters
    - Dragons
    - Heralds
    - TowersDestroyed
2. **Importancia**:
    - Proporciona información sobre el control del equipo en el mapa.
    - Puede influir en estrategias de rotación y control de objetivos.

#### Conjunto de Características de Rendimiento en Combate:
1. **Features**:
    - FirstBlood
    - Kills
    - Deaths
    - Assists
    - TotalGold
    - GoldDiff
    - ExperienceDiff
    - CSPerMin
    - GoldPerMin
2. **Importancia**:
    - Refleja el desempeño individual y colectivo en combate.
    - Puede influir en la acumulación de recursos y ventajas para el equipo.

#### Conjunto de Características de Desarrollo y Experiencia:
1. **Features**:
    - AvgLevel
    - TotalExperience
    - TotalMinionsKilled
    - TotalJungleMinionsKilled
2. **Importancia**:
    - Muestra el crecimiento y desarrollo de los campeones del equipo.
    - Puede influir en la capacidad del equipo para enfrentar desafíos más avanzados.

#### Conjunto de Características de Combate Temprano:
1. **Features**:
    - FirstBlood
    - Kills
    - Deaths
    - Assists
    - WardsPlaced
    - WardsDestroyed
2. **Importancia**:
    - Se centra en eventos tempranos que podrían influir en el curso del juego.
    - Puede revelar estrategias y decisiones cruciales en las etapas iniciales.

#### Conjunto de Características Económicas:
1. **Features**:
    - TotalGold
    - GoldPerMin
    - GoldDiff
2. **Importancia**:
    - Evalúa la capacidad del equipo para acumular recursos económicos.
    - Puede reflejar ventajas económicas y desventajas durante el juego.

#### Conjunto de Características de Desempeño en Dragones y Heralds:
1. **Features**:
    - Dragons
    - Heralds
    - GoldDiff
    - ExperienceDiff
2. **Importancia**:
    - Evalúa el éxito en la captura de objetivos importantes.
    - Puede influir en la ventaja estratégica y táctica del equipo.

### 3.5 Hipótesis ([Notebook](/notebooks/004_Hypothesis.ipynb))
Estas hipótesis proporcionan una base sólida para realizar pruebas y análisis más detallados sobre el dataset de League of Legends. Al evaluar cada una de estas hipótesis y validarlas con datos, el equipo podrá obtener una mejor comprensión de los factores que realmente influyen en el rendimiento y la probabilidad de victoria en el juego.

1. **Hipótesis 1**: Relación entre asesinatos y tasa de victoria?
    
    **Resultado**: El número de asesinatos conseguidos por un equipo en los primeros 10 minutos se correlacionará positivamente con su tasa de victoria. Cuanto mayor sea la cantidad de asesinatos, más alta será la probabilidad de ganar.

    ![Hypothesis_001](/static/img/Hypothesis_001.png)

2. **Hipótesis 2**: Impacto de objetivos neutrales en la victoria? 
   
    **Resultados**: Equipos que aseguran más dragones y Herald durante los primeros 10 minutos tendrán una mayor probabilidad de ganar la partida, ya que estos objetivos proporcionan beneficios significativos para todo el equipo.

    ![Hypothesis_002A](/static/img/Hypothesis_002A.png)
    ![Hypothesis_002B](/static/img/Hypothesis_002B.png)

3. **Hipótesis 3**: Importancia de la ventaja económica y de experiencia?
    
    **Resultado**: Equipos que logran una ventaja significativa en oro y experiencia sobre el equipo contrario en los primeros 10 minutos tendrán mayores posibilidades de obtener la victoria.

    ![Hypothesis_003](/static/img/Hypothesis_003.png)

    Tabla descriptiva:
    | | GoldDiff | ExperienceDiff |	GoldDiff | ExperienceDiff |
    |---|---|---|---|---|
    | count | 9879 | 9879 | 9879 | 9879 |
    | mean | 1253 | 940 | -1253 | -940 |
    | std | 2108 | 1674 | 2108 | 1674 |
    | min | -6744 | -5355 | -11467 | -9333 |
    | 25% | -154 | -182 | -2574 | -2012 |
    | 50% | 1182 | 899 | -1182 | -899 |
    | 75% |2574 | 2012 | 154 | 182 |
    | max | 11467 | 9333 | 6744 | 5355 |

4. **Hipótesis 4**: Contribución individual y tasa de victoria?

    **Resultado**: Jugadores que contribuyen con un mayor número de asistencias tendrán un impacto positivo en la tasa de victoria de su equipo en las partidas clasificatorias Diamante.
    ![Hypothesis_004](/static/img/Hypothesis_004.png)

5. **Hipótesis 5**: Nivel promedio y probabilidad de victoria?

    **Resultado**: Un equipo con un mayor nivel promedio de sus jugadores durante los primeros 10 minutos tendrá una leve probabilidad de ganar la partida.
    ![Hypothesis_005](/static/img/Hypothesis_005.png)


## Herramientas y Métodos de Machine Learning en LoL
En el entorno competitivo de League of Legends, donde la estrategia y la coordinación son esenciales, la aplicación de herramientas y métodos de machine learning se presenta como un recurso valioso para optimizar el rendimiento de los equipos. Este análisis detallado se enfoca en la selección y aplicación de diversas técnicas de machine learning para examinar partidas clasificatorias Diamante en los primeros 10 minutos del juego.


### 4.1 Selección de Modelos ( [Ver](/models/) )

En el proceso de evaluación y predicción del resultado de partidas clasificatorias en League of Legends, se han aplicado tres modelos de aprendizaje automático: KNN, Random Forest y Decision Tree. Cada modelo fue entrenado y evaluado con seis conjuntos distintos de características, permitiendo así una exhaustiva exploración de los factores que impactan en la victoria o derrota del equipo azul. A continuación, se presentan los resultados destacados de cada modelo junto con el conjunto de características que maximizó su precisión:

| Modelo | Features Set | KNN Accuracy | Random Forest Accuracy | Decision Tree Accuracy |
|---|---|---|---|---|
| Modelo 1 | Visión | 57.99% | 58.90% | 57.34% |
| Modelo 2 | Rendimiento en Combate | 71.20% | 71.66% | 69.69% |
| Modelo 3 | Desarrollo y Experiencia | 65.18% | 63.87% | 62.04% |
| Modelo 4 | Combate Temprano | 68.67% | 69.48% | 67.91% |
| Modelo 5 | Económicas | 70.44% | 71.71% | 69.38% |
| Modelo 6 | Desempeño en Dragones y Heralds | 71.45% | 72.27% | 71.00% |




### 4.2 Construcción y Entrenamiento de Modelos
La construcción y entrenamiento de modelos involucran la preparación de datos y el ajuste de parámetros. En este contexto:

Para la construcción de los modelos, importamos los conjuntos de datos procesados a partir del conjunto de datos original. Utilizamos los datos del Team Blue para el entrenamiento y los del Team Red para la validación. Posteriormente, importamos el diccionario feature.json, que contiene los arreglos de columnas específicos para cada modelo, junto con otras características relevantes.

Para cada conjunto de características, procedemos a construir un modelo correspondiente. Numeramos y almacenamos estos modelos para llevar a cabo las validaciones pertinentes posteriormente.

![proceso](/static/img/proceso.png)

En este ejemplo, observamos cómo el uso de cada conjunto de características estimadas influye en la evolución de los modelos, como se ilustra específicamente en el caso del algoritmo KNN.

![knn_features_comparations](/static/img/knn_features_comparations.png)

### 4.3 Métricas de Evaluación de Modelos
#### 4.3.1 Precisión, Sensibilidad, Especificidad:
Estas métricas evalúan el rendimiento de los modelos en términos de la capacidad para prever victorias y derrotas. La precisión mide la proporción de predicciones correctas en general, mientras que sensibilidad y especificidad se centran en la capacidad del modelo para identificar verdaderos positivos y verdaderos negativos, respectivamente.

#### 4.3.2 KNN ( [Ver](/models/KNN/) ):
En el análisis del rendimiento de modelos KNN, seis modelos fueron entrenados utilizando diversos conjuntos de características. Destaca el Modelo 6, centrado en "Desempeño en Dragones y Heralds", alcanzando una máxima precisión del 71.45%. La optimización de cada modelo se ilustra en un gráfico de mejora. La evaluación del rendimiento mediante matrices de confusión revela detalles específicos para cada modelo. Por ejemplo, el Modelo 3 logró una precisión del 65.18%, con cero falsos negativos, mientras que el Modelo 4 mostró una variación en los patrones de error con 949 falsos negativos y 3487 falsos positivos. Este análisis proporciona una visión detallada del rendimiento de cada modelo, destacando áreas de fortaleza y oportunidades de mejora. La elección del modelo óptimo dependerá de consideraciones específicas del caso de uso y la importancia atribuida a diferentes tipos de errores.

![knn_Matrices_confusión](/static/img/knn_Matrices_confusión.png)
![knn_curve_roc](/static/img/knn_curve_roc.png)

#### 4.3.3 Random Forest ( [Ver](/models/Random_Forest/) ):

En este estudio del desempeño de modelos Random Forest, se entrenaron seis modelos con conjuntos específicos de características, destacando el Modelo 6 con "Desempeño en Dragones y Heralds" como el más preciso, logrando una máxima precisión del 72.27%. La evaluación detallada mediante matrices de confusión reveló que, aunque este modelo tuvo un notable éxito con 3564 Verdaderos Positivos, también presentó desafíos, incluyendo 1385 Falsos Negativos y 1354 Falsos Positivos. La elección del modelo más eficiente dependerá de los objetivos específicos del caso de uso, y se recomienda una evaluación cuidadosa junto con la exploración de estrategias adicionales para mejorar el rendimiento global del modelo.

![rf_Matrices_confusión](/static/img/rf_Matrices_confusión.png)
![rf_curve_roc](/static/img/rf_curve_roc.png)

#### 4.3.4 Decision Tree ( [Ver](/models/Decision_Tree/) ):
Los modelos, entrenados con diversos conjuntos, exhibieron máximas precisiones, destacando el Modelo 6 con "Desempeño en Dragones y Heralds" logrando un 71.00%. La evaluación del rendimiento mediante matrices de confusión reveló variaciones notables en los patrones de error para cada modelo y conjunto de características, proporcionando una visión detallada de su desempeño.

![df_Matrices_confusión](/static/img/df_Matrices_confusión.png)
![df_curve_roc](/static/img/df_curve_roc.png)

## Resumen de analisis
### 5.1 Unificación de Modelos para Mejor Rendimiento  ( [Notebook](/notebooks/006_Resumen.ipynb) )
Después de obtener tres modelos distintos para cada combinación de características según las estrategias de juego, se avanzó hacia la unificación de estos modelos. Este proceso culminó en la creación de un algoritmo que estima la factibilidad de victoria basándose en los datos procesados por los modelos más efectivos. El resultado de esta síntesis se presenta de manera visual a través de un gráfico, proporcionando así una perspectiva consolidada sobre la probabilidad de éxito en función de las características seleccionadas. Este enfoque integrado busca maximizar la capacidad predictiva y facilitar una comprensión más completa de los factores que influyen en el desempeño en partidas clasificatorias de League of Legends.

![estimacion_test](/static/img/estimacion_test.png)
- Estimación de Porcentaje de Victoria según KNN: 16.67%
- Estimación de Porcentaje de Victoria según Decision Tree: 50.0%
- Estimación de Porcentaje de Victoria según Random Forest: 33.33%


Aunque algunos modelos presentan un rendimiento inferior en comparación con otros, han demostrado su capacidad para identificar partidas que se desvían del estándar, incluyendo las notorias "remontadas épicas". Además, al considerar una estimación de victoria superior al 50%, se observa que el análisis es capaz de prever victorias con un 88% de precisión en base a los datos examinados. Este enfoque también proporciona insights valiosos al determinar qué estrategias de juego tienen el potencial de ser efectivas para asegurar la victoria en la partida. En conjunto, estos hallazgos resaltan la utilidad de los modelos, incluso aquellos con un rendimiento aparentemente inferior, al ofrecer una comprensión profunda y específica de situaciones de juego únicas.

# Literatura y Recursos de Investigación:
A continuación, enumero los libros y blogs que he consultado durante el desarrollo del proyecto para aplicar sus enseñanzas de manera efectiva.

## Libros:
- **Feature Engineering for Machine Learning** - Alice Zheng, Amanda Casari
- **Bootstrap y Métodos de Ensamblado** - Bradley Efron, Robert J. Tibshirani
- **Natural Language Processing with Python** - Steven Bird, Ewan Klein, Edward Loper

## Blogs:
- [GridSearchCV for Beginners](https://towardsdatascience.com/gridsearchcv-for-beginners-db48a90114ee) - Scott Okamura
- [20 Statistical Concepts Every Data Scientist/Analyst Should Know](https://medium.com/codex/20-statistical-concepts-every-data-scientist-analyst-should-know-2d28a06a5483) - Anmol Tomar
- [Your Dataset Has Missing Values? Do Nothing!](https://towardsdatascience.com/your-dataset-has-missing-values-do-nothing-10d1633b3727) - 
Samuele Mazzanti
- [One-Class SVM For Anomaly Detection](https://medium.com/grabngoinfo/one-class-svm-for-anomaly-detection-6c97fdd6d8af) - Amy @GrabNGoInfo
- [XGBoost 2.0: Major update on Tree-based methods](https://medium.com/aiguys/xgboost-2-0-major-update-on-tree-based-methods-2e4bc4f15baf) - Vishal Rajput
- [How to not be dumb at applying Principal Component Analysis (PCA)?](https://medium.com/data-design/how-to-not-be-dumb-at-applying-principal-component-analysis-pca-6c14de5b3c9d) - Laurae
- [Principal Component Analysis (PCA) Explained Visually with Zero Math](https://towardsdatascience.com/principal-component-analysis-pca-explained-visually-with-zero-math-1cbf392b9e7d) - Casey Cheng
- [Become a Pokémon Master with Machine Learning](https://towardsdatascience.com/become-a-pok%C3%A9mon-master-with-machine-learning-f61686542ef1) - Kartikeya Rana
- [ML Dataset — How To Prepare a Good One?](https://betterprogramming.pub/ml-dataset-how-to-prepare-a-good-one-7d92ce1d45e5) - Rafal Pytel