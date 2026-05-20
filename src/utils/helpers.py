# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: utils
# modulo: helper.py
# Funcionalidad: Auxiliares reutilizables
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
from pathlib import Path

from datetime import datetime

import pandas as pd
import numpy as np
# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from utils.logger import (
    log_info,
    log_error
)

# -------------------------------------------------------------------------
# CREAR DIRECTORIO
# -------------------------------------------------------------------------

def crear_directorio(
    ruta_directorio
):
    """
    Crea directorio si no existe.

    Parameters
    ----------
    ruta_directorio : str | Path
    """

    try:

        Path(
            ruta_directorio
        ).mkdir(
            parents=True,
            exist_ok=True
        )

        log_info(
            f"Directorio creado/verificado: {ruta_directorio}"
        )

    except Exception as e:

        log_error(
            f"Error creando directorio: {str(e)}"
        )

        raise


# -------------------------------------------------------------------------
# TIMESTAMP ACTUAL
# -------------------------------------------------------------------------

def obtener_timestamp():
    """
    Genera timestamp formateado.

    Returns
    -------
    str
    """

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


# -------------------------------------------------------------------------
# GUARDAR DATAFRAME CSV
# -------------------------------------------------------------------------

def guardar_dataframe_csv(
    df,
    ruta_salida,
    index=False
):
    """
    Guarda DataFrame en CSV.

    Parameters
    ----------
    df : pandas.DataFrame

    ruta_salida : str | Path

    index : bool
    """

    try:

        ruta_salida = Path(
            ruta_salida
        )

        crear_directorio(
            ruta_salida.parent
        )

        df.to_csv(
            ruta_salida,
            index=index
        )

        log_info(
            f"CSV guardado: {ruta_salida}"
        )

    except Exception as e:

        log_error(
            f"Error guardando CSV: {str(e)}"
        )

        raise


# -------------------------------------------------------------------------
# CARGAR DATAFRAME CSV
# -------------------------------------------------------------------------

def cargar_dataframe_csv(
    ruta_csv
):
    """
    Carga DataFrame desde CSV.

    Parameters
    ----------
    ruta_csv : str | Path

    Returns
    -------
    pandas.DataFrame
    """

    try:

        df = pd.read_csv(
            ruta_csv
        )

        log_info(
            f"CSV cargado correctamente: {ruta_csv}"
        )

        return df

    except Exception as e:

        log_error(
            f"Error cargando CSV: {str(e)}"
        )

        raise


# -------------------------------------------------------------------------
# MOSTRAR SHAPE DATAFRAME
# -------------------------------------------------------------------------

def mostrar_shape_dataframe(
    df,
    nombre="dataset"
):
    """
    Muestra dimensiones DataFrame.
    """

    filas, columnas = df.shape

    print("\n" + "=" * 60)

    print(
        f"{nombre.upper()} -> "
        f"Filas: {filas} | "
        f"Columnas: {columnas}"
    )

    print("=" * 60)


# -------------------------------------------------------------------------
# RESUMEN MISSINGS
# -------------------------------------------------------------------------

def resumen_missing_values(
    df
):
    """
    Resume missing values.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
    """

    resumen = pd.DataFrame({

        "missing_total":
            df.isnull().sum(),

        "missing_pct":
            (
                df.isnull().mean() * 100
            ).round(2)
    })

    resumen = resumen[
        resumen["missing_total"] > 0
    ]

    resumen = resumen.sort_values(
        by="missing_pct",
        ascending=False
    )

    return resumen


# -------------------------------------------------------------------------
# VALIDAR COLUMNAS
# -------------------------------------------------------------------------

def validar_columnas(
    df,
    columnas_requeridas
):
    """
    Verifica columnas requeridas.

    Parameters
    ----------
    df : pandas.DataFrame

    columnas_requeridas : list
    """

    faltantes = [

        col for col in columnas_requeridas

        if col not in df.columns
    ]

    if faltantes:

        raise ValueError(
            f"Columnas faltantes: {faltantes}"
        )

    return True


# -------------------------------------------------------------------------
# CONVERTIR BOOLEANOS
# -------------------------------------------------------------------------

def convertir_booleanos(
    df,
    columnas
):
    """
    Convierte columnas binarias.

    Parameters
    ----------
    df : pandas.DataFrame

    columnas : list

    Returns
    -------
    pandas.DataFrame
    """

    for col in columnas:

        df[col] = (
            df[col]
            .astype(int)
        )

    return df


# -------------------------------------------------------------------------
# CLIP RANGO
# -------------------------------------------------------------------------

def aplicar_clip(
    serie,
    minimo,
    maximo
):
    """
    Limita rango valores.

    Parameters
    ----------
    serie : pandas.Series

    minimo : float

    maximo : float

    Returns
    -------
    pandas.Series
    """

    return serie.clip(
        lower=minimo,
        upper=maximo
    )


# -------------------------------------------------------------------------
# NORMALIZACION MIN-MAX
# -------------------------------------------------------------------------

def normalizar_minmax(
    serie
):
    """
    Escalado min-max.

    Parameters
    ----------
    serie : pandas.Series

    Returns
    -------
    pandas.Series
    """

    minimo = serie.min()

    maximo = serie.max()

    if minimo == maximo:

        return pd.Series(
            np.zeros(len(serie))
        )

    return (
        (serie - minimo) /
        (maximo - minimo)
    )


# -------------------------------------------------------------------------
# RESUMEN DATASET
# -------------------------------------------------------------------------

def generar_resumen_dataset(
    df
):
    """
    Genera resumen ejecutivo dataset.

    Parameters
    ----------
    df : pandas.DataFrame
    """

    print("\n" + "=" * 60)
    print("RESUMEN DATASET")
    print("=" * 60)

    print(
        f"Filas: {df.shape[0]}"
    )

    print(
        f"Columnas: {df.shape[1]}"
    )

    print(
        f"Missing Values Totales: "
        f"{df.isnull().sum().sum()}"
    )

    print("=" * 60)


# -------------------------------------------------------------------------
# EXPORTAR TXT SIMPLE
# -------------------------------------------------------------------------

def exportar_texto(
    contenido,
    ruta_archivo
):
    """
    Exporta contenido texto.

    Parameters
    ----------
    contenido : str

    ruta_archivo : str | Path
    """

    try:

        ruta_archivo = Path(
            ruta_archivo
        )

        crear_directorio(
            ruta_archivo.parent
        )

        with open(
            ruta_archivo,
            "w",
            encoding="utf-8"
        ) as archivo:

            archivo.write(
                contenido
            )

        log_info(
            f"Archivo exportado: {ruta_archivo}"
        )

    except Exception as e:

        log_error(
            f"Error exportando texto: {str(e)}"
        )

        raise


# -------------------------------------------------------------------------
# TEST MODULO
# -------------------------------------------------------------------------

if __name__ == "__main__":

    print("\nHelpers cargados correctamente")