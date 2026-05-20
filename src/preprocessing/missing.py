# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: preprocessing
# modulo: missing.py
# Funcionalidad: 
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from config.settings import VARIABLES_NUMERICAS
from config.settings import VARIABLES_BOOLEANAS
from config.settings import VARIABLES_CRITICAS

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

