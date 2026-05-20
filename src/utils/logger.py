# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: utils
# modulo: logger.py
# Funcionalidad: Configuracion centralizada de logging
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
import logging

from pathlib import Path
# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from config.settings import (
    OUTPUTS_DIR,
    LOGS_DIR
)

# -------------------------------------------------------------------------
# DIRECTORIO LOGS
# -------------------------------------------------------------------------
LOGS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# -------------------------------------------------------------------------
# ARCHIVO LOG PRINCIPAL
# -------------------------------------------------------------------------

LOG_FILE = LOGS_DIR / "abandono_escolar.log"


# -------------------------------------------------------------------------
# CONFIGURACION BASE LOGGER
# -------------------------------------------------------------------------

def configurar_logger(
    nombre_logger="abandono_escolar",
    nivel=logging.INFO
):
    """
    Configura logger principal del sistema.

    Parameters
    ----------
    nombre_logger : str

    nivel : logging level

    Returns
    -------
    logging.Logger
    """

    logger = logging.getLogger(
        nombre_logger
    )

    # -------------------------------------------------------------
    # EVITAR DUPLICAR HANDLERS
    # -------------------------------------------------------------

    if logger.handlers:

        return logger

    logger.setLevel(nivel)

    # -------------------------------------------------------------
    # FORMATO
    # -------------------------------------------------------------

    formatter = logging.Formatter(

        fmt=(
            "%(asctime)s | "
            "%(levelname)s | "
            "%(name)s | "
            "%(message)s"
        ),

        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # -------------------------------------------------------------
    # FILE HANDLER
    # -------------------------------------------------------------

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setLevel(nivel)

    file_handler.setFormatter(
        formatter
    )

    # -------------------------------------------------------------
    # CONSOLE HANDLER
    # -------------------------------------------------------------

    console_handler = logging.StreamHandler()

    console_handler.setLevel(nivel)

    console_handler.setFormatter(
        formatter
    )

    # -------------------------------------------------------------
    # REGISTRO HANDLERS
    # -------------------------------------------------------------

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)

    return logger


# -------------------------------------------------------------------------
# LOGGER DEFAULT
# -------------------------------------------------------------------------

logger = configurar_logger()


# -------------------------------------------------------------------------
# FUNCIONES AUXILIARES
# -------------------------------------------------------------------------

def log_inicio_pipeline(
    nombre_pipeline
):
    """
    Registra inicio de pipeline.
    """

    logger.info(
        f"INICIO PIPELINE: {nombre_pipeline}"
    )


def log_fin_pipeline(
    nombre_pipeline
):
    """
    Registra finalizacion pipeline.
    """

    logger.info(
        f"FIN PIPELINE: {nombre_pipeline}"
    )


def log_dataset_cargado(
    shape
):
    """
    Registra dimensiones dataset.
    """

    logger.info(
        f"Dataset cargado correctamente: {shape}"
    )


def log_modelo_entrenado(
    modelo_nombre
):
    """
    Registra entrenamiento modelo.
    """

    logger.info(
        f"Modelo entrenado: {modelo_nombre}"
    )


def log_metricas(
    metricas
):
    """
    Registra metricas principales.
    """

    logger.info(
        f"Metricas modelo: {metricas}"
    )


def log_error(
    mensaje_error
):
    """
    Registra errores.
    """

    logger.error(
        mensaje_error
    )


def log_warning(
    mensaje
):
    """
    Registra warnings.
    """

    logger.warning(
        mensaje
    )


def log_info(
    mensaje
):
    """
    Registra informacion general.
    """

    logger.info(
        mensaje
    )


def log_debug(
    mensaje
):
    """
    Registra informacion debug.
    """

    logger.debug(
        mensaje
    )


# -------------------------------------------------------------------------
# TEST LOGGER
# -------------------------------------------------------------------------

if __name__ == "__main__":

    logger = configurar_logger()

    log_info(
        "Sistema de logging inicializado"
    )

    log_warning(
        "Ejemplo warning"
    )

    log_error(
        "Ejemplo error"
    )