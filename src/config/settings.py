# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: config
# modulo: settings.py
# Funcionalidad: 
# Version: 2.0
# ==========================================

# Estructura base de archivos
# proyecto_abandono_escolar/
# │
# ├── data/
# ├── datasets/
# ├── docs/
# ├── notebooks/
# ├── outputs/
# ├── prompts/
# ├── src/
# │   ├── config/
# │   │   └── settings.py
#
# ==========================================
# RUTAS
# ==========================================
from pathlib import Path

# ------------------------------------------
# ROOT del Proyecto
# ------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Resultado:
# proyecto_abandono_escolar/

# ------------------------------------------
# DATASETS
# ------------------------------------------

DATA_DIR = BASE_DIR / "data"

DATASET_DIR = BASE_DIR / "datasets"

#Caso volumen: 1000
DATASET_PATH_1K = DATA_DIR / "estudiantes_1k.csv"
#Caso volumen: 2000
DATASET_PATH_2K = DATA_DIR / "estudiantes_2k.csv"
#Caso volumen: 5000
DATASET_PATH_5K = DATA_DIR / "estudiantes_5k.csv"

# Asignamos el dataset por defecto seleccionando uno de los casos.
DATASET_PATH = DATASET_PATH_2K

# ------------------------------------------
# OUTPUTS
# ------------------------------------------

OUTPUTS_DIR = BASE_DIR / "outputs"

MODELS_DIR = OUTPUTS_DIR / "modelos"

METRICS_DIR = OUTPUTS_DIR / "metricas"

LOGS_DIR = OUTPUTS_DIR / "logs"

VISUALIZATIONS_DIR = OUTPUTS_DIR / "visualizaciones"

# ------------------------------------------
# DOCS
# ------------------------------------------

DOCS_DIR = BASE_DIR / "docs"

# ------------------------------------------
# NOTEBOOKS
# ------------------------------------------

NOTEBOOKS_DIR = BASE_DIR / "notebooks"

# ==========================================
# VARIABLES GLOBALES
# ==========================================

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


# ==========================================
# # CONSTANTES
# ==========================================

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


# ==========================================
# TARGET
# ==========================================

# ==========================================
# DATASET
# ==========================================

# ==========================================
# FEATURES
# ==========================================

# ==========================================
# RISK ENGINE
# ==========================================

# ==========================================
# MODEL
# ==========================================
DEFAULT_MODEL_NAME = "modelo_abandono.pkl"
DEFAULT_SCALER_NAME = "scaler_abandono.pkl"

# ==========================================
# VISUALIZATION
# ==========================================
ARCHIVO_METRICAS_MODELO = "metricas_modelo.csv"
ARCHIVO_DASHBOARD_PRINCIPAL = "dashboard_principal.png"