# Predicción de Abandono Escolar con Machine Learning

## Descripción del Proyecto

Este proyecto utiliza técnicas de Machine Learning para predecir el riesgo de abandono escolar en estudiantes, considerando factores relacionados con educación y pobreza.

El objetivo principal es desarrollar un modelo de clasificación binaria que identifique si un estudiante:

- `0 → No abandona`
- `1 → Riesgo de abandono`

El modelo seleccionado es:

- Logistic Regression

Este enfoque permite interpretar fácilmente cuáles variables influyen más en el riesgo de deserción escolar.

---

# Objetivos

## Objetivo General

Desarrollar un sistema predictivo que ayude a identificar estudiantes con riesgo de abandono escolar.

## Objetivos Específicos

- Analizar variables socioeconómicas y académicas.
- Entrenar un modelo de clasificación binaria.
- Evaluar el rendimiento mediante una matriz de confusión.
- Interpretar el impacto social del modelo.
- Proponer intervenciones tempranas para reducir la deserción escolar.

---

# Variables del Modelo

Las principales variables utilizadas son:

| Variable | Descripción |
|---|---|
| distancia_escuela | Distancia entre casa y escuela |
| acceso_internet | Disponibilidad de internet |
| nivel_socioeconomico | Nivel económico familiar |
| nota_media | Rendimiento académico |
| asistencia_pct | Porcentaje de asistencia |
| apoyo_familiar | Apoyo académico y emocional |
| trabaja | Si el estudiante trabaja |
| materias_suspensas | asignaturas no aprobadas |
| numero_materias_curso | asignaturas totales del curso |
| evaluaciones_realizadas | total evaluaciones hechas al alumno |
| partes_disciplinarios | total de amonestaciones durante el curso |
| matricula_activa | indicador de que está matriculado en curso |
| oferta_educativa | diferentes tramos educativos |
| repetidor_curso_actual | indicador si repite el curso |
| dias_sin_actividad | total dias sin registro educativo |
| inasistencias_consecutivas | número de faltas seguidas |
| grado_urbanizacion | rango de urbanización aplicable |ø
| abandono | Variable objetivo |

---

# Tecnologías Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

# Estructura del Proyecto

```text
proyecto_abandono_escolar/
│
├─ data/
│   └─ estudiantes.csv
|
├─datasets/
│   └─abandono.csv
│
├── notebooks/
│   └── analisis.ipynb
│
├── src/
│   ├─preprocessing.py
│   ├── model.py
│  └── visualization.py
│
├── outputs/
│   ├── matriz_confusion.png
│   └── reporte_modelo.txt
│
├─docs/
│
├─ prompts/
│
├── requirements.txt
└── README.md
---
