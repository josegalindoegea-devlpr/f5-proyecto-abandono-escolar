# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: evaluation
# modulo: metrics.py
# Funcionalidad: 
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report,
    confusion_matrix
)

import pandas as pd

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# METRICAS PRINCIPALES
# -------------------------------------------------------------------------

def calcular_metricas(y_true, y_pred):
    """
    Calcula metricas principales del modelo.
    
    Parameters
    ----------
    y_true : array-like
        Valores reales.
    
    y_pred : array-like
        Predicciones del modelo.
    
    Returns
    -------
    dict
        Diccionario con metricas calculadas.
    """

    accuracy = accuracy_score(y_true, y_pred)

    precision = precision_score(
        y_true,
        y_pred,
        zero_division=0
    )

    recall = recall_score(
        y_true,
        y_pred,
        zero_division=0
    )

    f1 = f1_score(
        y_true,
        y_pred,
        zero_division=0
    )

    metricas = {
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1_score": round(f1, 4)
    }

    return metricas


# -------------------------------------------------------------------------
# REPORTE DETALLADO
# -------------------------------------------------------------------------

def generar_reporte_clasificacion(y_true, y_pred):
    """
    Genera reporte completo de clasificacion.
    
    Parameters
    ----------
    y_true : array-like
        Valores reales.
    
    y_pred : array-like
        Predicciones del modelo.
    
    Returns
    -------
    str
        Reporte textual sklearn.
    """

    reporte = classification_report(
        y_true,
        y_pred,
        target_names=[
            "Estable",
            "Abandono"
        ],
        zero_division=0
    )

    return reporte


# -------------------------------------------------------------------------
# MATRIZ DE CONFUSION
# -------------------------------------------------------------------------

def obtener_matriz_confusion(y_true, y_pred):
    """
    Genera matriz de confusion.
    
    Parameters
    ----------
    y_true : array-like
        Valores reales.
    
    y_pred : array-like
        Predicciones del modelo.
    
    Returns
    -------
    ndarray
        Matriz de confusion.
    """

    matriz = confusion_matrix(
        y_true,
        y_pred
    )

    return matriz


# -------------------------------------------------------------------------
# DATAFRAME DE METRICAS
# -------------------------------------------------------------------------

def metricas_a_dataframe(metricas):
    """
    Convierte metricas a DataFrame.
    
    Parameters
    ----------
    metricas : dict
    
    Returns
    -------
    pandas.DataFrame
    """

    df_metricas = pd.DataFrame(
        [metricas]
    )

    return df_metricas


# -------------------------------------------------------------------------
# IMPRESION FORMATEADA
# -------------------------------------------------------------------------

def mostrar_metricas(metricas):
    """
    Muestra metricas por consola.
    
    Parameters
    ----------
    metricas : dict
    """

    print("\n" + "=" * 50)
    print("METRICAS DEL MODELO")
    print("=" * 50)

    for nombre, valor in metricas.items():

        print(
            f"{nombre.upper():<15}: {valor:.4f}"
        )


# -------------------------------------------------------------------------
# PIPELINE COMPLETO EVALUACION
# -------------------------------------------------------------------------

def evaluar_modelo(y_true, y_pred):
    """
    Ejecuta evaluacion completa.
    
    Parameters
    ----------
    y_true : array-like
    
    y_pred : array-like
    
    Returns
    -------
    dict
        Resultado completo evaluacion.
    """

    metricas = calcular_metricas(
        y_true,
        y_pred
    )

    reporte = generar_reporte_clasificacion(
        y_true,
        y_pred
    )

    matriz = obtener_matriz_confusion(
        y_true,
        y_pred
    )

    mostrar_metricas(metricas)

    print("\n" + "=" * 50)
    print("REPORTE DE CLASIFICACION")
    print("=" * 50)

    print(reporte)

    return {
        "metricas": metricas,
        "reporte": reporte,
        "matriz_confusion": matriz
    }