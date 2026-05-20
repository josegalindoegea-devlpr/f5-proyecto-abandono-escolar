
===============================================================================
DATASET SINTÉTICO - ABANDONO ESCOLAR
===============================================================================

Fecha generación:
2026-05-20 20:30:24.823159

Total registros:
1000

Porcentaje abandono:
11.3%

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
