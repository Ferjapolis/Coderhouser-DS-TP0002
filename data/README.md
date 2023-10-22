# Datasets
## Introducción:

League of Legends, uno de los juegos en línea más populares y competitivos del mundo, atrae a millones de jugadores de todas partes. Cada partida en este emocionante universo de batallas requiere una estrategia cuidadosamente elaborada y la toma de decisiones en tiempo real. Para comprender mejor los factores que influyen en el resultado de las partidas y para predecir qué equipo se alzará con la victoria, los científicos de datos y entusiastas del juego han recurrido a una valiosa fuente de información: los datasets de League of Legends.

Estos datasets, disponibles en plataformas como Kaggle, contienen información detallada sobre las partidas, ofreciendo una visión profunda de los eventos que ocurren en los primeros 10 minutos de juego. Lo más destacado es que estos datos se han dividido en dos equipos, "blueTeam" y "redTeam", lo que permite un análisis comparativo de su rendimiento y estadísticas. Además, es importante señalar que estos datasets están completamente limpios, sin datos nulos, lo que facilita su uso para la construcción de modelos predictivos y análisis detallados.

## Glosario
- **Tótem guardián**: un elemento que un jugador puede colocar en el mapa para revelar el área cercana. Muy útil para el control de mapas/objetivos.
- **Minions**: NPC que pertenecen a ambos equipos. Dan oro cuando los jugadores los matan.
- **Minions de la selva**: NPC que no pertenecen a NINGÚN EQUIPO. Dan oro y ventajas cuando los jugadores los matan.
- **Monstruos de élite**: Monstruos con alto HP/daño que otorgan una enorme bonificación (oro/XP/estadísticas) cuando los mata un equipo.
- **Dragones**: Monstruo de élite que otorga bonificación al equipo cuando muere. El cuarto dragón asesinado por un equipo otorga una enorme bonificación a las estadísticas. El quinto dragón (Dragón anciano) ofrece una gran ventaja al equipo.
- **Heraldo**: Monstruo de élite que otorga una bonificación de estadísticas cuando el jugador lo mata. Ayuda a empujar un carril y destruye estructuras.
- **Torres**: Estructuras que debes destruir para llegar al Nexus enemigo. Dan oro.
- **Nivel**: Nivel campeón. Empieza en 1. Max tiene 18.

## Tablas:

### high_diamond_ranked_10min.csv

#### Origen del Dataset:
Este dataset proviene de Kaggle, una plataforma en línea que aloja datasets y competencias de ciencia de datos. Fue recopilado con el propósito de analizar partidas de League of Legends con un enfoque en los primeros 10 minutos de juego.

Link: [Kaggle](https://www.kaggle.com/datasets/bobbyscience/league-of-legends-diamond-ranked-games-10-min?resource=download)

#### Tamaño del Dataset:
Este dataset consta de un total de 40 columnas, cada una con su propia descripción, y un total de 9879 registros de partidas. El tamaño del dataset, es decir, el número de filas, es de 9879, lo que permite un análisis estadístico significativo.

#### Ausencia de Datos Nulos:
Uno de los aspectos notables de este dataset es que no contiene datos nulos (missing values). Esto significa que cada celda en el conjunto de datos contiene un valor válido para su respectiva columna. La ausencia de datos nulos simplifica el análisis de datos y las tareas de modelado predictivo, ya que no es necesario lidiar con la imputación o eliminación de datos faltantes.

|Número | Columna | Descripción | Dtype|
|---|---|---|---|
|0 | gameId | Identificador único para cada juego clasificado de League of Legends. | int64|
|1 | blueWins | Valor objetivo que se intenta predecir: 1 si el equipo azul ganó, 0 si el equipo rojo ganó. | int64|
|2 | blueWardsPlaced | Cantidad de "Warding totems" (elementos de visión) colocados por el equipo azul. | int64|
|3 | blueWardsDestroyed | Cantidad de "Warding totems" del equipo azul que fueron destruidos por el equipo rojo. | int64|
|4 | blueFirstBlood | Valor binario (0 o 1) que indica si el equipo azul fue el primero en obtener una muerte ("First Blood"). | int64|
|5 | blueKills | Número de asesinatos conseguidos por el equipo azul en los primeros 10 minutos del juego. | int64|
|6 | blueDeaths | Número de muertes sufridas por el equipo azul en los primeros 10 minutos del juego. | int64|
|7 | blueAssists | Número de asistencias realizadas por el equipo azul en los primeros 10 minutos del juego. | int64|
|8 | blueEliteMonsters | Cantidad de monstruos de élite (como dragones o Heralds) eliminados por el equipo azul. | int64|
|9 | blueDragons | Cantidad de dragones eliminados por el equipo azul. | int64|
|10 | blueHeralds | Cantidad de Heralds eliminados por el equipo azul. | int64|
|11 | blueTowersDestroyed | Cantidad de torres destruidas por el equipo azul. | int64|
|12 | blueTotalGold | Cantidad total de oro obtenida por el equipo azul en los primeros 10 minutos del juego. | int64|
|13 | blueAvgLevel | Nivel promedio de los campeones del equipo azul en los primeros 10 minutos del juego. | float64|
|14 | blueTotalExperience | Cantidad total de experiencia obtenida por el equipo azul en los primeros 10 minutos del juego. | int64|
|15 | blueTotalMinionsKilled | Cantidad total de minions asesinados por el equipo azul en los primeros 10 minutos del juego. | int64|
|16 | blueTotalJungleMinionsKilled | Cantidad total de minions de la jungla asesinados por el equipo azul en los primeros 10 minutos del juego. | int64|
|17 | blueGoldDiff | Diferencia de oro entre el equipo azul y el equipo rojo en los primeros 10 minutos del juego. | int64|
|18 | blueExperienceDiff | Diferencia de experiencia entre el equipo azul y el equipo rojo en los primeros 10 minutos del juego. | int64|
|19 | blueCSPerMin | Promedio de minions asesinados por minuto por el equipo azul en los primeros 10 minutos del juego. | float64|
|20 | blueGoldPerMin | Promedio de oro obtenido por minuto por el equipo azul en los primeros 10 minutos del juego. | float64|
|21 | redWardsPlaced | Cantidad de "Warding totems" (elementos de visión) colocados por el equipo rojo. | int64|
|22 | redWardsDestroyed | Cantidad de "Warding totems" del equipo rojo que fueron destruidos por el equipo azul. | int64|
|23 | redFirstBlood | Valor binario (0 o 1) que indica si el equipo rojo fue el primero en obtener una muerte ("First Blood"). | int64|
|24 | redKills | Número de asesinatos conseguidos por el equipo rojo en los primeros 10 minutos del juego. | int64|
|25 | redDeaths | Número de muertes sufridas por el equipo rojo en los primeros 10 minutos del juego. | int64|
|26 | redAssists | Número de asistencias realizadas por el equipo rojo en los primeros 10 minutos del juego. | int64|
|27 | redEliteMonsters | Cantidad de monstruos de élite (como dragones o Heralds) eliminados por el equipo rojo. | int64|
|28 | redDragons | Cantidad de dragones eliminados por el equipo rojo. | int64|
|29 | redHeralds | Cantidad de Heralds eliminados por el equipo rojo. | int64|
|30 | redTowersDestroyed | Cantidad de torres destruidas por el equipo rojo. | int64|
|31 | redTotalGold | Cantidad total de oro obtenida por el equipo rojo en los primeros 10 minutos del juego. | int64|
|32 | redAvgLevel | Nivel promedio de los campeones del equipo rojo en los primeros 10 minutos del juego. | float64|
|33 | redTotalExperience | Cantidad total de experiencia obtenida por el equipo rojo en los primeros 10 minutos del juego. | int64|
|34 | redTotalMinionsKilled | Cantidad total de minions asesinados por el equipo rojo en los primeros 10 minutos del juego. | int64|
|35 | redTotalJungleMinionsKilled | Cantidad total de minions de la jungla asesinados por el equipo rojo en los primeros 10 minutos del juego. | int64|
|36 | redGoldDiff | Diferencia de oro entre el equipo rojo y el equipo azul en los primeros 10 minutos del juego. | int64|
|37 | redExperienceDiff | Diferencia de experiencia entre el equipo rojo y el equipo azul en los primeros 10 minutos del juego. | int64|
|38 | redCSPerMin | Promedio de minions asesinados por minuto por el equipo rojo en los primeros 10 minutos del juego. | float64|
|39 | redGoldPerMin | Promedio de oro obtenido por minuto por el equipo rojo en los primeros 10 minutos del juego. | float64|

#### Procesamiento del Dataset:
El dataset original, que contiene información detallada sobre partidas de League of Legends, ha sido sometido a un proceso de procesamiento y sección con el objetivo de facilitar futuras predicciones y análisis. Este procesamiento implica la creación de dos subconjuntos de datos, conocidos como "blueTeam" y "redTeam", con el propósito de analizar y predecir los resultados de las partidas.

#### Blue Team:
El subconjunto "blueTeam" representa las estadísticas y datos asociados con el equipo azul en cada partida. Esto incluye información sobre las acciones, logros y rendimiento del equipo azul durante los primeros 10 minutos del juego. Las estadísticas como asesinatos, muertes, oro, experiencia, eliminación de monstruos de élite y muchos otros factores que pueden influir en el resultado del juego se recopilan específicamente para el equipo azul.

[data\procesed\blueTeam.csv](data\procesed\blueTeam.csv)

#### Red Team:
El subconjunto "redTeam", por otro lado, se enfoca en las mismas estadísticas pero para el equipo rojo en cada partida. Esto permite un análisis comparativo entre el equipo azul y el equipo rojo, lo que es fundamental en League of Legends, donde los equipos compiten en un formato de enfrentamiento directo.

[data\procesed\redTeam.csv](data\procesed\redTeam.csv)

Este procesamiento y división del dataset en dos equipos permite a los analistas y científicos de datos realizar un análisis más detallado de las partidas y también preparar datos para la construcción de modelos de aprendizaje automático. Al tener dos subconjuntos separados para cada equipo, es posible evaluar qué factores tienen un impacto significativo en el resultado de las partidas y cómo se comparan los dos equipos en términos de estadísticas y rendimiento.