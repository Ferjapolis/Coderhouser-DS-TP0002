# ML para el Éxito en el Mundo de League of Legends

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

### 3.3 Preprocesamiento de Datos ([Data Wranging](/notebooks/000_Wranging.ipynb))
Antes de realizar el análisis exploratorio, se llevó a cabo un proceso de preprocesamiento de datos para garantizar la calidad y coherencia de la información. Este proceso incluyó:
- **Manejo de Datos Faltantes**: Verificación y tratamiento de cualquier dato faltante para evitar sesgos en el análisis.
- **Normalización de Variables**: Ajuste de escalas para variables que podrían tener magnitudes diferentes.
- **Codificación de Variables Categóricas**: Convertir variables categóricas en un formato adecuado para el análisis. 

![correlacion](/static/img/correlacion_total.png)
( ver el notebook [005_Features](/notebooks/005_Features.ipynb) )

### 3.4 Optimización y Características en el Análisis Estratégico ([Feature Engineering](/notebooks/005_Features.ipynb))
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

## Herramientas y Métodos de Machine Learning en LoL
En el entorno competitivo de League of Legends, donde la estrategia y la coordinación son esenciales, la aplicación de herramientas y métodos de machine learning se presenta como un recurso valioso para optimizar el rendimiento de los equipos. Este análisis detallado se enfoca en la selección y aplicación de diversas técnicas de machine learning para examinar partidas clasificatorias Diamante en los primeros 10 minutos del juego.
### 4.1 Selección de Modelos ( [Ver](/models/) )
#### 4.1.1 KNN ( [Ver](/models/KNN/) ):
En el análisis del rendimiento de modelos KNN, seis modelos fueron entrenados utilizando diversos conjuntos de características. Destaca el Modelo 6, centrado en "Desempeño en Dragones y Heralds", alcanzando una máxima precisión del 71.45%. La optimización de cada modelo se ilustra en un gráfico de mejora. La evaluación del rendimiento mediante matrices de confusión revela detalles específicos para cada modelo. Por ejemplo, el Modelo 3 logró una precisión del 65.18%, con cero falsos negativos, mientras que el Modelo 4 mostró una variación en los patrones de error con 949 falsos negativos y 3487 falsos positivos. Este análisis proporciona una visión detallada del rendimiento de cada modelo, destacando áreas de fortaleza y oportunidades de mejora. La elección del modelo óptimo dependerá de consideraciones específicas del caso de uso y la importancia atribuida a diferentes tipos de errores.
| Modelo | Features Set | Max Accuracy |
|---|---|---|
| Modelo 1 | Visión | **57.99%** |
| Modelo 2 | Rendimiento en Combate | **71.20%** |
| Modelo 3 | Desarrollo y Experiencia | **65.18%** |
| Modelo 4 | Combate Temprano | **68.67%** |
| Modelo 5 | Económicas | **70.44%** |
| Modelo 6 | Desempeño en Dragones y Heralds | **71.45%** |

![grafico_mejora](/static/img/knn_Matrices_confusión.png)

#### 4.1.2 Random Forest ( [Ver](/models/Random_Forest/) ):

En este estudio del desempeño de modelos Random Forest, se entrenaron seis modelos con conjuntos específicos de características, destacando el Modelo 6 con "Desempeño en Dragones y Heralds" como el más preciso, logrando una máxima precisión del 72.27%. La evaluación detallada mediante matrices de confusión reveló que, aunque este modelo tuvo un notable éxito con 3564 Verdaderos Positivos, también presentó desafíos, incluyendo 1385 Falsos Negativos y 1354 Falsos Positivos. La elección del modelo más eficiente dependerá de los objetivos específicos del caso de uso, y se recomienda una evaluación cuidadosa junto con la exploración de estrategias adicionales para mejorar el rendimiento global del modelo.

| Modelo | Features Set | Max Accuracy |
|---|---|---|
| Modelo 1 | Visión | **58.90%** |
| Modelo 2 | Rendimiento en Combate | **71.66%** |
| Modelo 3 | Desarrollo y Experiencia | **63.87%** |
| Modelo 4 | Combate Temprano | **69.48%** |
| Modelo 5 | Económicas | **71.71%** |
| Modelo 6 | Desempeño en Dragones y Heralds | **72.27%** |

![grafico_mejora](/static/img/rf_Matrices_confusión.png)

#### 4.1.3 :

#### 4.1.4 Redes Neuronales:

### 4.2 Construcción y Entrenamiento de Modelos
La construcción y entrenamiento de modelos involucran la preparación de datos y el ajuste de parámetros. En este contexto:

Preprocesamiento de Datos: La normalización de variables, manejo de valores atípicos y codificación de variables categóricas son pasos esenciales.

Entrenamiento del Modelo: Se realizará utilizando conjuntos de entrenamiento y validación, y se ajustarán parámetros para mejorar el rendimiento del modelo.

### 4.3 Métricas de Evaluación de Modelos
#### 4.3.1 Precisión, Sensibilidad, Especificidad:
Estas métricas evalúan el rendimiento de los modelos en términos de la capacidad para prever victorias y derrotas. La precisión mide la proporción de predicciones correctas en general, mientras que sensibilidad y especificidad se centran en la capacidad del modelo para identificar verdaderos positivos y verdaderos negativos, respectivamente.

#### 4.3.2 Curva ROC:
La Curva ROC proporciona una representación visual de la sensibilidad frente a la tasa de falsos positivos en diferentes umbrales de clasificación, ofreciendo información valiosa sobre el rendimiento del modelo en distintos escenarios.

### 4.4 Consideraciones Específicas para Modelos en Juegos
Los juegos, como League of Legends, presentan desafíos únicos para la aplicación de modelos de machine learning:
- **Interpretación de Resultados**: La interpretación de los resultados de los modelos debe ser accesible para los jugadores y entrenadores, lo que implica traducir las predicciones en estrategias tangibles.
- **Adaptabilidad**: Dado que el metajuego de League of Legends evoluciona constantemente, los modelos deben ser adaptables para capturar nuevas tendencias y estrategias.
- **Combinación con Conocimiento del Juego**: La integración de la experiencia y conocimientos de los jugadores profesionales puede mejorar la efectividad de los modelos al considerar aspectos estratégicos específicos del juego.
