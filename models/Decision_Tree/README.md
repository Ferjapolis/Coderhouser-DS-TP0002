# Modelo Decision Tree
Esta sección aborda los resultados de la construcción de modelos Decision Tree utilizando conjuntos de características y estrategias establecidas según el análisis obtenido en Features Engineering ( [Notebook](/notebooks/005_Features.ipynb) ).

## Desempeño por Conjunto de Features
Los modelos Decision Tree fueron entrenados sobre varios conjuntos de features, y se evaluó su rendimiento en términos de máxima precisión (Max Accuracy) alcanzada en cada conjunto. A continuación, se presentan los resultados en la siguiente tabla:

| Modelo | Features Set | Max Accuracy | Curva ROC (AUC) |
|---|---|---|---|
| Modelo 1 | Visión | **57.34%** | 0.45 |
| Modelo 2 | Rendimiento en Combate | **69.69%** | 0.71 |
| Modelo 3 | Desarrollo y Experiencia | **62.04%** | 0.43 |
| Modelo 4 | Combate Temprano | **67.91%** | 0.55 |
| Modelo 5 | Económicas | **69.38%** | 0.50 |
| Modelo 6 | Desempeño en Dragones y Heralds | **71.00%** | 0.72 |

## Evaluación del Aprendizaje
Se utilizó la función learning_curve para evaluar el proceso de aprendizaje en cada conjunto de características, con el objetivo de determinar la disposición óptima de los datos y mejorar el rendimiento de los modelos. Esta herramienta proporcionó información valiosa sobre cómo el tamaño del conjunto de entrenamiento afecta el rendimiento del modelo, permitiendo ajustar estratégicamente la cantidad de datos utilizados para mejorar la capacidad de generalización de los modelos a través de diferentes conjuntos de características.

![learning_curve](/static/img/df_learning_curve.png)

## Evaluación del Rendimiento
Se llevó a cabo una evaluación del rendimiento mediante la construcción de matrices de confusión para cada modelo. Estas matrices se visualizan en el siguiente gráfico de radar, superponiendo los resultados obtenidos para cada modelo.

![grafico_mejora](/static/img/df_Matrices_confusión.png)

### Tabla de matriz de confusión

| Modelo | FN | FP | TN |TP |
|---|---|---|---|---|
| Modelo 1 | 4551 | 194 | 4736 | 398 |
| Modelo 2 | 1381 | 1367 | 3563 | 3568 |
| Modelo 3 | 3268 | 2318 | 2612 | 1681 |
| Modelo 4 | 215 | 4208 | 722 | 4734 |
| Modelo 5 | 3 | 4929 | 1 | 4946 |
| Modelo 6 | 1234 | 1480 | 3450 | 3715 |

Estos resultados proporcionan una visión detallada del rendimiento de cada modelo en términos de falsos negativos (FN), falsos positivos (FP), verdaderos negativos (TN) y verdaderos positivos (TP). Se observan variaciones notables en los patrones de error para cada modelo y conjunto de características.

![grafico_mejora](/static/img/df_curve_roc.png)

## Consideraciones Finales
Los modelos, entrenados con diversos conjuntos, exhibieron máximas precisiones, destacando el Modelo 6 con "Desempeño en Dragones y Heralds" logrando un 71.00%. La evaluación del rendimiento mediante matrices de confusión reveló variaciones notables en los patrones de error para cada modelo y conjunto de características, proporcionando una visión detallada de su desempeño.
En este caso, parece que el modelo está aprendiendo de manera efectiva incluso con tamaños de entrenamiento más grandes, y no hay señales de un sobreajuste significativo (puntuación de entrenamiento mucho más alta que la de validación cruzada) o subajuste (puntuaciones bajas en general). La convergencia de las puntuaciones sugiere un buen rendimiento general del modelo.