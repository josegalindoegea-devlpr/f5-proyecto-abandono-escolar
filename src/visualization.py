# ==========================================
# visualization.py
# Visualización de resultados
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix


def graficar_matriz_confusion(y_test, y_pred):
    """
    Genera matriz de confusión.
    """

    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 4))

    sns.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues',
        xticklabels=['No abandona', 'Abandona'],
        yticklabels=['No abandona', 'Abandona']
    )

    plt.xlabel("Predicción")

    plt.ylabel("Valor Real")

    plt.title("Matriz de Confusión")

    plt.show()


def graficar_importancia_variables(modelo, columnas):
    """
    Visualiza importancia de variables.
    """

    coeficientes = modelo.coef_[0]

    plt.figure(figsize=(8, 5))

    sns.barplot(
        x=coeficientes,
        y=columnas
    )

    plt.title("Importancia de Variables")

    plt.xlabel("Coeficiente")

    plt.ylabel("Variables")

    plt.show()

