# ==========================================
# modulo: preprocessing.py
# Funcionalidad: Preparación y transformación de datos
# Version: 2.0
# ==========================================

import pandas as pd

import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.compose import ColumnTransformer

from sklearn.pipeline import Pipeline

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import (
    StandardScaler,
    OneHotEncoder
)


# -------------------------------------------------------------------------
# CONFIGURACION GLOBAL
# -------------------------------------------------------------------------
TARGET = "abandono_escolar"

COLUMNAS_REQUERIDAS = [
    "asistencia_pct",
    "nota_media",
    "materias_suspensas",
    "numero_materias_curso",
    "evaluaciones_realizadas",
    "partes_disciplinarios",
    "matricula_activa",
    "oferta_educativa",
    "repetidor_curso_actual",
    "dias_sin_actividad",
    "inasistencias_consecutivas",
    "grado_urbanizacion",
    "distancia_escuela",
    "acceso_internet",
    "nivel_socioeconomico",
    "apoyo_familiar",
    "trabaja",
    TARGET
]

VARIABLES_NUMERICAS = [
    "asistencia_pct",
    "nota_media",
    "materias_suspensas",
    "numero_materias_curso",
    "evaluaciones_realizadas",
    "partes_disciplinarios",
    "dias_sin_actividad",
    "inasistencias_consecutivas",
    "distancia_escuela"
]

VARIABLES_BOOLEANAS = [
    "matricula_activa",
    "repetidor_curso_actual",
    "acceso_internet",
    "apoyo_familiar",
    "trabaja"
]

VARIABLES_ORDINALES = [
    "oferta_educativa",
    "grado_urbanizacion",
    "nivel_socioeconomico",
]

VARIABLES_CRITICAS = [
    "asistencia_pct",
    "matricula_activa",
    "dias_sin_actividad"
]

MAPEO_RIESGO_OFERTA = {
    1: 0.3,   # ESO
    2: 0.2,   # Bachillerato
    3: 0.8,   # FP Básica
    4: 0.5    # FP Medio
}

UMBRALES_DISTANCIA = {
    1: 40,    # Rural
    2: 20,    # Semiurbano
    3: 10     # Urbano
}

# =============================================================================
# CONSTANTES
# =============================================================================

MAX_DIAS_INACTIVIDAD = 65
MAX_INASISTENCIAS = 65
CORTE_ASISTENCIA = 30

MIN_NOTA = 0.0
MAX_NOTA = 10.0
CORTE_NOTA = 3

MIN_ASISTENCIA = 0.0
MAX_ASISTENCIA = 100.0
NORMAL_ASISTENCIA = 80
DEFAULT_SEED = 42

PROBABILIDAD_MATRICULA = 0.92
PROBABILIDAD_REPETIDOR = 0.20
PROBABILIDAD_TRABAJA = 0.25
PROBABILIDAD_FAMILIAR = 0.78
PROBABILIDAD_INTERNET = 0.88
PROBABILIDAD_NOTA = 0.75

NIVEL_SOCIOECO_MIN = 1
NIVEL_SOCIECO_MAX = 6
MIN_MATERIAS_CURSO = 10
MAX_MATERIAS_CURSO = 14
MIN_OFERTA_EDUCATIVA = 1
MAX_OFERTA_EDUCATIVA = 4
MIN_URBANIZACION = 1
MAX_URBANIZACION = 3


# -------------------------------------------------------------------------
# FUNCIONALIDAD
#
# Las fases principales son:
# 1. Carga
# 2. Validación estructural
# 3. Limpieza y tipado
# 4. Gestión de missing values
# 5. Ingeniería de variables de riesgo
# 6. Transformación ML (encoding/escalado)2. Validación estructural
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# 1. Carga
# -------------------------------------------------------------------------

def cargar_dataset(ruta_dataset):
    """
    Carga el dataset desde un archivo CSV.
    """

    df = pd.read_csv(ruta_dataset)

    return df

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
# 3. Tipar variables
# -------------------------------------------------------------------------
def tipar_variables(df):
    """
    Convierte columnas a tipos consistentes.
    """
    for col in VARIABLES_NUMERICAS:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    for col in VARIABLES_BOOLEANAS:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    for col in VARIABLES_ORDINALES:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df

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

# -------------------------------------------------------------------------
# 5. Gestión de missing values
# -------------------------------------------------------------------------
def gestionar_missing_values(df):
    """
    Gestiona valores faltantes según reglas operativas.
    """

    # -------------------------------------------------------------
    # VARIABLES CRITICAS
    # -------------------------------------------------------------

    for col in VARIABLES_CRITICAS:

        df = df[
            df[col].notnull()
        ]

    # -------------------------------------------------------------
    # VARIABLES NUMERICAS
    # Mediana por oferta educativa
    # -------------------------------------------------------------

    for col in VARIABLES_NUMERICAS:

        if col != "nota_media":

            df[col] = (
                df.groupby("oferta_educativa")[col]
                .transform(
                    lambda x: x.fillna(
                        x.median()
                    )
                )
            )

    # -------------------------------------------------------------
    # NOTA MEDIA
    # -------------------------------------------------------------

    df["nota_media_missing"] = (
        df["nota_media"].isnull()
    ).astype(int)

    df["nota_media"] = (
        df.groupby("oferta_educativa")["nota_media"]
        .transform(
            lambda x: x.fillna(
                x.median()
            )
        )
    )

    # -------------------------------------------------------------
    # VARIABLES BOOLEANAS
    # Categoria auxiliar
    # -------------------------------------------------------------

    for col in VARIABLES_BOOLEANAS:

        missing_col = f"{col}_missing"

        df[missing_col] = (
            df[col].isnull()
        ).astype(int)

        df[col] = df[col].fillna(0)

    return df


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

# -------------------------------------------------------------------------
# 8. Preparacion de features ML
# -------------------------------------------------------------------------
def preparar_features(df):
    """
    Selecciona variables finales para ML.
    """

    columnas_modelo = [

        "R_asistencia",
        "R_inactividad",
        "R_notas",
        "R_suspensas",
        "R_socioeco",
        "R_familia",
        "R_trabajo",
        "R_internet",
        "R_distancia",
        "R_oferta",

        "nota_media_missing",
        "acceso_internet_missing",
        "apoyo_familiar_missing",
        "trabaja_missing"
    ]

    X = df[columnas_modelo]

    y = df[TARGET]

    return X, y

# -------------------------------------------------------------------------
# 9. Pipeline completo
# -------------------------------------------------------------------------
def preparar_datos(df):
    """
    Ejecuta pipeline completo.
    """

    validar_dataset(df)

    df = tipar_variables(df)

    validar_rangos(df)

    df = gestionar_missing_values(df)

    df = generar_variables_riesgo(df)

    df = generar_risk_index(df)

    X, y = preparar_features(df)

    return X, y, df

# -------------------------------------------------------------------------
# 10. Dividir datos (Split Train Test)
# -------------------------------------------------------------------------
def dividir_datos(
    X,
    y,
    test_size=0.2
):
    """
    Divide train/test.
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42,
        stratify=y
    )


def escalar_datos(X_train, X_test):
    """
    Escala las variables numéricas.
    """

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler

