# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: pipelines
# modulo: evaluation_pipeline.py
# Funcionalidad: Pipeline completo de evaluacion ML
# Version: 2.0
# ==========================================
# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
import pandas as pd
# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from evaluation.metrics import (
    calcular_metricas_modelo,
    mostrar_metricas
)

from evaluation.confusion import (
    generar_matriz_confusion,
    mostrar_matriz_confusion
)

from visualization.dashboards import (
    visualizar_distribucion_predicciones,
    visualizar_probabilidades
)

from modeling.predict import (
    predecir,
    predecir_probabilidades
)

from utils.logger import (
    log_inicio_pipeline,
    log_fin_pipeline,
    log_metricas,
    log_error,
    log_info
)


# -------------------------------------------------------------------------
# PIPELINE EVALUACION COMPLETO
# -------------------------------------------------------------------------

def ejecutar_evaluation_pipeline(
    modelo,
    X_test,
    y_test,
    mostrar_graficas=True
):
    """
    Ejecuta pipeline completo evaluación modelo.

    Flujo:
    -------
    1. Predicciones
    2. Probabilidades
    3. Métricas
    4. Matriz confusión
    5. Dashboards
    6. Logging

    Parameters
    ----------
    modelo : sklearn model

    X_test : array-like

    y_test : array-like

    mostrar_graficas : bool

    Returns
    -------
    dict
    """

    try:

        # -------------------------------------------------------------
        # INICIO PIPELINE
        # -------------------------------------------------------------

        log_inicio_pipeline(
            "evaluation_pipeline"
        )

        # -------------------------------------------------------------
        # PREDICCIONES
        # -------------------------------------------------------------

        log_info(
            "Generando predicciones"
        )

        y_pred = predecir(
            modelo,
            X_test
        )

        # -------------------------------------------------------------
        # PROBABILIDADES
        # -------------------------------------------------------------

        log_info(
            "Calculando probabilidades"
        )

        y_prob = predecir_probabilidades(
            modelo,
            X_test
        )

        # -------------------------------------------------------------
        # METRICAS
        # -------------------------------------------------------------

        log_info(
            "Calculando metricas"
        )

        metricas = (
            calcular_metricas_modelo(
                y_test,
                y_pred
            )
        )

        mostrar_metricas(
            metricas
        )

        log_metricas(
            metricas
        )

        # -------------------------------------------------------------
        # MATRIZ CONFUSION
        # -------------------------------------------------------------

        log_info(
            "Generando matriz confusion"
        )

        matriz = generar_matriz_confusion(
            y_test,
            y_pred
        )

        mostrar_matriz_confusion(
            matriz
        )

        # -------------------------------------------------------------
        # VISUALIZACIONES
        # -------------------------------------------------------------

        if mostrar_graficas:

            log_info(
                "Generando dashboards"
            )

            visualizar_distribucion_predicciones(
                y_pred
            )

            visualizar_probabilidades(
                y_prob
            )

        # -------------------------------------------------------------
        # FIN PIPELINE
        # -------------------------------------------------------------

        log_fin_pipeline(
            "evaluation_pipeline"
        )

        # -------------------------------------------------------------
        # RESULTADOS
        # -------------------------------------------------------------

        resultados = {

            "metricas": metricas,

            "matriz_confusion": matriz,

            "predicciones": y_pred,

            "probabilidades": y_prob
        }

        return resultados

    except Exception as e:

        log_error(
            f"Error evaluation pipeline: {str(e)}"
        )

        raise


# -------------------------------------------------------------------------
# RESUMEN EJECUTIVO
# -------------------------------------------------------------------------

def mostrar_resumen_evaluacion(
    resultados
):
    """
    Muestra resumen ejecutivo evaluación.

    Parameters
    ----------
    resultados : dict
    """

    metricas = resultados[
        "metricas"
    ]

    print("\n" + "=" * 60)
    print("RESUMEN EJECUTIVO EVALUACION")
    print("=" * 60)

    print(
        f"Accuracy : {metricas['accuracy']:.4f}"
    )

    print(
        f"Precision: {metricas['precision']:.4f}"
    )

    print(
        f"Recall   : {metricas['recall']:.4f}"
    )

    print(
        f"F1 Score : {metricas['f1_score']:.4f}"
    )

    print("=" * 60)

# -------------------------------------------------------------------------
# EJEMPLO USO
# -------------------------------------------------------------------------

if __name__ == "__main__":

    print(
        "\nPipeline de evaluación listo"
    )