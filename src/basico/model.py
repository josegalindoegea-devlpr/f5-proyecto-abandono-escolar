# ==========================================
# model.py
# Entrenamiento y evaluación del modelo
# ==========================================

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report
)


def entrenar_modelo(X_train, y_train):
    """
    Entrena el modelo Logistic Regression.
    """

    modelo = LogisticRegression()

    modelo.fit(X_train, y_train)

    return modelo


def realizar_predicciones(modelo, X_test):
    """
    Genera predicciones.
    """

    y_pred = modelo.predict(X_test)

    return y_pred


def evaluar_modelo(y_test, y_pred):
    """
    Calcula métricas principales.
    """

    accuracy = accuracy_score(y_test, y_pred)

    reporte = classification_report(y_test, y_pred)

    return accuracy, reporte
