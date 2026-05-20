# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: persistence
# modulo: model_registry.py
# Funcionalidad: Persistencia y carga de modelo ML
# Version: 2.0
# ==========================================
# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
from pathlib import Path

import joblib

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from config.settings import (
    MODELS_DIR,
    DEFAULT_MODEL_NAME,
    DEFAULT_SCALER_NAME
)
from ingestion.loader import cargar_dataset

# -------------------------------------------------------------------------
# CREACION DIRECTORIOS
# -------------------------------------------------------------------------

MODELS_DIR.mkdir(
    parents=True,
    exist_ok=True
)



# -------------------------------------------------------------------------
# GUARDAR MODELO
# -------------------------------------------------------------------------

def guardar_modelo(
    modelo,
    nombre_modelo=DEFAULT_MODEL_NAME
):
    """
    Guarda modelo entrenado.

    Parameters
    ----------
    modelo : sklearn model

    nombre_modelo : str

    Returns
    -------
    pathlib.Path
    """

    ruta_modelo = (
        MODELS_DIR /
        nombre_modelo
    )

    joblib.dump(
        modelo,
        ruta_modelo
    )

    print("\nModelo guardado correctamente:")
    print(ruta_modelo)

    return ruta_modelo


# -------------------------------------------------------------------------
# CARGAR MODELO
# -------------------------------------------------------------------------

def cargar_modelo(
    nombre_modelo=DEFAULT_MODEL_NAME
):
    """
    Carga modelo entrenado.

    Parameters
    ----------
    nombre_modelo : str

    Returns
    -------
    sklearn model
    """

    ruta_modelo = (
        MODELS_DIR /
        nombre_modelo
    )

    if not ruta_modelo.exists():

        raise FileNotFoundError(
            f"No existe el modelo: {ruta_modelo}"
        )

    modelo = joblib.load(
        ruta_modelo
    )

    print("\nModelo cargado correctamente:")
    print(ruta_modelo)

    return modelo


# -------------------------------------------------------------------------
# GUARDAR SCALER
# -------------------------------------------------------------------------

def guardar_scaler(
    scaler,
    nombre_scaler=DEFAULT_SCALER_NAME
):
    """
    Guarda scaler entrenado.

    Parameters
    ----------
    scaler : StandardScaler

    nombre_scaler : str

    Returns
    -------
    pathlib.Path
    """

    ruta_scaler = (
        MODELS_DIR /
        nombre_scaler
    )

    joblib.dump(
        scaler,
        ruta_scaler
    )

    print("\nScaler guardado correctamente:")
    print(ruta_scaler)

    return ruta_scaler


# -------------------------------------------------------------------------
# CARGAR SCALER
# -------------------------------------------------------------------------

def cargar_scaler(
    nombre_scaler=DEFAULT_SCALER_NAME
):
    """
    Carga scaler previamente entrenado.

    Parameters
    ----------
    nombre_scaler : str

    Returns
    -------
    StandardScaler
    """

    ruta_scaler = (
        MODELS_DIR /
        nombre_scaler
    )

    if not ruta_scaler.exists():

        raise FileNotFoundError(
            f"No existe el scaler: {ruta_scaler}"
        )

    scaler = joblib.load(
        ruta_scaler
    )

    print("\nScaler cargado correctamente:")
    print(ruta_scaler)

    return scaler


# -------------------------------------------------------------------------
# GUARDAR PIPELINE COMPLETO
# -------------------------------------------------------------------------

def guardar_pipeline_completo(
    modelo,
    scaler,
    nombre_modelo=DEFAULT_MODEL_NAME,
    nombre_scaler=DEFAULT_SCALER_NAME
):
    """
    Guarda modelo y scaler.
    """

    guardar_modelo(
        modelo,
        nombre_modelo
    )

    guardar_scaler(
        scaler,
        nombre_scaler
    )

    print("\nPipeline persistido correctamente")


# -------------------------------------------------------------------------
# CARGAR PIPELINE COMPLETO
# -------------------------------------------------------------------------

def cargar_pipeline_completo(
    nombre_modelo=DEFAULT_MODEL_NAME,
    nombre_scaler=DEFAULT_SCALER_NAME
):
    """
    Carga modelo y scaler.

    Returns
    -------
    tuple
        (modelo, scaler)
    """

    modelo = cargar_modelo(
        nombre_modelo
    )

    scaler = cargar_scaler(
        nombre_scaler
    )

    return modelo, scaler


# -------------------------------------------------------------------------
# VALIDAR EXISTENCIA MODELO
# -------------------------------------------------------------------------

def existe_modelo(
    nombre_modelo=DEFAULT_MODEL_NAME
):
    """
    Verifica si existe modelo persistido.

    Returns
    -------
    bool
    """

    ruta_modelo = (
        MODELS_DIR /
        nombre_modelo
    )

    return ruta_modelo.exists()


# -------------------------------------------------------------------------
# VALIDAR EXISTENCIA SCALER
# -------------------------------------------------------------------------

def existe_scaler(
    nombre_scaler=DEFAULT_SCALER_NAME
):
    """
    Verifica si existe scaler persistido.

    Returns
    -------
    bool
    """

    ruta_scaler = (
        MODELS_DIR /
        nombre_scaler
    )

    return ruta_scaler.exists()


# -------------------------------------------------------------------------
# LISTAR MODELOS DISPONIBLES
# -------------------------------------------------------------------------

def listar_modelos():
    """
    Lista modelos disponibles en el registry.

    Returns
    -------
    list
    """

    modelos = list(
        MODELS_DIR.glob("*.pkl")
    )

    return modelos


# -------------------------------------------------------------------------
# MOSTRAR MODELOS DISPONIBLES
# -------------------------------------------------------------------------

def mostrar_modelos():
    """
    Muestra modelos persistidos.
    """

    modelos = listar_modelos()

    print("\n" + "=" * 60)
    print("MODELOS DISPONIBLES")
    print("=" * 60)

    if not modelos:

        print("No existen modelos registrados")

        return

    for modelo in modelos:

        print(f"- {modelo.name}")