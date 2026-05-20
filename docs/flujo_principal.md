# Flujo Principal del Modelo Predictivo de Abandono Escolar

## Descripción General

El flujo principal del proyecto describe el proceso completo desde la carga de datos hasta la predicción del riesgo de abandono escolar utilizando un modelo de Machine Learning basado en Logistic Regression.

El objetivo es transformar datos educativos y socioeconómicos en información útil para detectar estudiantes vulnerables de manera temprana.

---

# Flujo General del Sistema

```text
Inicio
   │
   ▼
Carga del Dataset
   │
   ▼
# Fase de Validacion, limpieza y preparación de datos.
   │
   ▼
Validación estructural
   │
   ▼
Tipado y limpieza
   │
   ▼
Gestión de missing values
   │
   ▼   
Ground Truth (abandono_escolar)
   │
   ▼
# Fase de Preparación de datos
   │
   ▼
Ingeniería de variables
   │
   ▼
Calculo RiskIndex
   │
   ▼
Transformación ML
   │
   ▼
# Fase de División de Datos (Train/Test) y entrenamiento
   │
   ▼
Division de datos
   │
   ▼
Adecuación y Escalado de Variables
   │
   ▼
Entrenamiento del Modelo
   │
   ▼
# Fase de Predicción
   │
   ▼
Evaluación del Modelo
   │
   ▼
Generación de Matriz de Confusión
   │
   ▼
Visualización
   │
   ▼
Análisis de Resultados
   │
   ▼
Identificación de Estudiantes en Riesgo
   │
   ▼
Fin
```
---
