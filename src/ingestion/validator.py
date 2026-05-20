# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: ingestion
# modulo: validator.py
# Funcionalidad: 
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from config.settings import COLUMNAS_REQUERIDAS

# -------------------------------------------------------------------------
# 2. Validación estructural
# -------------------------------------------------------------------------
def validar_dataset(df):
    """
    Valida estructura mínima del dataset.
    """

    faltantes = [
        col for col in COLUMNAS_REQUERIDAS
        if col not in df.columns
    ]

    if faltantes:
        raise ValueError(
            f"Columnas faltantes: {faltantes}"
        )

    if df.empty:
        raise ValueError("El Dataset está vacío")

    return True

# -------------------------------------------------------------------------
# 4. Validacion de rangos
# -------------------------------------------------------------------------
def validar_rangos(df):
    """
    Valida rangos lógicos del modelo.
    """

    if (
        (df["asistencia_pct"] < 0) |
        (df["asistencia_pct"] > 100)
    ).any():

        raise ValueError(
            "asistencia_pct fuera de rango [0,100]"
        )

    if (
        (df["nota_media"] < 0) |
        (df["nota_media"] > 10)
    ).any():

        raise ValueError(
            "nota_media fuera de rango [0,10]"
        )

    if (
        (df["nivel_socioeconomico"] < 1) |
        (df["nivel_socioeconomico"] > 6)
    ).any():

        raise ValueError(
            "nivel_socioeconomico fuera de rango [1,6]"
        )

    return True