# Modelo Random Forest
Esta sección aborda los resultados de la construcción de modelos Random Forest utilizando conjuntos de características y estrategias establecidas según el análisis obtenido en Features Engineering ( [Notebook](/notebooks/005_Features.ipynb) ).

## Desempeño por Conjunto de Features
Los modelos Random Forest fueron entrenados sobre varios conjuntos de features, y se evaluó su rendimiento en términos de máxima precisión (Max Accuracy) alcanzada en cada conjunto. A continuación, se presentan los resultados en la siguiente tabla:

| Modelo | Features Set | Max Accuracy | Curva ROC (AUC) |
|---|---|---|---|
| Modelo 1 | Visión | **58.90%** | 0.51 |
| Modelo 2 | Rendimiento en Combate | **71.66%** | 0.75 |
| Modelo 3 | Desarrollo y Experiencia | **63.87%** | 0.68 |
| Modelo 4 | Combate Temprano | **69.48%** | 0.57 |
| Modelo 5 | Económicas | **71.71%** | 0.73 |
| Modelo 6 | Desempeño en Dragones y Heralds | **72.27%** | 0.76 |

## Evaluación del Rendimiento
Se llevó a cabo una evaluación del rendimiento mediante la construcción de matrices de confusión para cada modelo. Estas matrices se visualizan en el siguiente gráfico de radar, superponiendo los resultados obtenidos para cada modelo.

![grafico_mejora](/static/img/rf_Matrices_confusión.png)

### Tabla de matriz de confusión

| Modelo | FN | FP | TN |TP |
|---|---|---|---|---|
| Modelo 1 | 4069 | 419 | 4511 | 880 |
| Modelo 2 | 1377 | 1357 | 3573 | 3572 |
| Modelo 3 | 242 | 4299 | 631 | 4707 |
| Modelo 4 | 142 | 4305 | 625 | 4807 |
| Modelo 5 | 1385 | 1353 | 3577 | 3564 |
| Modelo 6 | 1385 | 1354 | 3576 | 3564 |

Estos resultados proporcionan una visión detallada del rendimiento de cada modelo en términos de falsos negativos (FN), falsos positivos (FP), verdaderos negativos (TN) y verdaderos positivos (TP). Se observan variaciones notables en los patrones de error para cada modelo y conjunto de características.

## Consideraciones Finales
El análisis indica que el Modelo 6, con el conjunto de características "Desempeño en Dragones y Heralds", obtuvo la mayor precisión. Sin embargo, la evaluación del rendimiento a través de matrices de confusión proporciona información detallada sobre los falsos positivos, falsos negativos, verdaderos positivos y verdaderos negativos para cada modelo, lo que puede ser crucial dependiendo de los objetivos específicos del modelo y la aplicación.