# Modelo Operativo — Predicción de Abandono Escolar

# Descripción General

Este documento define el modelo operativo funcional del sistema de predicción de abandono escolar.

El objetivo es establecer:

- definición operativa del abandono,
- reglas de etiquetado,
- criterios de validación,
- construcción del índice de riesgo,
- y flujo de procesamiento de datos.

El modelo separa claramente:

- abandono confirmado (`ground truth`),
- y vulnerabilidad futura (`RiskIndex`).

Esto permite construir un sistema:

- interpretable,
- reproducible,
- escalable,
- y alineado con criterios educativos.

---

# Objetivo del Sistema

Construir un sistema capaz de:

1. Detectar abandono escolar confirmado.
2. Estimar riesgo futuro de abandono.
3. Priorizar intervenciones institucionales.
4. Facilitar dashboards y seguimiento educativo.

---

# Definición Operativa de Abandono Escolar

Se considera abandono escolar:

> Estudiante que interrumpe su trayectoria educativa durante el curso académico sin actividad académica verificable durante un periodo prolongado.

---

# Variables Necesarias

## Variables Académicas

| Variable | Tipo | Descripción |
|---|---|---|
| asistencia_pct | entero | Porcentaje de asistencia |
| nota_media | decimal | Promedio académico sobre 10 |
| materias_suspensas | entero | Número de asignaturas no aprobadas |
| numero_materias_curso | entero | Número total de asignaturas |
| evaluaciones_realizadas | entero | Número de evaluaciones realizadas |
| partes_disciplinarios | entero | Número de incidencias disciplinarias |

---

## Variables Administrativas

| Variable | Tipo | Descripción |
|---|---|---|
| matricula_activa | booleano | 1 = sí, 0 = no |
| oferta_educativa | categórica ordinal | 1 ESO, 2 Bachillerato, 3 FP Básica, 4 FP Medio |
| repetidor_curso_actual | booleano | Indica repetición del curso |

---

## Variables Temporales

| Variable | Tipo | Descripción |
|---|---|---|
| dias_sin_actividad | entero | Días sin actividad educativa |
| inasistencias_consecutivas | entero | Faltas continuadas |

---

## Variables Demográficas

| Variable | Tipo | Descripción |
|---|---|---|
| grado_urbanizacion | categórica ordinal | 1 Rural, 2 Semiurbano, 3 Urbano |

---

## Variables Socioeducativas

| Variable | Tipo | Descripción |
|---|---|---|
| distancia_escuela | decimal | Distancia al centro educativo |
| acceso_internet | booleano | Disponibilidad de internet |
| nivel_socioeconomico | ordinal | Escala social de 1 a 6 |
| apoyo_familiar | booleano | Existencia de apoyo familiar |
| trabaja | booleano | Compatibiliza estudios y trabajo |

---

# Ground Truth — Etiquetado de Abandono

La variable objetivo es:

```text
abandono_escolar
```

Valores:

```text
1 → abandono confirmado
0 → no abandono confirmado
```

---

# Reglas de Etiquetado

## R1 — Abandono Administrativo

```text
matricula_activa == 0
```

---

## R2 — Inactividad Crítica

```text
dias_sin_actividad >= 60
AND asistencia_pct < 20
```

---

## R3 — Desvinculación Académica Severa

```text
evaluaciones_realizadas == 0
AND asistencia_pct < 30
AND (nota_media IS NULL OR nota_media < 3)
```

---

# Regla de Estabilidad

Un estudiante se considera estable si:

```text
matricula_activa == 1
AND asistencia_pct >= 75
AND evaluaciones_realizadas > 0
```

---

# Zona Intermedia

Los siguientes casos no se consideran abandono confirmado:

- asistencia entre 30% y 75%,
- bajo rendimiento sin desconexión total,
- asistencia irregular con actividad académica.

Estos casos:

- se etiquetan como `0`,
- o pueden excluirse del entrenamiento.

---

# Casos Límite

## Caso 1 — Baja Asistencia con Actividad

```text
asistencia = 40%
evaluaciones_realizadas > 0
```

Resultado:

```text
No abandono
Sí riesgo
```

---

## Caso 2 — Notas Ausentes

Si:

```text
nota_media = NULL
```

Entonces:

- utilizar asistencia,
- actividad,
- y permanencia.

---

## Caso 3 — Abandono Tardío

Si:

```text
dias_sin_actividad >= 60
```

al final del periodo académico:

```text
abandono = 1
```

---

# Separación Conceptual

## Ground Truth

Confirma abandono real.

---

## RiskIndex

Estima vulnerabilidad futura.

---

# Objetivos de la Separación

Evitar:

- contaminación del target,
- fuga semántica,
- problemas interpretativos,
- mezcla entre scoring y clasificación.

---

# Gestión de Missing Values

## Variables Críticas

Si faltan:

- asistencia,
- matrícula,
- actividad,

el registro debe:

- excluirse,
- o marcarse como inválido.

---

## Variables Numéricas

Política:

```text
Imputación por mediana agrupada por oferta educativa
```

---

## Variables Binarias

Se añade categoría auxiliar:

```text
variable_missing
```

Ejemplo:

```text
internet_missing
```

---

# RiskIndex — Índice de Riesgo

## Objetivo

Construir un índice continuo:

```text
0 → riesgo mínimo
1 → riesgo máximo
```

---

# Principios del Índice

El índice debe:

## Penalizar

- baja asistencia,
- bajo rendimiento,
- desconexión académica,
- vulnerabilidad socioeconómica.

---

## Incrementar riesgo cuando

- trabaja,
- no tiene internet,
- no tiene apoyo familiar,
- vive lejos.

---

# Normalización de Variables

Todas las variables deben:

- mantener dirección semántica coherente,
- estar normalizadas en `[0,1]`,
- tener impacto comparable.

---

# Variables de Riesgo

## Riesgo por Asistencia

```text
R_asistencia = 1 - (asistencia_pct / 100)
```

---

## Riesgo por Notas

```text
R_notas = 1 - (nota_media / 10)
```

---

## Riesgo por Suspensas

```text
R_suspensas = materias_suspensas / numero_materias_curso
```

---

## Riesgo por Inactividad

```text
R_inactividad = min(dias_sin_actividad / 30, 1)
```

---

## Riesgo por Distancia

Umbral según urbanización:

| Zona | Umbral |
|---|---|
| Urbana | 10 km |
| Semiurbana | 20 km |
| Rural | 40 km |

Fórmula:

```text
R_distancia = min(distancia_escuela / umbral_zona, 1)
```

---

## Riesgo por Internet

```text
1 → no tiene internet
0 → sí tiene internet
```

---

## Riesgo por Apoyo Familiar

```text
1 → no tiene apoyo
0 → sí tiene apoyo
```

---

## Riesgo por Trabajo

```text
1 → trabaja
0 → no trabaja
```

---

## Riesgo Socioeconómico

```text
R_socioeco = (nivel_socioeconomico - 1) / 5
```

---

## Riesgo por Oferta Educativa

| Oferta | Riesgo |
|---|---|
| ESO | 0.3 |
| Bachillerato | 0.2 |
| FP Básica | 0.8 |
| FP Medio | 0.5 |

---

# Ponderación del RiskIndex

| Variable | Peso |
|---|---|
| asistencia_pct | 0.22 |
| dias_sin_actividad | 0.18 |
| nota_media | 0.12 |
| materias_suspensas | 0.08 |
| nivel_socioeconomico | 0.12 |
| acceso_internet | 0.05 |
| apoyo_familiar | 0.08 |
| trabaja | 0.07 |
| distancia_escuela | 0.05 |
| oferta_educativa | 0.03 |

---

# Fórmula Final del RiskIndex

```text
RiskIndex =
0.22 * R_asistencia +
0.18 * R_inactividad +
0.12 * R_notas +
0.08 * R_suspensas +
0.12 * R_socioeco +
0.08 * R_familia +
0.07 * R_trabajo +
0.05 * R_internet +
0.05 * R_distancia +
0.03 * R_oferta
```

Finalmente:

```text
RiskIndex = min(RiskIndex, 1)
```

---

# Clasificación Operativa

| Rango | Nivel |
|---|---|
| 0.00 – 0.29 | Bajo |
| 0.30 – 0.49 | Medio |
| 0.50 – 0.69 | Alto |
| ≥ 0.70 | Crítico |

---

# Objetivos Operativos

La clasificación permite:

- dashboards institucionales,
- alertas tempranas,
- priorización educativa,
- seguimiento longitudinal,
- derivación a intervención.

---

# Flujo Operativo del Sistema

```text
Carga Dataset
      ↓
Validación estructural
      ↓
Tipado y limpieza
      ↓
Gestión de missing values
      ↓
Generación de abandono_escolar
      ↓
Generación de variables riesgo
      ↓
Cálculo RiskIndex
      ↓
Split Train/Test
      ↓
Pipeline ML
      ↓
Entrenamiento
      ↓
Evaluación
      ↓
Visualización
      ↓
Resultados
```

---

# Principios Técnicos del Modelo

## Separación entre clasificación y scoring

El sistema distingue:

- abandono confirmado,
- y riesgo futuro.

---

## Prevención de Data Leakage

Las transformaciones:

- imputación,
- escalado,
- encoding,

se ajustan únicamente sobre entrenamiento.

---

## Interpretabilidad

Se prioriza:

- trazabilidad,
- interpretación educativa,
- explicabilidad institucional.

---

# Evolución Futura

## Mejoras Técnicas

- Cross-validation
- SHAP values
- Feature selection
- Random Forest
- XGBoost
- APIs REST
- MLOps

---

# Conclusión

El modelo operativo define una arquitectura educativa y analítica coherente para:

- detectar abandono,
- estimar vulnerabilidad,
- y priorizar intervenciones preventivas.

La separación entre reglas de negocio y modelado estadístico permite construir un sistema:

- mantenible,