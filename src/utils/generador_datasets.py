"""
===============================================================================
GENERADOR PROFESIONAL DE DATASET SINTÉTICO - ABANDONO ESCOLAR
===============================================================================

Versión:
    2.0 Production Ready

Autor:
    Varios

Descripción:
----------------------------------------------------------------------------
Generador profesional de datasets sintéticos orientados al entrenamiento
de modelos de Machine Learning para detección de abandono escolar.

Características:
----------------------------------------------------------------------------
✔ Arquitectura modular
✔ Compatible producción / notebooks / terminal
✔ CLI profesional con argparse
✔ Logging avanzado
✔ Validaciones robustas
✔ Generación estadística coherente
✔ Motor de reglas configurable
✔ Exportación CSV
✔ README automático
✔ Diccionario de datos
✔ Estadísticas descriptivas
✔ Reproducibilidad mediante seed
✔ Manejo de excepciones
✔ Código tipado y documentado
✔ Compatible pipelines ML / MLOps

Dependencias:
----------------------------------------------------------------------------
pip install pandas numpy

Ejemplo ejecución:
----------------------------------------------------------------------------
python generador_dataset.py \
    --rows 10000 \
    --output ./output_datasets \
    --file abandono.csv \
    --seed 42
    
===============================================================================
"""
# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
from __future__ import annotations

import argparse
import logging
import random
import sys
import time
import warnings
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore", category=DeprecationWarning)

# =============================================================================
# CONFIGURACIÓN LOGGING
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

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
DEFAULT_ROWS = 1000
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


# =============================================================================
# CONFIG DATACLASS
# =============================================================================


@dataclass
class DatasetConfig:
    rows: int
    output_path: Path
    filename: str
    seed: Optional[int] = None


# =============================================================================
# UTILIDADES
# =============================================================================

def configure_seed(seed: Optional[int]) -> None:
    """
    Configura semilla global.
    """

    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

        logger.info(f"Seed configurada: {seed}")


def truncate(value: float, minimum: float, maximum: float) -> float:
    """
    Trunca valores dentro de rango.
    """

    return max(minimum, min(value, maximum))


def boolean_by_probability(probability_true: float) -> int:
    """
    Genera booleano binario basado en probabilidad.
    """

    return int(random.random() < probability_true)


def ensure_csv_extension(filename: str) -> str:
    """
    Garantiza extensión .csv
    """

    if not filename.endswith(".csv"):
        filename += ".csv"

    return filename


# =============================================================================
# MOTOR REGLAS ABANDONO
# =============================================================================

def calculate_dropout(
    matricula_activa: int,
    dias_sin_actividad: int,
    asistencia_pct: float,
    evaluaciones_realizadas: int,
    nota_media: Optional[float]
) -> int:
    """
    Determina abandono escolar según reglas definidas.
    """

    # -------------------------------------------------------------------------
    # R1 - Abandono administrativo
    # -------------------------------------------------------------------------

    if matricula_activa == 0:
        return 1

    # -------------------------------------------------------------------------
    # R2 - Inactividad crítica
    # -------------------------------------------------------------------------

    if (
        dias_sin_actividad >= 60
        and asistencia_pct < 20
    ):
        return 1

    # -------------------------------------------------------------------------
    # R3 - Desvinculación académica severa
    # -------------------------------------------------------------------------

    if (
        evaluaciones_realizadas == 0
        and asistencia_pct < CORTE_ASISTENCIA
        and (
            pd.isna(nota_media)
            or nota_media < CORTE_NOTA
        )
    ):
        return 1

    return 0


# =============================================================================
# GENERADOR REGISTRO
# =============================================================================

def generate_record() -> Dict[str, Any]:
    """
    Genera registro coherente y semi-realista.
    """

    # -------------------------------------------------------------------------
    # VARIABLES BASE
    # -------------------------------------------------------------------------
  
    matricula_activa = boolean_by_probability(PROBABILIDAD_MATRICULA)

    repetidor = boolean_by_probability(PROBABILIDAD_REPETIDOR)

    trabaja = boolean_by_probability(PROBABILIDAD_TRABAJA)

    apoyo_familiar = boolean_by_probability(PROBABILIDAD_FAMILIAR)

    acceso_internet = boolean_by_probability(PROBABILIDAD_INTERNET)

    nivel_socioeconomico = random.randint(NIVEL_SOCIOECO_MIN, NIVEL_SOCIECO_MAX)

    # -------------------------------------------------------------------------
    # ASISTENCIA
    # -------------------------------------------------------------------------

    asistencia = np.random.normal(NORMAL_ASISTENCIA, 15)

    if repetidor:
        asistencia -= 10

    if trabaja:
        asistencia -= 8

    if not apoyo_familiar:
        asistencia -= 12

    if not matricula_activa:
        asistencia -= 55

    if nivel_socioeconomico >= 5:
        asistencia -= 8

    asistencia_pct = round(
        truncate(asistencia, 0, 100),
        2
    )

    # -------------------------------------------------------------------------
    # DÍAS SIN ACTIVIDAD
    # -------------------------------------------------------------------------

    dias_sin_actividad = int(
        truncate(
            np.random.normal(10, 10),
            1,
            MAX_DIAS_INACTIVIDAD
        )
    )

    if asistencia_pct < 30:
        dias_sin_actividad += random.randint(15, 40)

    dias_sin_actividad = min(
        dias_sin_actividad,
        MAX_DIAS_INACTIVIDAD
    )

    # -------------------------------------------------------------------------
    # INASISTENCIAS
    # -------------------------------------------------------------------------

    inasistencias_consecutivas = int(
        truncate(
            np.random.normal(6, 8),
            1,
            MAX_INASISTENCIAS
        )
    )

    if asistencia_pct < 25:
        inasistencias_consecutivas += random.randint(10, 30)

    inasistencias_consecutivas = min(
        inasistencias_consecutivas,
        MAX_INASISTENCIAS
    )

    # -------------------------------------------------------------------------
    # EVALUACIONES
    # -------------------------------------------------------------------------

    if asistencia_pct < CORTE_ASISTENCIA:
        evaluaciones_realizadas = random.choice([0, 0, 1, 1, 2])
    else:
        evaluaciones_realizadas = random.randint(1, 4)

    # -------------------------------------------------------------------------
    # NOTA MEDIA
    # -------------------------------------------------------------------------

    if evaluaciones_realizadas == 0:

        if boolean_by_probability(PROBABILIDAD_NOTA):
            nota_media = np.nan
        else:
            nota_media = round(
                truncate(
                    np.random.normal(2.0, 1.2),
                    MIN_NOTA,
                    MAX_NOTA
                ),
                2
            )

    else:

        nota = np.random.normal(6.5, 1.5)

        if asistencia_pct < 40:
            nota -= 2

        if repetidor:
            nota -= 1

        if trabaja:
            nota -= 0.8

        if not apoyo_familiar:
            nota -= 1.2

        nota_media = round(
            truncate(nota, MIN_NOTA, MAX_NOTA),
            2
        )

    # -------------------------------------------------------------------------
    # MATERIAS
    # -------------------------------------------------------------------------

    numero_materias_curso = random.randint(MIN_MATERIAS_CURSO, MAX_MATERIAS_CURSO)

    if pd.isna(nota_media):

        materias_suspensas = random.randint(6, 10)

    else:

        ratio = (10 - nota_media) / 10

        materias_suspensas = int(
            truncate(
                ratio * numero_materias_curso
                + random.randint(0, 2),
                0,
                10
            )
        )

    # -------------------------------------------------------------------------
    # DISCIPLINA
    # -------------------------------------------------------------------------

    partes_disciplinarios = int(
        truncate(
            np.random.normal(2, 2),
            0,
            10
        )
    )

    if asistencia_pct < 40:
        partes_disciplinarios += random.randint(1, 4)

    partes_disciplinarios = min(
        partes_disciplinarios,
        10
    )

    # -------------------------------------------------------------------------
    # VARIABLES RESTANTES
    # -------------------------------------------------------------------------

    oferta_educativa = random.randint(MIN_OFERTA_EDUCATIVA, MAX_OFERTA_EDUCATIVA)

    grado_urbanizacion = random.randint(MIN_URBANIZACION, MAX_URBANIZACION)

    distancia_escuela = round(
        truncate(
            np.random.normal(12, 10),
            1,
            50
        ),
        2
    )

    # -------------------------------------------------------------------------
    # VARIABLE OBJETIVO
    # -------------------------------------------------------------------------

    abandono_escolar = calculate_dropout(
        matricula_activa=matricula_activa,
        dias_sin_actividad=dias_sin_actividad,
        asistencia_pct=asistencia_pct,
        evaluaciones_realizadas=evaluaciones_realizadas,
        nota_media=nota_media
    )

    return {
        "asistencia_pct": asistencia_pct,
        "nota_media": nota_media,
        "materias_suspensas": materias_suspensas,
        "numero_materias_curso": numero_materias_curso,
        "evaluaciones_realizadas": evaluaciones_realizadas,
        "partes_disciplinarios": partes_disciplinarios,
        "matricula_activa": matricula_activa,
        "oferta_educativa": oferta_educativa,
        "repetidor_curso_actual": repetidor,
        "dias_sin_actividad": dias_sin_actividad,
        "inasistencias_consecutivas": inasistencias_consecutivas,
        "grado_urbanizacion": grado_urbanizacion,
        "distancia_escuela": distancia_escuela,
        "acceso_internet": acceso_internet,
        "nivel_socioeconomico": nivel_socioeconomico,
        "apoyo_familiar": apoyo_familiar,
        "trabaja": trabaja,
        "abandono_escolar": abandono_escolar
    }


# =============================================================================
# GENERADOR DATAFRAME
# =============================================================================

def generate_dataset(rows: int) -> pd.DataFrame:
    """
    Genera dataset completo.
    """

    logger.info(f"Generando {rows} registros...")

    records: List[Dict[str, Any]] = [
        generate_record()
        for _ in range(rows)
    ]

    df = pd.DataFrame(records)

    return df


# =============================================================================
# VALIDACIONES
# =============================================================================

def validate_dataset(df: pd.DataFrame) -> None:
    """
    Ejecuta validaciones críticas.
    """

    logger.info("Validando dataset...")

    validations = [
        df["asistencia_pct"].between(0, 100).all(),
        df["materias_suspensas"].between(0, 10).all(),
        df["numero_materias_curso"].between(10, 14).all(),
        df["evaluaciones_realizadas"].between(0, 4).all(),
        df["partes_disciplinarios"].between(0, 10).all(),
        df["dias_sin_actividad"].between(1, 65).all(),
        df["inasistencias_consecutivas"].between(1, 65).all(),
        df["distancia_escuela"].between(1, 50).all()
    ]

    if not all(validations):
        raise ValueError(
            "El dataset contiene valores fuera de rango."
        )

    logger.info("Validación completada correctamente.")


# =============================================================================
# EXPORTACIÓN
# =============================================================================

def export_dataset(
    df: pd.DataFrame,
    output_path: Path,
    filename: str
) -> Path:
    """
    Exporta dataset CSV.
    """

    output_path.mkdir(
        parents=True,
        exist_ok=True
    )

    csv_path = output_path / filename

    df.to_csv(
        csv_path,
        index=False,
        encoding="utf-8"
    )

    logger.info(f"Dataset exportado: {csv_path}")

    return csv_path


# =============================================================================
# DOCUMENTACIÓN
# =============================================================================

def generate_readme(
    output_path: Path,
    df: pd.DataFrame
) -> None:
    """
    Genera README automático.
    """

    dropout_pct = round(
        df["abandono_escolar"].mean() * 100,
        2
    )

    content = f"""
===============================================================================
DATASET SINTÉTICO - ABANDONO ESCOLAR
===============================================================================

Fecha generación:
{datetime.now()}

Total registros:
{len(df)}

Porcentaje abandono:
{dropout_pct}%

Descripción:
----------------------------------------------------------------------------
Dataset sintético orientado al entrenamiento de modelos de IA
para detección de abandono escolar.

Reglas:
----------------------------------------------------------------------------
R1:
matricula_activa == 0

R2:
dias_sin_actividad >= 60
AND asistencia_pct < 20

R3:
evaluaciones_realizadas == 0
AND asistencia_pct < 30
AND (
    nota_media is null
    OR nota_media < 3
)

Formato:
----------------------------------------------------------------------------
CSV UTF-8 separado por comas.

===============================================================================
"""

    readme_path = output_path / "README_datasets.txt"

    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(content)

    logger.info("README_datasets generado.")


def generate_data_dictionary(output_path: Path) -> None:
    """
    Genera diccionario de datos.
    """

    dictionary = [
        ["asistencia_pct", "float", "Porcentaje asistencia"],
        ["nota_media", "float", "Promedio académico"],
        ["materias_suspensas", "int", "Asignaturas suspendidas"],
        ["numero_materias_curso", "int", "Total asignaturas"],
        ["evaluaciones_realizadas", "int", "Evaluaciones realizadas"],
        ["partes_disciplinarios", "int", "Amonestaciones"],
        ["matricula_activa", "bool", "Matrícula activa"],
        ["oferta_educativa", "int", "Oferta educativa"],
        ["repetidor_curso_actual", "bool", "Alumno repetidor"],
        ["dias_sin_actividad", "int", "Días sin actividad"],
        ["inasistencias_consecutivas", "int", "Faltas consecutivas"],
        ["grado_urbanizacion", "int", "Urbanización"],
        ["distancia_escuela", "float", "Distancia escuela"],
        ["acceso_internet", "bool", "Acceso internet"],
        ["nivel_socioeconomico", "int", "Nivel socioeconómico"],
        ["apoyo_familiar", "bool", "Apoyo familiar"],
        ["trabaja", "bool", "Alumno trabaja"],
        ["abandono_escolar", "bool", "Variable objetivo"]
    ]

    df_dictionary = pd.DataFrame(
        dictionary,
        columns=[
            "variable",
            "tipo",
            "descripcion"
        ]
    )

    path = output_path / "diccionario_datos.csv"

    df_dictionary.to_csv(
        path,
        index=False,
        encoding="utf-8"
    )

    logger.info("Diccionario de datos generado.")


def generate_statistics(
    output_path: Path,
    df: pd.DataFrame
) -> None:
    """
    Genera estadísticas descriptivas.
    """

    stats = df.describe(include="all").transpose()

    stats["null_values"] = df.isnull().sum()

    stats["null_percentage"] = (
        df.isnull().mean() * 100
    )

    path = output_path / "estadisticas_dataset.csv"

    stats.to_csv(
        path,
        encoding="utf-8"
    )

    logger.info("Estadísticas generadas.")


# =============================================================================
# CLI
# =============================================================================

def parse_arguments() -> DatasetConfig:
    """
    Parser CLI profesional.
    """

    parser = argparse.ArgumentParser(
        description="Generador Dataset Abandono Escolar"
    )

    parser.add_argument(
        "--rows",
        type=int,
        default=DEFAULT_ROWS,
        help="Número registros"
    )

    parser.add_argument(
        "--output",
        type=str,
        default="./output_datasets",
        help="Directorio salida"
    )

    default_filename = (
        f"abandono_escolar_"
        f"{datetime.now().strftime('%Y%m%d')}.csv"
    )

    parser.add_argument(
        "--file",
        type=str,
        default=default_filename,
        help="Nombre archivo CSV"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help="Seed reproducibilidad"
    )

    args = parser.parse_args()

    if args.rows <= 0:
        raise ValueError(
            "El número de filas debe ser mayor que cero."
        )

    return DatasetConfig(
        rows=args.rows,
        output_path=Path(args.output),
        filename=ensure_csv_extension(args.file),
        seed=args.seed
    )


# =============================================================================
# MAIN
# =============================================================================

def main() -> None:
    """
    Punto entrada principal.
    """

    start_time = time.time()

    try:

        logger.info("INICIO GENERACIÓN DATASET")

        config = parse_arguments()

        configure_seed(config.seed)

        # ---------------------------------------------------------------------
        # GENERACIÓN
        # ---------------------------------------------------------------------

        df = generate_dataset(config.rows)

        # ---------------------------------------------------------------------
        # VALIDACIÓN
        # ---------------------------------------------------------------------

        validate_dataset(df)

        # ---------------------------------------------------------------------
        # EXPORTACIÓN
        # ---------------------------------------------------------------------

        csv_path = export_dataset(
            df=df,
            output_path=config.output_path,
            filename=config.filename
        )

        # ---------------------------------------------------------------------
        # DOCUMENTACIÓN
        # ---------------------------------------------------------------------

        generate_readme(
            config.output_path,
            df
        )

        generate_data_dictionary(
            config.output_path
        )

        generate_statistics(
            config.output_path,
            df
        )

        # ---------------------------------------------------------------------
        # MÉTRICAS
        # ---------------------------------------------------------------------

        dropout_pct = round(
            df["abandono_escolar"].mean() * 100,
            2
        )

        elapsed = round(
            time.time() - start_time,
            2
        )

        logger.info("================================================")
        logger.info("GENERACIÓN COMPLETADA")
        logger.info("================================================")
        logger.info(f"Archivo: {csv_path}")
        logger.info(f"Registros: {len(df)}")
        logger.info(f"Abandono: {dropout_pct}%")
        logger.info(f"Tiempo: {elapsed}s")
        logger.info("================================================")

    except Exception as error:

        logger.exception(
            f"ERROR CRÍTICO: {error}"
        )

        sys.exit(1)


# =============================================================================
# ENTRYPOINT
# =============================================================================

if __name__ == "__main__":
    main()