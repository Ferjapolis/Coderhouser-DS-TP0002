
# ML para el Éxito en el Mundo de League of Legends

## Índice
   1. ¿Qué es League of Legends?
   2. Objetivos del análisis
   3. Fuente de datos
   4. Implicaciones de los hallazgos
   5. Resumen de los resultados

## ¿Qué es League of Legends? 
Antes de adentrarnos en nuestra propuesta, permítanme    ofrecerles un contexto sobre League of Legends. Este videojuego, desarrollado por Riot Games, ha revolucionado el mundo de los deportes electrónicos. League of Legends es un juego en línea de estrategia y acción, que reúne a jugadores de todo el mundo en partidas competitivas. Con millones de jugadores y espectadores, League of Legends se ha convertido en un fenómeno global.

![mapa](https://www.pinnacle.com/Cms_Data/Contents/Guest/Media/esports2017/Article-Images/LoL/2019/2019-How-to-improve-your-lol-predictions/Esports-Hero-Esports-How-to-improve-your-LoL-predictions.jpg)

El juego se basa en la estrategia y la coordinación en equipo, ya que cada campeón tiene roles y habilidades específicas que deben utilizarse de manera efectiva. Los jugadores ganan oro y experiencia a lo largo de la partida, lo que les permite mejorar sus campeones y comprar objetos para fortalecer sus habilidades.

Sin duda, la liga de League of Legends ha experimentado un notable crecimiento en los últimos años. Para dar una idea más precisa, veamos algunos datos concretos. En 2010, el juego tenía aproximadamente 5 millones de usuarios, y hoy en día, en 2021, ese número ha superado los 155 millones. Esto representa un crecimiento impresionante, con un incremento de más del 3100% en la base de usuarios en tan solo una década. Este crecimiento vertiginoso no se limita solo a la comunidad de jugadores, ya que los espectadores también han aumentado sustancialmente.

Los torneos de alto nivel, como el Campeonato Mundial de League of Legends, han sido testigos de un incremento constante en la audiencia. En 2010, apenas 1 millón de usuarios se conectaban diariamente para participar en partidas, y en 2021, esta cifra ha superado los 31 millones. Esto equivale a un aumento de más del 3000% en la cantidad de usuarios conectados diariamente durante este período. La creciente base de jugadores y espectadores ha convertido a League of Legends en un fenómeno global, atrayendo a fanáticos de todas partes del mundo.

### Crecimiento de Usuarios de League of Legends
Además , a medida que la escena competitiva ha crecido, también se ha vuelto más profesional. Grandes organizaciones y patrocinadores respaldan a equipos y jugadores, lo que demuestra la inversión y el compromiso que el juego ha generado en la industria de los deportes electrónicos. Este emocionante crecimiento y la perspectiva de seguir atrayendo a nuevos jugadores y fanáticos hacen de League of Legends un mercado prometedor y dinámico para cualquier inversor en busca de oportunidades en los deportes electrónicos

El crecimiento fenomenal de League of Legends no solo se ha manifestado en números, sino también en la dedicación apasionada de su comunidad de jugadores. Como hemos observado, millones de usuarios se conectan diariamente, y esta base activa de jugadores ha demostrado un compromiso inquebrantable con el juego. Participan activamente en foros de discusión, utilizan redes sociales para compartir estrategias y experiencias, y se sumergen en plataformas de transmisión en vivo para aprender y entretenerse. Además, la formación de clanes y equipos amateur ha impulsado la competencia a niveles locales y regionales, creando una vibrante escena competitiva en todo el mundo. Esta comunidad apasionada y comprometida es un testimonio de la influencia duradera de League of Legends en el mundo de los deportes electrónicos.


---

### Objetivos del análisis:
El presente informe tiene como objetivo analizar un conjunto de datos de partidas clasificatorias Diamante de League of Legends (LoL) en los primeros 10 minutos, con el propósito de proporcionar información valiosa para un nuevo equipo que busca optimizar su rendimiento y estrategias. El dataset contiene estadísticas de aproximadamente 10,000 partidas con jugadores de niveles similares. El valor objetivo a predecir es si el equipo azul ganó la partida (valor 1) o no (valor 0).

Referncias:
- https://www.redbull.com/ar-es/lol-el-sistema-de-ranking-de-league-of-legends-explicado
- https://tips.gg/es/lol/teams/

---

### EDA ([Notebook](notebooks/001_EDA.ipynb))

---
### Insight encontrados ([Notebook](notebooks/002_Insight.ipynb))

- **Control temprano del mapa**: El hecho de que equipos que colocan más "Warding totems", obtienen más asesinatos y torres tengan una mayor probabilidad de victoria resalta la importancia de la visión del mapa y las estrategias de emboscada para obtener ventajas iniciales.
![insight_001](static/img/Insight_001.png)


- **Importancia de los objetivos neutrales**: La correlación entre asegurar más dragones y Herald en los primeros 10 minutos y una mayor tasa de victoria enfatiza la necesidad de coordinar y priorizar la captura de objetivos neutrales para obtener beneficios significativos para todo el equipo.
![insight_001](static/img/Insight_002.png)

- **Desempeño individual y ventaja económica**: El número de asistencias y las diferencias de oro y experiencia entre los equipos como indicadores cruciales de la probabilidad de victoria destacan la importancia del desempeño individual y la ventaja económica para el éxito del equipo.
![insight_001](static/img/Insight_003.png)

- **Nivel promedio del equipo**: La correlación entre un mayor nivel promedio del equipo azul y una mayor probabilidad de ganar subraya la importancia de mantener un ritmo de crecimiento constante y eficiente durante la fase temprana del juego.ntener un ritmo de crecimiento constante y eficiente durante la fase temprana del juego.
![insight_001](static/img/Insight_004.png)

- **Diferencias de oro y experiencia determinantes**: La fuerte vinculación entre las diferencias de oro y experiencia entre los equipos en los primeros 10 minutos y los resultados resalta la relevancia de obtener una ventaja significativa en estos aspectos.
![insight_001](static/img/Insight_005.png)

---

### Hipotesis ([Notebook](notebooks/003_Outsight.ipynb))
Estas hipótesis proporcionan una base sólida para realizar pruebas y análisis más detallados sobre el dataset de League of Legends. Al evaluar cada una de estas hipótesis y validarlas con datos, el equipo podrá obtener una mejor comprensión de los factores que realmente influyen en el rendimiento y la probabilidad de victoria en el juego.

- **Hipótesis 1**: Relación entre asesinatos y tasa de victoria
El número de asesinatos conseguidos por un equipo en los primeros 10 minutos se correlacionará positivamente con su tasa de victoria. Cuanto mayor sea la cantidad de asesinatos, más alta será la probabilidad de ganar.
![insight_001](static/img/Hypothesis_001.png)


- **Hipótesis 2**: Impacto de objetivos neutrales en la victoria
Equipos que aseguran más dragones y Herald durante los primeros 10 minutos tendrán una mayor probabilidad de ganar la partida, ya que estos objetivos proporcionan beneficios significativos para todo el equipo.

  ![insight_002A](static/img/Hypothesis_002A.png)
  La relación entre la captura del Dragon y la cantidad total de experiencia y oro en el juego:
  Para el equipo que captura el Dragon (Dragon si [D1]):
  - La cantidad promedio de experiencia total obtenida es de aproximadamente 18,235.37.
  - La cantidad promedio de oro total obtenida es de aproximadamente 16,841.97.

  Para el equipo que no captura el Dragon (Dragon no [D0]):
  - La cantidad promedio de experiencia total obtenida es ligeramente menor, con un valor promedio de aproximadamente 17,761.14.
  - La cantidad promedio de oro total obtenida también es menor, con un valor promedio de aproximadamente 16,277.49.

   ![insight_002B](static/img/Hypothesis_002B.png)
   Para el equipo que captura el Herald (Herald si [H1]):

  - La cantidad promedio de experiencia total obtenida es de aproximadamente 18,328.27.
  - La cantidad promedio de oro total obtenida es de aproximadamente 17,000.59.

  Para el equipo que no captura el Herald (Herald no [H0]):
  - La cantidad promedio de experiencia total obtenida es ligeramente menor, con un valor promedio de aproximadamente 17,864.16.
  - La cantidad promedio de oro total obtenida también es menor, con un valor promedio de aproximadamente 16,390.00.

   En general, los equipos que capturan tanto el Dragon como el Herald tienden a obtener una mayor cantidad de experiencia y oro en comparación con los equipos que no capturan estos objetivos. La captura de objetivos neutrales (Dragon y Herald) en el juego está relacionada con una ventaja significativa en términos de recursos (experiencia y oro) para el equipo que los asegura. Estos valores son promedios y pueden variar según la estrategia y otros factores del juego.

  podemos resumir la relación entre la captura de Dragones y Herald y la factibilidad de la victoria de la siguiente manera:

  - Cuando un equipo no captura ni Dragon ni Herald, la probabilidad de victoria es del 40.52%.
  - Cuando un equipo captura Dragon pero no Herald, la probabilidad de victoria es del 38.50%.
  - Cuando un equipo no captura Dragon pero captura Herald, la probabilidad de victoria es del 10.43%.
  - Cuando un equipo captura tanto Dragon como Herald, la probabilidad de victoria es del 10.56%.

  ![insight_002C](static/img/Hypothesis_002.png)
  Basándonos en estos datos, podemos observar que la probabilidad de victoria es más alta cuando un equipo captura al menos uno de estos objetivos neutrales (Dragon o Herald) en comparación con cuando no captura ninguno. Esto sugiere que la captura de estos objetivos neutrales está relacionada con una mayor factibilidad de la victoria en las partidas de League of Legends. La probabilidad de victoria es especialmente alta cuando se capturan ambos objetivos.


- **Hipótesis 3**: Importancia de la ventaja económica y de experiencia
Equipos que logran una ventaja significativa en oro y experiencia sobre el equipo contrario en los primeros 10 minutos tendrán mayores posibilidades de obtener la victoria.
   ![insight_003](static/img/Hypothesis_003.png)

- **Hipótesis 4**: Contribución individual y tasa de victoria Jugadores que contribuyen con un mayor número de asistencias tendrán un impacto positivo en la tasa de victoria de su equipo en las partidas clasificatorias Diamante.

  ![insight_004](static/img/Hypothesis_004.png)
  los jugadores que contribuyen con un mayor número de asistencias tienen una mayor probabilidad de obtener la victoria en este nivel de juego. Este resultado sugiere que el juego en equipo y la contribución individual son factores importantes para el éxito en las partidas de Diamante en League of Legends.

- **Hipótesis 5**: Nivel promedio y probabilidad de victoria Un equipo con un mayor nivel promedio de sus jugadores durante los primeros 10 minutos tendrá una mayor probabilidad de ganar la partida.

  ![insight_005](static/img/Hypothesis_005.png)
  El resultado obtenido de 69.43k de nivel promedio en partidas victoriosas y 67.29k de nivel promedio en partidas derrotadas indica que, en promedio, no hay una gran diferencia en el nivel promedio de los jugadores entre las partidas ganadas y las partidas perdidas.

  Esto sugiere que, al menos en el contexto de las partidas analizadas, el nivel promedio de los jugadores en los primeros 10 minutos no parece ser un factor determinante para la tasa de victoria en League of Legends. La diferencia en el nivel promedio entre partidas ganadas y perdidas es relativamente pequeña, lo que sugiere que otros factores pueden tener un impacto más significativo en el resultado de la partida.