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

- reglas operativas,
- procesamiento de datos,
- cálculo de riesgo,
- entrenamiento de modelos,
- evaluación,
- y visualización.

Esto permite evolucionar el sistema desde un MVP académico hacia una plataforma institucional de analítica educativa.

---

# Objetivos Arquitectónicos

La arquitectura propuesta busca:

## Objetivos funcionales

- Detectar abandono escolar confirmado.
- Estimar vulnerabilidad futura.
- Priorizar intervenciones educativas.
- Facilitar análisis institucional.

---

## Objetivos técnicos

- Evitar acoplamiento excesivo.
- Permitir evolución incremental.
- Facilitar testing.
- Garantizar reproducibilidad.
- Prevenir data leakage.
- Mantener interpretabilidad.

---

# Principios de Diseño

# 1. Separación de Responsabilidades

Cada módulo tiene una responsabilidad única.

---

# 2. Arquitectura Modular

Los componentes pueden evolucionar de forma independiente.

---

# 3. Reproducibilidad

Todo el pipeline debe producir resultados consistentes.

---

# 4. Escalabilidad

La solución debe crecer hacia:

- APIs,
- dashboards,
- pipelines automáticos,
- y MLOps.

---

# 5. Interpretabilidad

El sistema prioriza modelos explicables para contexto educativo.

---

# Arquitectura General del Sistema

```text
Dataset Educativo
        ↓
Validación Estructural
        ↓
Preprocessing Avanzado
        ↓
Ground Truth
(abandono_escolar)
        ↓
Variables de Riesgo
        ↓
RiskIndex
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

# Arquitectura Física del Proyecto

```text
proyecto_abandono_escolar/
│
├── data/
│   └── estudiantes.csv
│
├─datasets/
│   └─abandono.csv
│
├── notebooks/
│   └── analisis_exploratorio.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── risk_index.py
│   ├── labeling.py
│   ├── model.py
│   ├── evaluation.py
│   ├── visualization.py
│   ├── config.py
│   ├── utils.py
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

# Componentes Arquitectónicos

# 1. Data Layer

## Responsabilidad

Gestionar:

- carga de datos,
- validación estructural,
- control de integridad.

---

## Entradas

```text
CSV institucional
```

---

## Validaciones

- columnas requeridas,
- tipos de datos,
- rangos válidos,
- registros críticos faltantes.

---

# 2. Preprocessing Layer

## Responsabilidad

Transformar datos brutos en datos utilizables para ML.

---

## Funcionalidades

- tipado,
- limpieza,
- imputación,
- generación de variables,
- normalización,
- encoding,
- pipelines reproducibles.

---

## Principios

- sin data leakage,
- reproducibilidad,
- trazabilidad.

---

# 3. Ground Truth Layer

## Responsabilidad

Construir:

```text
abandono_escolar
```

mediante reglas operativas.

---

## Reglas Implementadas

### R1 — Abandono administrativo

```text
matricula_activa == 0
```

---

### R2 — Inactividad crítica

```text
dias_sin_actividad >= 60
AND asistencia_pct < 20
```

---

### R3 — Desvinculación severa

```text
evaluaciones_realizadas == 0
AND asistencia_pct < 30
AND nota_media < 3
```

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
- dirección semántica coherente,
- ponderación institucional,
- interpretabilidad.

---

## Variables utilizadas

- asistencia,
- inactividad,
- notas,
- suspensas,
- NSE,
- internet,
- familia,
- trabajo,
- distancia,
- oferta educativa.

---

# 5. Machine Learning Layer

## Responsabilidad

Entrenar y evaluar modelos predictivos.

---

## MVP Actual

```text
Logistic Regression
```

---

## Motivos de selección

- interpretabilidad,
- robustez,
- simplicidad,
- explicabilidad institucional.

---

## Evolución futura

- Random Forest,
- XGBoost,
- ensemble methods.

---

# 6. Evaluation Layer

## Responsabilidad

Medir rendimiento del sistema.

---

## Métricas principales

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

para evitar estudiantes vulnerables no detectados.

---

# 7. Visualization Layer

## Responsabilidad

Facilitar interpretación visual.

---

## Visualizaciones

- matriz de confusión,
- importancia de variables,
- distribución de riesgo,
- segmentación institucional.

---

# 8. Documentation Layer

## Responsabilidad

Garantizar:

- trazabilidad,
- gobernanza técnica,
- mantenibilidad,
- transferencia de conocimiento.

---

# Flujo Operativo Completo

```text
Carga CSV
    ↓
Validación estructural
    ↓
Limpieza y tipado
    ↓
Gestión de missing values
    ↓
Generación abandono_escolar
    ↓
Generación variables riesgo
    ↓
Cálculo RiskIndex
    ↓
Train/Test Split
    ↓
Pipeline ML
    ↓
Entrenamiento modelo
    ↓
Predicciones
    ↓
Evaluación
    ↓
Visualización
    ↓
Resultados institucionales
```

---

# Diseño del Pipeline ML

# Objetivos

Garantizar:

- reproducibilidad,
- ausencia de leakage,
- consistencia estadística.

---

# Componentes

## Split

```text
80% train
20% test
```

---

## Imputación

- mediana por oferta educativa,
- variables auxiliares missing.

---

## Escalado

```text
StandardScaler
```

aplicado únicamente sobre entrenamiento.

---

## Encoding

```text
OneHotEncoder
```

para variables categóricas.

---

# Prevención de Data Leakage

Todas las transformaciones:

- imputación,
- escalado,
- encoding,

se ajustan exclusivamente sobre train.

---

# Arquitectura de Riesgo

# Separación conceptual

## Ground Truth

Confirma abandono real.

---

## RiskIndex

Estima vulnerabilidad futura.

---

# Beneficios

Evita:

- contaminación del target,
- confusión semántica,
- mezcla entre scoring y clasificación.

---

# Gestión de Missing Values

# Variables críticas

Si faltan:

- asistencia,
- matrícula,
- actividad,

el registro:

- se excluye,
- o se marca inválido.

---

# Variables numéricas

```text
Imputación mediana por oferta educativa
```

---

# Variables binarias

Creación de:

```text
variable_missing
```

---

# Escalabilidad Técnica

# Evolución prevista

## Corto plazo

- logging,
- persistencia modelos,
- métricas avanzadas.

---

## Medio plazo

- cross-validation,
- SHAP values,
- balanceo de clases,
- feature selection.

---

## Largo plazo

- FastAPI,
- dashboards institucionales,
- ETL automatizado,
- monitorización,
- MLOps.

---

# Gobernanza Técnica

# Documentación centralizada

La solución incorpora:

- arquitectura,
- métricas,
- decisiones técnicas,
- backlog,
- historias de usuario,
- modelo operativo.

---

# Beneficios Institucionales

La arquitectura permite:

- detección temprana,
- priorización educativa,
- seguimiento longitudinal,
- análisis institucional,
- soporte preventivo.

---

# Beneficios Técnicos

| Característica | Beneficio |
|---|---|
| Modularidad | Evolución independiente |
| Reproducibilidad | Resultados consistentes |
| Interpretabilidad | Explicación institucional |
| Escalabilidad | Evolución futura |
| Testing | Validación aislada |
| Mantenibilidad | Menor complejidad |

---

# Riesgos Identificados

# Riesgo de Sesgo

Variables socioeconómicas pueden introducir:

- correlaciones espurias,
- discriminación indirecta.

---

# Mitigaciones

- auditorías,
- explicabilidad,
- revisión institucional,
- fairness metrics futuras.

---

# Resultado Esperado del MVP

Al finalizar el MVP:

- dataset validado,
- preprocessing avanzado,
- etiquetado automático,
- RiskIndex funcional,
- modelo entrenado,
- métricas calculadas,
- visualizaciones generadas,
- documentación completa,
- arquitectura reproducible.

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

La combinación entre:

- reglas operativas,
- ingeniería de datos,
- scoring de riesgo,
- Machine Learning,
- y documentación técnica,

permite desarrollar una solución:

- mantenible,
- escalable,
- interpretable,
- y alineada con necesidades educativas reales.

