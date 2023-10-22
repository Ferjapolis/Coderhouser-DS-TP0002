# Importacion de sklearn para el modelo KNN
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from plyer import notification
import time


"""
La función model_train_test está diseñada para simplificar el proceso de entrenamiento, 
evaluación y visualización de resultados de un modelo de aprendizaje automático. 
A continuación, se proporciona una descripción detallada de cada parte de la función:

Argumentos:
    - model: El modelo de aprendizaje automático que se entrenará y evaluará.
    - xts: Conjunto de entrenamiento con las características estandarizadas.
    - xTest: Conjunto de prueba con las características estandarizadas.
    - yTrain: Etiquetas de entrenamiento.
    - yTest: Etiquetas de prueba.
"""
def model_train_test(model, xts, xTest, yTrain, yTest):
    model.fit(xts, yTrain)
    y_predict = model.predict(xTest)
    print(classification_report(yTest, y_predict))
    ConfusionMatrixDisplay.from_estimator(model, xTest, yTest)

def notificar(titulo, mensaje, tiempo):
    while True:
        time.sleep(tiempo)
        notification.notify(
            title = titulo,
            message = mensaje,
            timeout = 10,
        )