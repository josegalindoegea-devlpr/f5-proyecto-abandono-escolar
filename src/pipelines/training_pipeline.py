# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: pipelines
# modulo: training_pipeline.py
# Funcionalidad: Pipeline principal de entrenamiento
# Version: 2.0
# ==========================================
# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------

from config.settings import DATASET_PATH

from ingestion.loader import cargar_dataset

from preprocessing.pipeline import (
    preparar_datos,
    dividir_datos,
    escalar_datos
)

from modeling.train import entrenar_modelo

from modeling.predict import predecir

from evaluation.metrics import calcular_metricas

from visualization.plots import (
    graficar_matriz_confusion
)


# -------------------------------------------------------------------------
# PIPELINE
# -------------------------------------------------------------------------

def ejecutar_pipeline_entrenamiento():
    """
    Proceso de ejecución del pipeline de entrenamiento.
    """
    print("\n[1] Cargando dataset...")

    df = cargar_dataset(DATASET_PATH)

    print(f"Dataset cargado: {df.shape}")

    # -------------------------------------------------------------
    # PREPROCESSING
    # -------------------------------------------------------------

    print("\n[2] Preparando datos...")

    X, y, df = preparar_datos(df)

    # -------------------------------------------------------------
    # SPLIT
    # -------------------------------------------------------------

    print("\n[3] Dividiendo train/test...")

    X_train, X_test, y_train, y_test = dividir_datos(
        X,
        y
    )

    # -------------------------------------------------------------
    # SCALING
    # -------------------------------------------------------------

    print("\n[4] Escalando datos...")

    X_train, X_test, scaler = escalar_datos(
        X_train,
        X_test
    )

    # -------------------------------------------------------------
    # MODEL
    # -------------------------------------------------------------

    print("\n[5] Entrenando modelo...")

    model = entrenar_modelo(
        X_train,
        y_train
    )

    # -------------------------------------------------------------
    # PREDICCIONES
    # -------------------------------------------------------------

    print("\n[6] Generando predicciones...")

    y_pred = predecir(
        model,
        X_test
    )

    # -------------------------------------------------------------
    # METRICAS
    # -------------------------------------------------------------

    print("\n[7] Evaluando modelo...")

    calcular_metricas(
        y_test,
        y_pred
    )

    # -------------------------------------------------------------
    # VISUALIZACION
    # -------------------------------------------------------------

    print("\n[8] Generando visualizaciones...")

    graficar_matriz_confusion(
        y_test,
        y_pred
    )

    print("\nPipeline finalizado")

    # -------------------------------------------------------------------------
# EJEMPLO USO
# -------------------------------------------------------------------------

if __name__ == "__main__":

    print(
        "\nPipeline de entrenamiento listo"
    )