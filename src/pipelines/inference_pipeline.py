# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: pipelines
# modulo: inference_pipeline.py
# Funcionalidad: Pipeline principal de inferencia
# Version: 2.0
# ==========================================
# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
import pandas as pd
# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from ingestion.loader import cargar_dataset

from preprocessing.pipeline import preparar_datos

from modeling.predict import (
    predecir,
    predecir_probabilidades
)

from evaluation.metrics import (
    calcular_metricas,
    mostrar_metricas
)

from evaluation.confusion import (
    ejecutar_analisis_confusion
)

from visualization.plots import (
    graficar_matriz_confusion
)

from visualization.dashboards import (
    generar_dashboard_principal
)

from persistence.model_registry import (
    cargar_modelo,
    cargar_scaler
)

from config.settings import (
    DATASET_PATH,
    TARGET
)


# -------------------------------------------------------------------------
# PIPELINE INFERENCIA
# -------------------------------------------------------------------------

def ejecutar_pipeline_inferencia():
    """
    Ejecuta pipeline completo de inferencia.

    Flujo:
    1. Carga dataset
    2. Preparacion features
    3. Carga modelo entrenado
    4. Escalado
    5. Predicciones
    6. Evaluacion
    7. Visualizacion

    Returns
    -------
    dict
        Resultado completo inferencia.
    """

    print("\n" + "=" * 60)
    print("PIPELINE INFERENCIA - ABANDONO ESCOLAR")
    print("=" * 60)

    # -------------------------------------------------------------
    # 1. CARGA DATASET
    # -------------------------------------------------------------

    print("\n[1/7] Cargando dataset...")

    df = cargar_dataset(
        DATASET_PATH
    )

    print(
        f"Dataset cargado correctamente: "
        f"{df.shape}"
    )

    # -------------------------------------------------------------
    # 2. PREPROCESSING
    # -------------------------------------------------------------

    print("\n[2/7] Preparando datos...")

    X, y, df = preparar_datos(df)

    print(
        f"Features preparadas: "
        f"{X.shape}"
    )

    # -------------------------------------------------------------
    # 3. CARGA MODELO
    # -------------------------------------------------------------

    print("\n[3/7] Cargando modelo...")

    modelo = cargar_modelo()

    scaler = cargar_scaler()

    print("Modelo cargado correctamente")

    # -------------------------------------------------------------
    # 4. ESCALADO
    # -------------------------------------------------------------

    print("\n[4/7] Escalando features...")

    X_scaled = scaler.transform(X)

    # -------------------------------------------------------------
    # 5. PREDICCIONES
    # -------------------------------------------------------------

    print("\n[5/7] Generando predicciones...")

    y_pred = predecir(
        modelo,
        X_scaled
    )

    y_prob = predecir_probabilidades(
        modelo,
        X_scaled
    )

    print("Predicciones generadas")

    # -------------------------------------------------------------
    # 6. METRICAS
    # -------------------------------------------------------------

    print("\n[6/7] Evaluando resultados...")

    metricas = calcular_metricas(
        y,
        y_pred
    )

    mostrar_metricas(metricas)

    confusion_results = (
        ejecutar_analisis_confusion(
            y,
            y_pred
        )
    )

    # -------------------------------------------------------------
    # 7. VISUALIZACIONES
    # -------------------------------------------------------------

    print("\n[7/7] Generando visualizaciones...")

    graficar_matriz_confusion(
        y,
        y_pred
    )

    generar_dashboard_principal(
        df=df,
        y_true=y,
        y_pred=y_pred,
        metricas=metricas
    )

    # -------------------------------------------------------------
    # RESULTADOS FINALES
    # -------------------------------------------------------------

    df_resultados = df.copy()

    df_resultados["prediccion"] = y_pred

    df_resultados["probabilidad_abandono"] = y_prob

    print("\n" + "=" * 60)
    print("PIPELINE FINALIZADO")
    print("=" * 60)

    return {

        "modelo": modelo,

        "metricas": metricas,

        "predicciones": y_pred,

        "probabilidades": y_prob,

        "matriz_confusion": (
            confusion_results["matriz_confusion"]
        ),

        "resultados": df_resultados
    }


# -------------------------------------------------------------------------
# PIPELINE INFERENCIA SIMPLE
# -------------------------------------------------------------------------

def ejecutar_inferencia_simple(
    modelo,
    scaler,
    df
):
    """
    Ejecuta inferencia simple sobre un DataFrame.

    Parameters
    ----------
    modelo : sklearn model

    scaler : StandardScaler

    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    X, _, df = preparar_datos(df)

    X_scaled = scaler.transform(X)

    predicciones = predecir(
        modelo,
        X_scaled
    )

    probabilidades = (
        predecir_probabilidades(
            modelo,
            X_scaled
        )
    )

    df_resultado = df.copy()

    df_resultado["prediccion"] = predicciones

    df_resultado[
        "probabilidad_abandono"
    ] = probabilidades

    return df_resultado

# -------------------------------------------------------------------------
# EJEMPLO USO
# -------------------------------------------------------------------------

if __name__ == "__main__":

    print(
        "\nPipeline de inferencia listo"
    )