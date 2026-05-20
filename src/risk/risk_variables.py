# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: risk
# modulo: risk_variables.py
# Funcionalidad: 
# Version: 2.0
# ==========================================
# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
import numpy as np
import pandas as pd

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from config.settings import VARIABLES_NUMERICAS
from config.settings import MAPEO_RIESGO_OFERTA
from config.settings import UMBRALES_DISTANCIA

# -------------------------------------------------------------------------
# 6. Generacion de variables de riesgo
# -------------------------------------------------------------------------
def generar_variables_riesgo(df):
    """
    Genera variables normalizadas [0,1].
    """

    # -------------------------------------------------------------
    # RIESGO ASISTENCIA
    # -------------------------------------------------------------

    df["R_asistencia"] = (
        1 - (df["asistencia_pct"] / 100)
    )

    # -------------------------------------------------------------
    # RIESGO NOTAS
    # -------------------------------------------------------------

    df["R_notas"] = (
        1 - (df["nota_media"] / 10)
    )

    # -------------------------------------------------------------
    # RIESGO SUSPENSAS
    # -------------------------------------------------------------

    df["R_suspensas"] = (
        df["materias_suspensas"] /
        df["numero_materias_curso"]
    )

    df["R_suspensas"] = (
        df["R_suspensas"]
        .clip(0, 1)
    )

    # -------------------------------------------------------------
    # RIESGO INACTIVIDAD
    # -------------------------------------------------------------

    df["R_inactividad"] = np.minimum(
        df["dias_sin_actividad"] / 30,
        1
    )

    # -------------------------------------------------------------
    # RIESGO INTERNET
    # -------------------------------------------------------------

    df["R_internet"] = (
        1 - df["acceso_internet"]
    )

    # -------------------------------------------------------------
    # RIESGO FAMILIA
    # -------------------------------------------------------------

    df["R_familia"] = (
        1 - df["apoyo_familiar"]
    )

    # -------------------------------------------------------------
    # RIESGO TRABAJO
    # -------------------------------------------------------------

    df["R_trabajo"] = (
        df["trabaja"]
    )

    # -------------------------------------------------------------
    # RIESGO SOCIOECONOMICO
    # -------------------------------------------------------------

    df["R_socioeco"] = (
        (df["nivel_socioeconomico"] - 1) / 5
    )

    # -------------------------------------------------------------
    # RIESGO DISTANCIA
    # -------------------------------------------------------------

    df["umbral_distancia"] = (
        df["grado_urbanizacion"]
        .map(UMBRALES_DISTANCIA)
    )

    df["R_distancia"] = np.minimum(
        (
            df["distancia_escuela"] /
            df["umbral_distancia"]
        ),
        1
    )

    # -------------------------------------------------------------
    # RIESGO OFERTA
    # -------------------------------------------------------------

    df["R_oferta"] = (
        df["oferta_educativa"]
        .map(MAPEO_RIESGO_OFERTA)
    )

    return df

# -------------------------------------------------------------------------
# 7. Generacion del Risk Index
# -------------------------------------------------------------------------
def generar_risk_index(df):
    """
    Calcula índice final de riesgo.
    """

    df["RiskIndex"] = (

        0.22 * df["R_asistencia"] +

        0.18 * df["R_inactividad"] +

        0.12 * df["R_notas"] +

        0.08 * df["R_suspensas"] +

        0.12 * df["R_socioeco"] +

        0.08 * df["R_familia"] +

        0.07 * df["R_trabajo"] +

        0.05 * df["R_internet"] +

        0.05 * df["R_distancia"] +

        0.03 * df["R_oferta"]
    )

    df["RiskIndex"] = (
        df["RiskIndex"]
        .clip(0, 1)
    )

    return df