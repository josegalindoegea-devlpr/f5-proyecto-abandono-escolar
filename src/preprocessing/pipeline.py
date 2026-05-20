# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: preprocessing
# modulo: pipeline.py
# Funcionalidad: 
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from config.settings import TARGET
from risk.risk_variables import generar_risk_index
from risk.risk_variables import generar_variables_riesgo
from preprocessing.missing import gestionar_missing_values
from preprocessing.cleaning import tipar_variables
from ingestion.validator import validar_dataset
from ingestion.validator import validar_rangos


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