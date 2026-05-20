# Arquitectura Final Propuesta — Sistema de Predicción de Abandono Escolar

# Resumen Ejecutivo

Este documento describe la arquitectura final propuesta para el sistema de predicción de abandono escolar.

El objetivo de la arquitectura es construir una solución:

- modular,
- escalable,
- mantenible,
- reproducible,
- interpretable,
- y alineada con criterios educativos e institucionales.

La arquitectura separa claramente:

- validación de datos,
- procesamiento,
- generación de etiquetas,
- cálculo de riesgo,
- entrenamiento ML,
- evaluación,
- visualización,
- y orquestación operativa.

Esto permite evolucionar el sistema desde un MVP académico hacia una plataforma institucional de analítica educativa.

---

# Objetivos Arquitectónicos

# Objetivos funcionales

- Detectar abandono escolar confirmado.
- Estimar vulnerabilidad futura.
- Priorizar intervenciones educativas.
- Facilitar análisis institucional.
- Proporcionar interpretabilidad operativa.

---

# Objetivos técnicos

- Evitar acoplamiento excesivo.
- Permitir evolución incremental.
- Facilitar testing.
- Garantizar reproducibilidad.
- Prevenir data leakage.
- Facilitar trazabilidad arquitectónica.
- Separar responsabilidades funcionales.

---

# Principios de Diseño

# 1. Separación de Responsabilidades

Cada módulo posee una única responsabilidad claramente definida.

---

# 2. Arquitectura Modular

Los componentes evolucionan de manera independiente.

---

# 3. Reproducibilidad

Todo el pipeline debe producir resultados consistentes.

---

# 4. Escalabilidad

La solución podrá evolucionar hacia:

- APIs,
- dashboards,
- pipelines automáticos,
- MLOps,
- y monitorización institucional.

---

# 5. Interpretabilidad

El sistema prioriza modelos explicables para contexto educativo.

---

# 6. Trazabilidad Arquitectónica

Cada capa arquitectónica posee correspondencia directa con módulos físicos del proyecto.

---

# Arquitectura General del Sistema

```text
Dataset Educativo
        ↓
Ingestion Layer
        ↓
Preprocessing Layer
        ↓
Ground Truth Layer
        ↓
Risk Engine Layer
        ↓
Feature Engineering Layer
        ↓
Machine Learning Layer
        ↓
Evaluation Layer
        ↓
Visualization Layer
        ↓
Resultados Institucionales
```

---

# Arquitectura Física del Proyecto

```text
proyecto_abandono_escolar/
│
├── data/
│   └── estudiantes.csv
│
├── datasets/
│   └── abandono.csv
│
├── notebooks/
│   └── analisis_exploratorio.ipynb
│
├── src/
│
│   ├── ingestion/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── validator.py
│   │   └── schemas.py
│   │
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   ├── cleaning.py
│   │   ├── imputation.py
│   │   ├── encoding.py
│   │   ├── scaling.py
│   │   └── pipeline.py
│   │
│   ├── labeling/
│   │   ├── __init__.py
│   │   ├── dropout_rules.py
│   │   ├── target_builder.py
│   │   └── validation.py
│   │
│   ├── risk/
│   │   ├── __init__.py
│   │   ├── risk_variables.py
│   │   ├── risk_score.py
│   │   ├── weighting.py
│   │   └── normalization.py
│   │
│   ├── features/
│   │   ├── __init__.py
│   │   ├── feature_engineering.py
│   │   ├── feature_selection.py
│   │   └── feature_registry.py
│   │
│   ├── modeling/
│   │   ├── __init__.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   ├── pipeline.py
│   │   ├── persistence.py
│   │   └── models.py
│   │
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── metrics.py
│   │   ├── confusion.py
│   │   ├── validation.py
│   │   └── reporting.py
│   │
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── plots.py
│   │   ├── dashboards.py
│   │   └── export.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── paths.py
│   │   └── constants.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── helpers.py
│   │   └── decorators.py
│   │
│   ├── pipelines/
│   │   ├── __init__.py
│   │   ├── training_pipeline.py
│   │   ├── inference_pipeline.py
│   │   └── evaluation_pipeline.py
│   │
│   └── main.py
│
├── outputs/
│   ├── reportes/
│   ├── modelos/
│   ├── metricas/
│   └── visualizaciones/
│
├── docs/
│   ├── arquitectura_abandono_escolar.md
│   ├── modelo_operativo_abandono_escolar.md
│   ├── metricas_modelo_abandono_escolar.md
│   ├── decisiones_tecnicas_abandono_escolar.md
│   ├── historias_usuario_abandono_escolar_v2.md
│   ├── comparativa_evolutiva_proyecto_abandono_escolar.md
│   └── product_backlog_abandono_escolar.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Correspondencia entre Capas y Módulos

| Capa Arquitectónica | Directorio | Responsabilidad |
|---|---|---|
| Ingestion Layer | ingestion/ | Carga y validación |
| Preprocessing Layer | preprocessing/ | Transformación de datos |
| Ground Truth Layer | labeling/ | Construcción del target |
| Risk Engine Layer | risk/ | Cálculo de vulnerabilidad |
| Feature Layer | features/ | Ingeniería de variables |
| ML Layer | modeling/ | Entrenamiento e inferencia |
| Evaluation Layer | evaluation/ | Métricas y validación |
| Visualization Layer | visualization/ | Interpretación visual |
| Config Layer | config/ | Configuración global |
| Utility Layer | utils/ | Funciones compartidas |
| Pipeline Layer | pipelines/ | Orquestación |
| Entry Point | main.py | Coordinación global |

---

# Componentes Arquitectónicos

# 1. Ingestion Layer

## Responsabilidad

Gestionar:

- carga de datos,
- validación estructural,
- control de integridad,
- esquemas de entrada.

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| loader.py | Carga CSV |
| validator.py | Validaciones estructurales |
| schemas.py | Esquemas y contratos |

---

# 2. Preprocessing Layer

## Responsabilidad

Transformar datos brutos en datos utilizables para ML.

---

## Funcionalidades

- limpieza,
- imputación,
- encoding,
- escalado,
- normalización,
- pipelines reproducibles.

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| cleaning.py | Limpieza |
| imputation.py | Missing values |
| encoding.py | Variables categóricas |
| scaling.py | Escalado |
| pipeline.py | Pipeline preprocessing |

---

# 3. Ground Truth Layer

## Responsabilidad

Construir:

```text
abandono_escolar
```

mediante reglas operativas.

---

## Reglas

### R1 — Abandono administrativo

```text
matricula_activa == 0
```

### R2 — Inactividad crítica

```text
dias_sin_actividad >= 60
AND asistencia_pct < 20
```

### R3 — Desvinculación severa

```text
evaluaciones_realizadas == 0
AND asistencia_pct < 30
AND nota_media < 3
```

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| dropout_rules.py | Reglas operativas |
| target_builder.py | Construcción target |
| validation.py | Validación etiquetas |

---

# 4. Risk Engine Layer

## Responsabilidad

Calcular:

```text
RiskIndex
```

como índice continuo de vulnerabilidad.

---

## Características

- normalización [0,1],
- ponderación institucional,
- interpretabilidad,
- scoring reproducible.

---

## Variables

- asistencia,
- notas,
- internet,
- NSE,
- trabajo,
- distancia,
- actividad,
- contexto familiar.

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| risk_variables.py | Variables riesgo |
| risk_score.py | Cálculo score |
| weighting.py | Ponderaciones |
| normalization.py | Escalado riesgo |

---

# 5. Feature Engineering Layer

## Responsabilidad

Generar variables derivadas para ML.

---

## Funcionalidades

- ratios,
- agregaciones,
- transformaciones,
- selección de variables.

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| feature_engineering.py | Variables derivadas |
| feature_selection.py | Selección variables |
| feature_registry.py | Catálogo features |

---

# 6. Machine Learning Layer

## Responsabilidad

Entrenar y ejecutar modelos predictivos.

---

## MVP Actual

```text
Logistic Regression
```

---

## Evolución futura

- Random Forest,
- XGBoost,
- ensemble methods.

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| train.py | Entrenamiento |
| predict.py | Inferencia |
| pipeline.py | Pipeline ML |
| persistence.py | Persistencia |
| models.py | Registro modelos |

---

# 7. Evaluation Layer

## Responsabilidad

Medir rendimiento del sistema.

---

## Métricas

- accuracy,
- precision,
- recall,
- F1-score,
- matriz de confusión.

---

## Prioridad institucional

Minimizar:

```text
False Negatives
```

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| metrics.py | Métricas |
| confusion.py | Matriz confusión |
| validation.py | Validación |
| reporting.py | Reportes |

---

# 8. Visualization Layer

## Responsabilidad

Facilitar interpretación visual.

---

## Visualizaciones

- matriz de confusión,
- importancia variables,
- distribución riesgo,
- segmentación institucional.

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| plots.py | Gráficos |
| dashboards.py | Dashboards |
| export.py | Exportaciones |

---

# 9. Pipeline Layer

## Responsabilidad

Coordinar flujos operativos completos.

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| training_pipeline.py | Pipeline entrenamiento |
| inference_pipeline.py | Pipeline inferencia |
| evaluation_pipeline.py | Pipeline evaluación |

---

# 10. Config Layer

## Responsabilidad

Centralizar configuración global.

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| settings.py | Configuración global |
| paths.py | Rutas proyecto |
| constants.py | Constantes |

---

# 11. Utility Layer

## Responsabilidad

Servicios compartidos reutilizables.

---

## Módulos

| Archivo | Responsabilidad |
|---|---|
| logger.py | Logging |
| helpers.py | Funciones auxiliares |
| decorators.py | Decoradores |

---

# 12. main.py

## Responsabilidad

Punto único de entrada del sistema.

---

## Función

Coordinar:

- carga,
- preprocessing,
- labeling,
- risk scoring,
- entrenamiento,
- evaluación,
- visualización.

---

## Restricción Arquitectónica

```text
main.py NO contiene lógica de negocio
```

Solo orquesta ejecución.

---

# Flujo Operativo Completo

```text
Carga Dataset
      ↓
Validación
      ↓
Preprocessing
      ↓
Ground Truth
      ↓
RiskIndex
      ↓
Feature Engineering
      ↓
Train/Test Split
      ↓
Entrenamiento ML
      ↓
Predicción
      ↓
Evaluación
      ↓
Visualización
      ↓
Resultados
```

---

# Prevención de Data Leakage

Todas las operaciones de:

- imputación,
- encoding,
- escalado,
- feature engineering,

se ajustan exclusivamente sobre train.

---

# Escalabilidad Técnica

# Corto plazo

- logging,
- persistencia modelos,
- métricas avanzadas.

---

# Medio plazo

- cross-validation,
- SHAP values,
- balanceo de clases,
- fairness metrics.

---

# Largo plazo

- APIs FastAPI,
- dashboards institucionales,
- pipelines ETL,
- MLOps,
- monitorización.

---

# Beneficios Arquitectónicos

| Característica | Beneficio |
|---|---|
| Modularidad | Evolución independiente |
| Trazabilidad | Relación capa ↔ código |
| Testing | Validación aislada |
| Escalabilidad | Evolución futura |
| Interpretabilidad | Explicación institucional |
| Reproducibilidad | Resultados consistentes |

---

# Resultado Esperado del MVP

Al finalizar el MVP:

- dataset validado,
- preprocessing modular,
- etiquetado automático,
- RiskIndex funcional,
- feature engineering,
- modelo entrenado,
- métricas calculadas,
- visualizaciones generadas,
- pipelines reproducibles,
- documentación técnica completa.

---

# Visión Objetivo

La arquitectura está diseñada para evolucionar desde:

```text
MVP académico
```

hacia:

```text
Plataforma institucional de analítica educativa
```

---

# Conclusión

La arquitectura final propuesta proporciona una base sólida para construir un sistema profesional de predicción de abandono escolar.

La separación clara entre:

- capas,
- responsabilidades,
- pipelines,
- módulos,
- y flujos operativos,

permite desarrollar una solución:

- mantenible,
- escalable,
- reproducible,
- interpretable,
- y alineada con necesidades educativas reales.