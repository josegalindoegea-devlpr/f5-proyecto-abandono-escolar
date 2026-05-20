# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: ingestion
# modulo: loader.py
# Funcionalidad: 
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
import pandas as pd
import sys

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------

from config.settings import DATASET_PATH

# -------------------------------------------------------------------------
# 1. Carga
# -------------------------------------------------------------------------

def cargar_dataset(ruta_dataset):
    """
    Carga el dataset desde un archivo CSV de forma segura.
    """
    try:
        df = pd.read_csv(ruta_dataset)
        print(f"Éxito: Dataset cargado correctamente desde {ruta_dataset}")
        return df
        
    except FileNotFoundError:
        print(f"Error: No se encontró ningún archivo en la ruta '{ruta_dataset}'.", file=sys.stderr)
        return None
        
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo en '{ruta_dataset}' está completamente vacío.", file=sys.stderr)
        return None
        
    except pd.errors.ParserError:
        print(f"Error: El archivo en '{ruta_dataset}' no se pudo parsear /pɑːrz/ (formato CSV inválido o delimitador incorrecto).", file=sys.stderr)
        return None
        
    except PermissionError:
        print(f"Error: No tienes permisos de lectura para acceder a '{ruta_dataset}'.", file=sys.stderr)
        return None
        
    except Exception as e:
        print(f"Error inesperado al cargar el dataset: {e}", file=sys.stderr)
        return None