# Product Backlog — Proyecto Predicción de Abandono Escolar

# Descripción General

Este documento define el Product Backlog oficial del proyecto:

## Sistema Predictivo de Riesgo de Abandono Escolar mediante Machine Learning

El backlog organiza:

- épicas funcionales,
- iniciativas técnicas,
- evolución del pipeline ML,
- calidad de datos,
- despliegue,
- y capacidades futuras del sistema.

La estructura está alineada con:

- arquitectura modular,
- modelo operativo,
- historias de usuario v2,
- roadmap técnico,
- y estrategia de escalabilidad.

---

# Objetivos Estratégicos

El sistema busca:

- detectar riesgo de abandono escolar,
- construir un ground truth reproducible,
- generar un índice continuo de vulnerabilidad,
- facilitar intervención educativa temprana,
- y evolucionar hacia una plataforma institucional escalable.

---

# Estados del Backlog

| Estado | Descripción |
|---|---|
| Pendiente | No iniciado |
| En progreso | Actualmente en desarrollo |
| Completado | Implementado y validado |
| Bloqueado | Requiere dependencias |

---

# Priorización

| Prioridad | Significado |
|---|---|
| Alta | Crítico para MVP |
| Media | Importante para evolución |
| Baja | Evolución futura |

---

# EPIC 1 — Arquitectura y Base del Proyecto

## Objetivo

Construir una base técnica modular, mantenible y preparada para evolución futura.

| ID | Elemento | Descripción | Prioridad | Estado |
|---|---|---|---|---|
| PB-001 | Estructura modular definitiva | Consolidar separación por módulos (`preprocessing`, `model`, `visualization`, `main`) | Alta | Pendiente |
| PB-002 | Archivo de configuración global | Centralizar parámetros técnicos y operativos (`config.py`) | Alta | Pendiente |
| PB-003 | Logging estructurado | Implementar sistema de logs para trazabilidad y debugging | Alta | Pendiente |

## PB-001 — Estructura modular definitiva
### Descripción

Estandarizar estructura de carpetas y módulos.

### Prioridad

Alta

### Estado

Pendiente

### Criterios de aceptación
Separación clara de responsabilidades
Carpetas organizadas
Imports consistentes
Proyecto ejecutable desde main.py

## PB-002 — Archivo de configuración global
### Descripción

Centralizar constantes y parámetros del sistema.

### Prioridad

Alta

### Estado

Pendiente

### Entregables
config.py
Incluir
umbrales,
pesos,
rutas,
parámetros del modelo,
semillas aleatorias.

## PB-003 — Logging estructurado
### Descripción

Implementar logging profesional.

### Prioridad

Alta

### Estado

Pendiente

### Criterios
Logs INFO/WARNING/ERROR
Persistencia en archivo
Trazabilidad del pipeline
---

# EPIC 2 — Calidad y Validación del Dataset

## Objetivo

Garantizar calidad estructural, consistencia estadística y robustez del dataset.

| ID | Elemento | Descripción | Prioridad | Estado |
|---|---|---|---|---|
| PB-004 | Validación estructural del dataset | Verificar columnas requeridas y consistencia general | Alta | En progreso |
| PB-005 | Validación de rangos | Validar límites operativos y coherencia matemática | Alta | Pendiente |
| PB-006 | Gestión avanzada de missing values | Imputación diferenciada según tipo de variable | Alta | Pendiente |
| PB-007 | Tipado automático de variables | Conversión y validación automática de tipos | Media | Pendiente |

## PB-004 — Validación estructural del dataset
### Descripción

Verificar columnas obligatorias y dataset vacío.

### Prioridad

Alta

### Estado

En progreso

### Validaciones
columnas requeridas,
duplicados,
tipos esperados,
dataset vacío.

## PB-005 — Validación de rangos
### Descripción

Validar coherencia semántica de variables.

### Prioridad

Alta

### Estado

Pendiente

### Reglas
asistencia_pct ∈ [0,100]
nota_media ∈ [0,10]
dias_sin_actividad >= 0

## PB-006 — Gestión avanzada de missing values
### Descripción

Implementar política oficial de imputación.

### Prioridad

Alta

### Estado

Pendiente

### Estrategia
|Tipo	| Estrategia |
|---|---|
| Booleanas	| Categoría auxiliar |
| Numéricas	| Mediana por oferta educativa |
| Variables críticas | Exclusión del registro |

## PB-007 — Tipado automático de variables
### Descripción

Normalizar tipos de datos.

### Prioridad

Media

### Estado

Pendiente
---

# EPIC 3 — Ingeniería de Variables

## Objetivo

Transformar variables educativas en indicadores homogéneos y escalables.

| ID | Elemento | Descripción | Prioridad | Estado |
|---|---|---|---|---|
| PB-008 | Generación de variables de riesgo | Construcción de variables normalizadas en rango [0,1] | Alta | Pendiente |
| PB-009 | Implementación del RiskIndex | Construcción del índice ponderado de vulnerabilidad | Alta | Pendiente |
| PB-010 | Clasificación operativa del riesgo | Etiquetado Bajo/Medio/Alto/Crítico | Media | Pendiente |

## PB-008 — Generación de variables de riesgo

### Descripción

Implementar cálculo normalizado de riesgos.

### Prioridad

Alta

### Estado

Pendiente

### Variables
R_asistencia
R_notas
R_suspensas
R_inactividad
R_distancia
R_socioeco
R_internet
R_familia
R_trabajo
R_oferta

## PB-009 — Implementación del RiskIndex
### Descripción

Construir índice final ponderado.

### Prioridad

Alta

### Estado

Pendiente

### Restricciones
rango [0,1]
pesos suman 1.00
coherencia semántica

## PB-010 — Clasificación operativa del riesgo
### Descripción

Crear niveles interpretables.

### Prioridad

Media

### Estado

Pendiente

### Niveles
|Rango | Nivel |
|---|---|
| 0.00–0.29	| Bajo |
| 0.30–0.49	| Medio |
| 0.50–0.69	| Alto|
| ≥0.70	| Crítico |


---

# EPIC 4 — Ground Truth y Etiquetado

## Objetivo

Construir una variable objetivo consistente, reproducible y alineada con el modelo operativo.

| ID | Elemento | Descripción | Prioridad | Estado |
|---|---|---|---|---|
| PB-011 | Implementación automática de reglas de abandono | Construcción de `abandono_escolar` mediante reglas R1-R3 | Alta | Pendiente |
| PB-012 | Gestión de Edge Cases | Tratamiento de casos límite y ambigüedades | Media | Pendiente |

## PB-011 — Implementación automática de reglas de abandono
### Descripción

Generar abandono_escolar.

### Prioridad

Alta

### Estado

Pendiente

### Reglas
abandono administrativo,
inactividad crítica,
desvinculación severa.

## PB-012 — Gestión de edge cases
### Descripción

Controlar casos ambiguos.

## Prioridad

Media

### Estado

Pendiente

### Casos
notas nulas,
asistencia media,
abandono tardío.
---

# EPIC 5 — Machine Learning

## Objetivo

Construir el pipeline predictivo principal y mejorar progresivamente el rendimiento.

| ID | Elemento | Descripción | Prioridad | Estado |
|---|---|---|---|---|
| PB-013 | Pipeline ML integrado | Pipeline reproducible sin data leakage | Alta | Pendiente |
| PB-014 | Entrenamiento baseline | Modelo inicial Logistic Regression | Alta | En progreso |
| PB-015 | Métricas avanzadas | Precision, Recall, F1, ROC-AUC | Alta | Pendiente |
| PB-016 | Balanceo de clases | Técnicas SMOTE y control de desbalanceo | Media | Pendiente |
| PB-017 | Cross-validation | Validación robusta del modelo | Media | Pendiente |
| PB-018 | Comparativa de modelos | Random Forest, XGBoost y benchmarking | Media | Pendiente |

## PB-013 — Pipeline ML integrado
### Descripción

Unificar preprocessing + modelo.

### Prioridad

Alta

### Estado

Pendiente

### Tecnología
Pipeline
ColumnTransformer

## PB-014 — Entrenamiento baseline
### Descripción

Entrenar Logistic Regression.

### Prioridad

Alta

### Estado

En progreso

## PB-015 — Métricas avanzadas
### Descripción

Añadir métricas robustas.

### Prioridad

Alta

### Estado

Pendiente

### Métricas
Precision
Recall
F1-score
ROC-AUC

## PB-016 — Balanceo de clases
### Descripción

Gestionar desbalance del target.

### Prioridad

Media

### Estado

Pendiente

### Técnicas
class_weight
SMOTE

## PB-017 — Cross-validation
### Descripción

Validar estabilidad del modelo.

### Prioridad

Media

### Estado

Pendiente

## PB-018 — Comparativa de modelos
### Descripción

Evaluar algoritmos alternativos.

### Prioridad

Media

### Estado

Pendiente

### Modelos
Random Forest
XGBoost
LightGBM
---

# EPIC 6 — Explainability y Analítica

## Objetivo

Facilitar interpretación del modelo y soporte a la toma de decisiones educativas.

| ID | Elemento | Descripción | Prioridad | Estado |
|---|---|---|---|---|
| PB-019 | Importancia de variables | Interpretación de coeficientes e impacto | Alta | En progreso |
| PB-020 | SHAP values | Explainability avanzada basada en contribución individual | Media | Pendiente |
| PB-021 | Dashboard de métricas | Visualización institucional de KPIs | Media | Pendiente |

## PB-019 — Importancia de variables
### Descripción

Visualizar impacto de features.

### Prioridad

Alta

### Estado

En progreso

## PB-020 — SHAP values
### Descripción

Explicabilidad avanzada.

### Prioridad

Media

### Estado

Pendiente

## PB-021 — Dashboard de métricas
### Descripción

Visualización operativa.

### Prioridad

Media

### Estado

Pendiente
---

# EPIC 7 — Persistencia y Despliegue

## Objetivo

Preparar el sistema para inferencia desacoplada y despliegue institucional.

| ID | Elemento | Descripción | Prioridad | Estado |
|---|---|---|---|---|
| PB-022 | Persistencia de modelos | Guardado y carga de modelos (`joblib`) | Alta | Pendiente |
| PB-023 | Inferencia desacoplada | Predicción independiente del entrenamiento | Alta | Pendiente |
| PB-024 | API REST | Exposición del modelo mediante FastAPI | Media | Pendiente |
| PB-025 | Dockerización | Contenerización del sistema | Media | Pendiente |

## PB-022 — Persistencia de modelos
### Descripción

Guardar y cargar modelos entrenados.

### Prioridad

Alta

### Estado

Pendiente

### Tecnología
joblib
pickle

## PB-023 — Inferencia desacoplada
### Descripción

Separar entrenamiento e inferencia.

### Prioridad

Alta

### Estado

Pendiente

## PB-024 — API REST
### Descripción

Exponer predicciones vía API.

### Prioridad

Media

### Estado

Pendiente

###Tecnología
FastAPI

## PB-025 — Dockerización
### Descripción

Empaquetar aplicación.

## Prioridad

Media

## Estado

Pendiente
---

# EPIC 8 — Calidad de Software

## Objetivo

Asegurar mantenibilidad, estabilidad y calidad técnica del código.

| ID | Elemento | Descripción | Prioridad | Estado |
|---|---|---|---|---|
| PB-026 | Tests automáticos | Unit testing y validaciones automáticas | Alta | Pendiente |
| PB-027 | Linting y formateo | Black, Flake8 e isort | Media | Pendiente |
| PB-028 | Documentación técnica | Arquitectura, decisiones y modelo operativo | Alta | En progreso |

## PB-026 — Tests automáticos
### Descripción

Implementar testing unitario.

### Prioridad

Alta

### Estado

Pendiente

### Framework
pytest

## PB-027 — Linting y formateo
### Descripción

Estandarizar calidad de código.

### Prioridad

Media

### Estado

Pendiente

### Herramientas
black
flake8
isort

## PB-028 — Documentación técnica
### Descripción

Actualizar documentación del sistema.

### Prioridad

Alta

### Estado

En progreso
---

# EPIC 9 — MLOps y Operación

## Objetivo

Evolucionar el sistema hacia operación continua y escalabilidad institucional.

| ID | Elemento | Descripción | Prioridad | Estado |
|---|---|---|---|---|
| PB-029 | Versionado de datasets | Trazabilidad de datos y reproducibilidad | Baja | Pendiente |
| PB-030 | Monitorización del modelo | Drift, degradación y métricas operativas | Baja | Pendiente |
| PB-031 | Pipeline ETL automatizado | Automatización ingestión y procesamiento | Baja | Pendiente |

## PB-029 — Versionado de datasets
### Descripción

Control de trazabilidad de datos.

### Prioridad

Baja

### Estado

Pendiente

## PB-030 — Monitorización del modelo
### Descripción

Detectar drift y degradación.

### Prioridad

Baja

### Estado

Pendiente

## PB-031 — Pipeline ETL automatizado
### Descripción

Automatizar ingestión y procesamiento.

### Prioridad

Baja

### Estado

Pendiente
---

# Relación entre Épicas y Arquitectura

| Épica | Módulo principal relacionado |
|---|---|
| EPIC 1 | Arquitectura general |
| EPIC 2 | preprocessing.py |
| EPIC 3 | preprocessing.py |
| EPIC 4 | preprocessing.py |
| EPIC 5 | model.py |
| EPIC 6 | visualization.py |
| EPIC 7 | inference / deployment |
| EPIC 8 | testing / documentación |
| EPIC 9 | operación y MLOps |

---

# Dependencias Técnicas Principales

| Backlog | Dependencia |
|---|---|
| PB-009 | PB-008 |
| PB-011 | PB-004 + PB-005 |
| PB-013 | PB-006 + PB-007 |
| PB-015 | PB-014 |
| PB-018 | PB-017 |
| PB-024 | PB-022 + PB-023 |
| PB-030 | PB-024 |

---

# Roadmap de Implementación

# Fase 1 — MVP Operativo

Incluye:

- validación dataset,
- preprocessing avanzado,
- generación de etiquetas,
- RiskIndex,
- Logistic Regression,
- métricas básicas,
- visualizaciones.

Backlog asociado:

- PB-001 → PB-015

---

# Fase 2 — Robustez Analítica

Incluye:

- explainability,
- SHAP,
- cross-validation,
- balanceo,
- comparativa de modelos.

Backlog asociado:

- PB-016 → PB-021

---

# Fase 3 — Despliegue Institucional

Incluye:

- persistencia,
- inferencia desacoplada,
- API REST,
- dashboard,
- dockerización.

Backlog asociado:

- PB-022 → PB-028

---

# Fase 4 — MLOps y Escalabilidad

Incluye:

- versionado,
- monitorización,
- pipelines automáticos,
- observabilidad.

Backlog asociado:

- PB-029 → PB-031

---

# Resultado Esperado del MVP

Al finalizar el MVP:

- dataset validado,
- pipeline reproducible,
- etiquetas de abandono automatizadas,
- RiskIndex operativo,
- modelo baseline entrenado,
- métricas iniciales disponibles,
- arquitectura modular consolidada,
- documentación técnica completa.

---

# Conclusión

El Product Backlog propuesto organiza el proyecto bajo una estrategia evolutiva y modular.

La división por:

- épicas,
- backlog técnico,
- prioridades,
- y roadmap incremental

permite desarrollar el sistema de forma:

- mantenible,
- escalable,
- reproducible,
- y alineada con buenas prácticas de Machine Learning Engineering y MLOps.
