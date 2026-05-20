# ==========================================
# Proyecto: Abandono escolar
# modulo: main.py
# Funcionalidad: Ejecución principal del proyecto
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS Generales
# -------------------------------------------------------------------------
from datetime import datetime

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------

from utils.logger import (
    configurar_logger,
    log_info,
    log_error
)

from ingestion.loader import cargar_dataset

from preprocessing.pipeline import preparar_datos
from preprocessing.pipeline import dividir_datos
from preprocessing.pipeline import escalar_datos

from modeling.train import entrenar_modelo
from modeling.predict import predecir

from evaluation.metrics import calcular_metricas

from visualization.plots import graficar_matriz_confusion

from pipelines.training_pipeline import (
    ejecutar_pipeline_entrenamiento
)

from pipelines.inference_pipeline import (
    ejecutar_pipeline_inferencia
)

# -------------------------------------------------------------------------
# Configuracion del log
# -------------------------------------------------------------------------
logger = configurar_logger()

# -------------------------------------------------------------------------
# Pipelines preparadas
# -------------------------------------------------------------------------
def pipeline_entrenamiento():
    """    
    pipeline de entrenamiento
    """
    try:


        log_info(
            "Inicio sistema abandono escolar - Pipeline de Entrenamiento"
        )

        # Ejecutar pipeline
        ejecutar_pipeline_entrenamiento()

        log_info(
            "Pipeline ejecutado correctamente"
        )

    except Exception as e:

        log_error(
            f"Error ejecución en main.py: {str(e)}"
        )

def pipeline_inferencia():
    """    
    pipeline de inferencia
    """
    try:

        log_info(
            "Inicio sistema abandono escolar - Pipeline de Inferencia"
        )

        # Ejecutar pipeline
        ejecutar_pipeline_inferencia()

        log_info(
            "Pipeline ejecutado correctamente"
        )

    except Exception as e:

        log_error(
            f"Error ejecución en main.py: {str(e)}"
        )

# -------------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------------        
def main():

    print("=" * 60)
    tempo_ini = datetime.now()
    tempo_ini_str =tempo_ini.now().strftime("%Y-%m-%d %H:%M:%S")
    print("SISTEMA PREDICCION ABANDONO ESCOLAR")
    print(f"[{tempo_ini_str}] INICIO.")
    print("=" * 60)

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ahora}] Pipeline de ENTRENAMIENTO")
    pipeline_entrenamiento()

    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ahora}] Pipeline de INFERENCIA")
    pipeline_inferencia()

    print("=" * 60)
    tempo_fin = datetime.now()
    tempo_fin_str = tempo_fin.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{tempo_fin_str}] FINALIZACION.")
    segundos_totales = (tempo_fin - tempo_ini).total_seconds()
    print(f"[{segundos_totales:.2f} segundos] DURACION.")
    print("=" * 60)

# -------------------------------------------------------------------------
# ENTRY POINT
# -------------------------------------------------------------------------

if __name__ == "__main__":

    main()