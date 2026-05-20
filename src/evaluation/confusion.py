# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: evaluation
# modulo: confusion.py
# Funcionalidad: 
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
import pandas as pd

from sklearn.metrics import confusion_matrix

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# GENERAR MATRIZ DE CONFUSION
# -------------------------------------------------------------------------

def generar_matriz_confusion(y_true, y_pred):
    """
    Genera matriz de confusion.
    
    Parameters
    ----------
    y_true : array-like
        Valores reales.
    
    y_pred : array-like
        Predicciones realizadas.
    
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
# MATRIZ COMO DATAFRAME
# -------------------------------------------------------------------------

def matriz_confusion_dataframe(y_true, y_pred):
    """
    Convierte matriz de confusion en DataFrame.
    
    Parameters
    ----------
    y_true : array-like
    
    y_pred : array-like
    
    Returns
    -------
    pandas.DataFrame
    """

    matriz = generar_matriz_confusion(
        y_true,
        y_pred
    )

    df_matriz = pd.DataFrame(
        matriz,
        index=[
            "Real_No_Abandono",
            "Real_Abandono"
        ],
        columns=[
            "Pred_No_Abandono",
            "Pred_Abandono"
        ]
    )

    return df_matriz


# -------------------------------------------------------------------------
# EXTRAER COMPONENTES MATRIZ
# -------------------------------------------------------------------------

def obtener_componentes_matriz(y_true, y_pred):
    """
    Extrae TN, FP, FN, TP.
    
    Returns
    -------
    dict
    """

    matriz = generar_matriz_confusion(
        y_true,
        y_pred
    )

    tn, fp, fn, tp = matriz.ravel()

    return {
        "true_negatives": int(tn),
        "false_positives": int(fp),
        "false_negatives": int(fn),
        "true_positives": int(tp)
    }


# -------------------------------------------------------------------------
# ANALISIS INSTITUCIONAL
# -------------------------------------------------------------------------

def analizar_resultados_confusion(y_true, y_pred):
    """
    Genera interpretacion institucional
    de la matriz de confusion.
    
    Returns
    -------
    dict
    """

    componentes = obtener_componentes_matriz(
        y_true,
        y_pred
    )

    tn = componentes["true_negatives"]
    fp = componentes["false_positives"]
    fn = componentes["false_negatives"]
    tp = componentes["true_positives"]

    analisis = {

        "estudiantes_estables_correctos": tn,

        "abandono_detectado_correctamente": tp,

        "falsas_alertas": fp,

        "abandono_no_detectado": fn
    }

    return analisis


# -------------------------------------------------------------------------
# MOSTRAR MATRIZ EN CONSOLA
# -------------------------------------------------------------------------

def mostrar_matriz_confusion(y_true, y_pred):
    """
    Imprime matriz de confusion.
    """

    df_matriz = matriz_confusion_dataframe(
        y_true,
        y_pred
    )

    print("\n" + "=" * 60)
    print("MATRIZ DE CONFUSION")
    print("=" * 60)

    print(df_matriz)


# -------------------------------------------------------------------------
# MOSTRAR ANALISIS INSTITUCIONAL
# -------------------------------------------------------------------------

def mostrar_analisis_confusion(y_true, y_pred):
    """
    Imprime interpretacion institucional.
    """

    analisis = analizar_resultados_confusion(
        y_true,
        y_pred
    )

    print("\n" + "=" * 60)
    print("ANALISIS INSTITUCIONAL")
    print("=" * 60)

    print(
        f"Estudiantes estables correctamente clasificados: "
        f"{analisis['estudiantes_estables_correctos']}"
    )

    print(
        f"Casos de abandono correctamente detectados: "
        f"{analisis['abandono_detectado_correctamente']}"
    )

    print(
        f"Falsas alertas generadas: "
        f"{analisis['falsas_alertas']}"
    )

    print(
        f"Casos de abandono NO detectados: "
        f"{analisis['abandono_no_detectado']}"
    )


# -------------------------------------------------------------------------
# PIPELINE COMPLETO MATRIZ CONFUSION
# -------------------------------------------------------------------------

def ejecutar_analisis_confusion(y_true, y_pred):
    """
    Ejecuta flujo completo de matriz
    de confusion.
    
    Returns
    -------
    dict
    """

    matriz = generar_matriz_confusion(
        y_true,
        y_pred
    )

    componentes = obtener_componentes_matriz(
        y_true,
        y_pred
    )

    analisis = analizar_resultados_confusion(
        y_true,
        y_pred
    )

    mostrar_matriz_confusion(
        y_true,
        y_pred
    )

    mostrar_analisis_confusion(
        y_true,
        y_pred
    )

    return {
        "matriz_confusion": matriz,
        "componentes": componentes,
        "analisis": analisis
    }