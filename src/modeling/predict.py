# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: modeling
# modulo: predict.py
# Funcionalidad: Inferencia y predicciones del modelo ML
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report
)
# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from utils.logger import (
    log_info,
    log_error
)
# -------------------------------------------------------------------------
# PREDICCION BINARIA
# -------------------------------------------------------------------------

def predecir(
    modelo,
    X
):
    """
    Genera predicciones binarias.

    Parameters
    ----------
    modelo : sklearn model

    X : array-like
        Features escaladas.

    Returns
    -------
    numpy.ndarray
        Predicciones binarias.
    """

    log_info(
        "Generando predicciones binarias"
    )

    try:

        y_pred = modelo.predict(X)

        return y_pred

    except Exception as e:

        log_error(
            f"Error en prediccion: {str(e)}"
        )

        raise


# -------------------------------------------------------------------------
# PREDICCION PROBABILIDADES
# -------------------------------------------------------------------------

def predecir_probabilidades(
    modelo,
    X
):
    """
    Genera probabilidades de abandono.

    Parameters
    ----------
    modelo : sklearn model

    X : array-like

    Returns
    -------
    numpy.ndarray
        Probabilidad clase positiva.
    """

    log_info(
        "Calculando probabilidades"
    )

    try:

        probabilidades = (
            modelo.predict_proba(X)[:, 1]
        )

        return probabilidades

    except Exception as e:

        log_error(
            f"Error probabilidades: {str(e)}"
        )

        raise


# -------------------------------------------------------------------------
# CLASIFICACION RIESGO
# -------------------------------------------------------------------------

def clasificar_riesgo(
    probabilidades
):
    """
    Clasifica estudiantes por nivel riesgo.

    Parameters
    ----------
    probabilidades : array-like

    Returns
    -------
    list
    """

    categorias = []

    for prob in probabilidades:

        if prob < 0.30:

            categorias.append(
                "RIESGO_BAJO"
            )

        elif prob < 0.70:

            categorias.append(
                "RIESGO_MEDIO"
            )

        else:

            categorias.append(
                "RIESGO_ALTO"
            )

    return categorias


# -------------------------------------------------------------------------
# GENERAR DATAFRAME RESULTADOS
# -------------------------------------------------------------------------

def generar_dataframe_predicciones(
    df_original,
    y_pred,
    y_prob
):
    """
    Construye DataFrame final de resultados.

    Parameters
    ----------
    df_original : pandas.DataFrame

    y_pred : array-like

    y_prob : array-like

    Returns
    -------
    pandas.DataFrame
    """

    log_info(
        "Construyendo dataframe resultados"
    )

    df_resultados = df_original.copy()

    df_resultados[
        "prediccion_abandono"
    ] = y_pred

    df_resultados[
        "probabilidad_abandono"
    ] = np.round(
        y_prob,
        4
    )

    df_resultados[
        "nivel_riesgo"
    ] = clasificar_riesgo(
        y_prob
    )

    return df_resultados


# -------------------------------------------------------------------------
# OBTENER ESTUDIANTES RIESGO ALTO
# -------------------------------------------------------------------------

def obtener_estudiantes_riesgo_alto(
    df_resultados,
    umbral=0.70
):
    """
    Filtra estudiantes con riesgo alto.

    Parameters
    ----------
    df_resultados : pandas.DataFrame

    umbral : float

    Returns
    -------
    pandas.DataFrame
    """

    estudiantes_riesgo = df_resultados[
        df_resultados[
            "probabilidad_abandono"
        ] >= umbral
    ]

    return estudiantes_riesgo


# -------------------------------------------------------------------------
# RESUMEN PREDICCIONES
# -------------------------------------------------------------------------

def resumen_predicciones(
    df_resultados
):
    """
    Genera resumen ejecutivo.

    Parameters
    ----------
    df_resultados : pandas.DataFrame
    """

    total = len(df_resultados)

    abandono = (
        df_resultados[
            "prediccion_abandono"
        ].sum()
    )

    riesgo_alto = len(

        df_resultados[
            df_resultados[
                "nivel_riesgo"
            ] == "RIESGO_ALTO"
        ]
    )

    print("\n" + "=" * 60)
    print("RESUMEN PREDICCIONES")
    print("=" * 60)

    print(
        f"Total estudiantes: {total}"
    )

    print(
        f"Predicciones abandono: {abandono}"
    )

    print(
        f"Estudiantes riesgo alto: {riesgo_alto}"
    )


# -------------------------------------------------------------------------
# PIPELINE COMPLETO PREDICCION
# -------------------------------------------------------------------------

def ejecutar_prediccion(
    modelo,
    X,
    df_original
):
    """
    Ejecuta flujo completo inferencia.

    Parameters
    ----------
    modelo : sklearn model

    X : array-like

    df_original : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    log_info(
        "Iniciando pipeline prediccion"
    )

    y_pred = predecir(
        modelo,
        X
    )

    y_prob = predecir_probabilidades(
        modelo,
        X
    )

    df_resultados = (
        generar_dataframe_predicciones(
            df_original,
            y_pred,
            y_prob
        )
    )

    resumen_predicciones(
        df_resultados
    )

    log_info(
        "Pipeline prediccion finalizado"
    )

    return df_resultados