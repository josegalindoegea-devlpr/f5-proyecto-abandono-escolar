# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: preprocessing
# modulo: cleaning.py
# Funcionalidad: 
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
import pandas as pd

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from config.settings import VARIABLES_NUMERICAS
from config.settings import VARIABLES_BOOLEANAS
from config.settings import VARIABLES_ORDINALES

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