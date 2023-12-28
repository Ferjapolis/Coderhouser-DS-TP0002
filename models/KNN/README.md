# Modelo KNN
Esta sección aborda los resultados de la construcción de modelos KNN utilizando conjuntos de características y estrategias establecidas según el análisis obtenido en Features Engineering ( [Notebook](/notebooks/005_Features.ipynb) ).

## Desempeño por Conjunto de Features
Los modelos KNN fueron entrenados sobre varios conjuntos de features, y se evaluó su rendimiento en términos de máxima precisión (Max Accuracy) alcanzada en cada conjunto. A continuación, se presentan los resultados en la siguiente tabla:

| Modelo | Features Set | Max Accuracy |
|---|---|---|
| Modelo 1 | Visión | **57.99%** |
| Modelo 2 | Rendimiento en Combate | **71.20%** |
| Modelo 3 | Desarrollo y Experiencia | **65.18%** |
| Modelo 4 | Combate Temprano | **68.67%** |
| Modelo 5 | Económicas | **70.44%** |
| Modelo 6 | Desempeño en Dragones y Heralds | **71.45%** |

## Optimización del Modelo
El siguiente gráfico ilustra el proceso de optimización de cada modelo con respecto a los diferentes conjuntos de features.

![grafico_mejora](/static/img/knn_features_comparations.png)
![grafico_mejora](/static/img/knn_legends.png)

## Evaluación del Rendimiento
Se llevó a cabo una evaluación del rendimiento mediante la construcción de matrices de confusión para cada modelo. Estas matrices se visualizan en el siguiente gráfico de radar, superponiendo los resultados obtenidos para cada modelo.

![grafico_mejora](/static/img/knn_Matrices_confusión.png)

### Tabla de matriz de confusión

| Modelo | FN | FP | TN |TP |
|---|---|---|---|---|
| Modelo 1 | 4928 | 20 | 4910 | 21 |
| Modelo 2 | 715 | 2142 | 2788 | 4234 |
| Modelo 3 | 0 | 4930 | 0 | 4949 |
| Modelo 4 | 949 | 3487 | 1443 | 4000 |
| Modelo 5 | 465 | 2635 | 2295 | 4484 |
| Modelo 6 | 1332 | 1366 | 3564 | 3617 |

Estos resultados proporcionan una visión detallada del rendimiento de cada modelo en términos de falsos negativos (FN), falsos positivos (FP), verdaderos negativos (TN) y verdaderos positivos (TP). Se observan variaciones notables en los patrones de error para cada modelo y conjunto de características.

## Consideraciones Finales
Si bien el Modelo 3 destaca como el mejor en términos de precisión y patrones de error, se seguira evaluando cuidadosamente el equilibrio entre falsos positivos y falsos negativos según los requisitos específicos del contexto de aplicación. La elección del mejor modelo debera basarse en consideraciones prácticas y las implicaciones de los diferentes tipos de errores en la aplicación real.