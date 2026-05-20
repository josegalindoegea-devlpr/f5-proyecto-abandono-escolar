# Historias de Usuario — Proyecto Predicción de Abandono Escolar (Versión 2.0)

# Descripción General

Este documento redefine las Historias de Usuario del proyecto:

## Sistema Predictivo de Riesgo y Abandono Escolar mediante Machine Learning

La nueva versión reorganiza las épicas y las historias funcionales para alinearlas con:

- el modelo operativo de abandono escolar,
- las reglas de etiquetado (ground truth),
- el cálculo del RiskIndex,
- la ingeniería de variables,
- la arquitectura ML modular,
- la prevención de data leakage,
- y la evolución hacia un entorno productivo.

---

# Objetivos Estratégicos del Proyecto

El sistema busca:

- detectar abandono escolar confirmado,
- calcular vulnerabilidad futura,
- priorizar intervención educativa,
- permitir análisis institucional,
- y construir una plataforma ML escalable.

El modelo distingue explícitamente entre:

| Concepto | Objetivo |
|---|---|
| abandono_escolar | Ground truth supervisado |
| RiskIndex | Vulnerabilidad futura |

---

# Arquitectura Funcional Global

```text
Dataset
   ↓
Validación estructural
   ↓
Limpieza y tipado
   ↓
Gestión de missing values
   ↓
Generación de etiquetas
   ↓
Ingeniería de variables de riesgo
   ↓
Cálculo RiskIndex
   ↓
Pipeline ML
   ↓
Entrenamiento
   ↓
Predicción
   ↓
Evaluación
   ↓
Visualización
   ↓
Interpretación
```

---

# Nueva Organización de Épicas

| ID | Épica | Objetivo |
|---|---|---|
| EP-01 | Gestión y Calidad de Datos | Validar y preparar información educativa |
| EP-02 | Ground Truth y Riesgo | Generar abandono_escolar y RiskIndex |
| EP-03 | Pipeline de Machine Learning | Construir entrenamiento reproducible |
| EP-04 | Evaluación e Interpretabilidad | Analizar comportamiento del modelo |
| EP-05 | Documentación y Gobierno Técnico | Mantener trazabilidad y colaboración |
| EP-06 | Evolución Técnica y Productivización | Escalar arquitectura y despliegue |

---

# EP-01 — Gestión y Calidad de Datos

## Objetivo

Garantizar datasets válidos, consistentes y utilizables para entrenamiento ML.

---

## HU-01 — Cargar Dataset

### Historia

Como analista de datos,
quiero cargar datasets CSV institucionales,
para utilizar información educativa dentro del pipeline.

### Prioridad

Alta

### Criterios de aceptación

- Carga correcta de `estudiantes.csv`
- Validación de existencia del archivo
- Lectura mediante pandas
- Manejo de errores de lectura
- Retorno DataFrame válido

---

## HU-02 — Validar Calidad de Datos

### Historia

Como científico de datos,
quiero detectar inconsistencias estructurales,
para asegurar calidad estadística y operacional.

### Prioridad

Alta

### Criterios de aceptación

- Validar columnas obligatorias
- Detectar dataset vacío
- Validar tipos de datos
- Detectar valores fuera de rango
- Detectar valores nulos
- Mostrar resumen de validación

---

## HU-03 — Tipar Variables

### Historia

Como desarrollador ML,
quiero convertir correctamente los tipos de datos,
para garantizar coherencia matemática.

### Prioridad

Alta

### Criterios de aceptación

- Variables booleanas convertidas
- Variables numéricas convertidas
- Variables categóricas tipadas
- Tipos incompatibles gestionados

---

## HU-04 — Gestionar Missing Values

### Historia

Como científico de datos,
quiero aplicar políticas diferenciadas de imputación,
para preservar calidad estadística.

### Prioridad

Alta

### Criterios de aceptación

- Imputación numérica por mediana
- Imputación segmentada por oferta educativa
- Variables auxiliares missing generadas
- Exclusión de registros inválidos
- Validación posterior a imputación

---

## HU-05 — Validar Variables Críticas

### Historia

Como científico de datos,
quiero excluir registros inválidos,
para evitar contaminación del entrenamiento.

### Prioridad

Alta

### Criterios de aceptación

- Validación de asistencia_pct
- Validación de matricula_activa
- Validación de dias_sin_actividad
- Exclusión controlada de registros críticos
- Logging de exclusiones

---

# EP-02 — Ground Truth y Riesgo

## Objetivo

Construir etiquetas supervisadas y métricas continuas de vulnerabilidad.

---

## HU-06 — Generar Etiquetas de Abandono Escolar

### Historia

Como científico de datos,
quiero generar automáticamente la variable `abandono_escolar`,
para construir un ground truth reproducible.

### Prioridad

Alta

### Criterios de aceptación

- Implementación reglas R1, R2 y R3
- Etiquetas binarias válidas
- Gestión edge cases
- Coherencia lógica validada
- Reproducibilidad garantizada

---

## HU-07 — Generar Variables de Riesgo

### Historia

Como científico de datos,
quiero transformar variables educativas en métricas normalizadas,
para homogenizar el cálculo del riesgo.

### Prioridad

Alta

### Criterios de aceptación

- Variables normalizadas en [0,1]
- Dirección semántica coherente
- Riesgos derivados generados
- Validación matemática completada

---

## HU-08 — Calcular RiskIndex

### Historia

Como institución educativa,
quiero calcular un índice continuo de vulnerabilidad,
para priorizar intervención preventiva.

### Prioridad

Alta

### Criterios de aceptación

- Fórmula ponderada implementada
- RiskIndex acotado en [0,1]
- Variables correctamente ponderadas
- Clasificación Bajo/Medio/Alto/Crítico
- Consistencia matemática validada

---

## HU-09 — Clasificar Niveles de Riesgo

### Historia

Como director institucional,
quiero clasificar estudiantes por severidad,
para facilitar priorización educativa.

### Prioridad

Alta

### Criterios de aceptación

- Clasificación automática generada
- Niveles Bajo/Medio/Alto/Crítico
- Umbrales documentados
- Distribución estadística visible

---

# EP-03 — Pipeline de Machine Learning

## Objetivo

Construir un pipeline ML robusto, reproducible y sin fugas de información.

---

## HU-10 — Preparar Variables Predictoras

### Historia

Como desarrollador ML,
quiero separar correctamente variables predictoras y objetivo,
para entrenar el modelo supervisado.

### Prioridad

Alta

### Criterios de aceptación

- Separación correcta X/y
- Exclusión variable objetivo
- Validación dimensional
- Variables derivadas disponibles

---

## HU-11 — Dividir Dataset Train/Test

### Historia

Como científico de datos,
quiero dividir correctamente entrenamiento y prueba,
para evaluar rendimiento realista.

### Prioridad

Alta

### Criterios de aceptación

- División 80/20
- Uso random_state
- Estratificación opcional
- Tamaños correctos

---

## HU-12 — Prevenir Data Leakage

### Historia

Como científico de datos,
quiero evitar fugas de información,
para garantizar evaluaciones válidas.

### Prioridad

Alta

### Criterios de aceptación

- Split antes de transformaciones
- Imputación solo sobre train
- Escalado solo sobre train
- Pipeline reproducible

---

## HU-13 — Transformar Variables para ML

### Historia

Como desarrollador ML,
quiero transformar variables automáticamente,
para compatibilidad con algoritmos supervisados.

### Prioridad

Alta

### Criterios de aceptación

- Uso ColumnTransformer
- Escalado numérico
- Encoding categórico
- Pipeline reutilizable

---

## HU-14 — Entrenar Modelo Logistic Regression

### Historia

Como científico de datos,
quiero entrenar un modelo Logistic Regression,
para detectar abandono escolar.

### Prioridad

Alta

### Criterios de aceptación

- Modelo entrenado
- Sin errores de convergencia
- Persistencia temporal válida
- Entrenamiento reproducible

---

## HU-15 — Generar Predicciones

### Historia

Como analista educativo,
quiero obtener predicciones automáticas,
para identificar estudiantes vulnerables.

### Prioridad

Alta

### Criterios de aceptación

- Predicciones binarias válidas
- Resultados coherentes
- Salida interpretable
- Compatibilidad batch

---

# EP-04 — Evaluación e Interpretabilidad

## Objetivo

Evaluar rendimiento y explicar comportamiento del modelo.

---

## HU-16 — Evaluar Rendimiento del Modelo

### Historia

Como científico de datos,
quiero medir métricas de clasificación,
para validar calidad predictiva.

### Prioridad

Alta

### Criterios de aceptación

- Accuracy calculado
- Classification report generado
- Precision y recall visibles
- Métricas exportables

---

## HU-17 — Generar Matriz de Confusión

### Historia

Como director escolar,
quiero visualizar errores del modelo,
para comprender calidad predictiva.

### Prioridad

Alta

### Criterios de aceptación

- Heatmap generado
- Etiquetas legibles
- Visualización clara
- Exportación disponible

---

## HU-18 — Analizar Importancia de Variables

### Historia

Como analista educativo,
quiero conocer variables más influyentes,
para comprender causas del abandono.

### Prioridad

Media

### Criterios de aceptación

- Coeficientes calculados
- Variables ordenadas
- Gráfico interpretable
- Relación con RiskIndex documentada

---

## HU-19 — Interpretar Resultados Institucionales

### Historia

Como institución educativa,
quiero interpretar patrones de riesgo,
para intervenir tempranamente.

### Prioridad

Media

### Criterios de aceptación

- Hallazgos documentados
- Riesgos identificados
- Recomendaciones generadas
- Casos críticos identificados

---

# EP-05 — Documentación y Gobierno Técnico

## Objetivo

Garantizar mantenibilidad, reproducibilidad y colaboración.

---

## HU-20 — Documentar Arquitectura Técnica

### Historia

Como desarrollador,
quiero documentar la arquitectura modular,
para facilitar mantenimiento y evolución.

### Prioridad

Media

### Criterios de aceptación

- Diagramas actualizados
- Flujo técnico documentado
- Dependencias descritas
- Arquitectura reproducible

---

## HU-21 — Crear Notebook Demostrativo

### Historia

Como evaluador académico,
quiero un notebook reproducible,
para demostrar funcionamiento completo.

### Prioridad

Media

### Criterios de aceptación

- Notebook funcional
- Explicaciones Markdown
- Flujo reproducible
- Resultados interpretables

---

## HU-22 — Documentar Impacto Social

### Historia

Como institución educativa,
quiero comprender implicaciones éticas y sociales,
para utilizar el sistema responsablemente.

### Prioridad

Media

### Criterios de aceptación

- Riesgos identificados
- Sesgos potenciales documentados
- Casos de uso definidos
- Recomendaciones éticas incluidas

---

# EP-06 — Evolución Técnica y Productivización

## Objetivo

Escalar capacidades analíticas y preparar despliegue institucional.

---

## HU-23 — Implementar Nuevos Algoritmos

### Historia

Como científico de datos,
quiero comparar algoritmos avanzados,
para mejorar precisión predictiva.

### Prioridad

Baja

### Criterios de aceptación

- Random Forest implementado
- XGBoost implementado
- Comparativa documentada
- Benchmark reproducible

---

## HU-24 — Implementar Cross Validation

### Historia

Como científico de datos,
quiero validar robustez estadística,
para evitar sobreajuste.

### Prioridad

Media

### Criterios de aceptación

- K-Fold implementado
- Métricas promedio calculadas
- Variabilidad reportada

---

## HU-25 — Balancear Clases

### Historia

Como científico de datos,
quiero tratar desbalanceo del dataset,
para mejorar sensibilidad del modelo.

### Prioridad

Media

### Criterios de aceptación

- Distribución analizada
- Técnicas SMOTE o equivalentes aplicadas
- Comparativa antes/después documentada

---

## HU-26 — Implementar Explainability Avanzada

### Historia

Como analista institucional,
quiero interpretar decisiones del modelo,
para mejorar transparencia.

### Prioridad

Media

### Criterios de aceptación

- SHAP values implementados
- Explicabilidad local disponible
- Explicabilidad global disponible

---

## HU-27 — Persistir Modelos Entrenados

### Historia

Como ML Engineer,
quiero almacenar modelos entrenados,
para reutilización y despliegue.

### Prioridad

Media

### Criterios de aceptación

- Serialización con joblib
- Versionado básico
- Carga correcta de modelos

---

## HU-28 — Crear API REST

### Historia

Como institución educativa,
quiero consumir predicciones vía API,
para integrar el sistema con plataformas externas.

### Prioridad

Baja

### Criterios de aceptación

- API FastAPI funcional
- Endpoint predict operativo
- Validación inputs
- Respuesta JSON válida

---

## HU-29 — Crear Dashboard Institucional

### Historia

Como director escolar,
quiero visualizar métricas en tiempo real,
para monitorear estudiantes vulnerables.

### Prioridad

Baja

### Criterios de aceptación

- Dashboard funcional
- Visualizaciones dinámicas
- Riesgos visibles
- Métricas institucionales disponibles

---

# Priorización General

| Prioridad | Historias |
|---|---|
| Alta | HU-01 → HU-17 |
| Media | HU-18 → HU-27 |
| Baja | HU-28 → HU-29 |

---

# Propuesta de Sprints

# Sprint 1 — Calidad y Validación de Datos

## Historias

- HU-01
- HU-02
- HU-03
- HU-04
- HU-05

## Entregables

- Validación estructural
- Gestión de missing values
- Dataset limpio

---

# Sprint 2 — Ground Truth y RiskIndex

## Historias

- HU-06
- HU-07
- HU-08
- HU-09

## Entregables

- Etiquetado reproducible
- Variables de riesgo
- RiskIndex operativo

---

# Sprint 3 — Pipeline ML

## Historias

- HU-10
- HU-11
- HU-12
- HU-13
- HU-14
- HU-15

## Entregables

- Pipeline reproducible
- Logistic Regression funcional
- Predicciones válidas

---

# Sprint 4 — Evaluación e Interpretabilidad

## Historias

- HU-16
- HU-17
- HU-18
- HU-19

## Entregables

- Métricas avanzadas
- Matriz de confusión
- Interpretación institucional

---

# Sprint 5 — Gobierno Técnico y Documentación

## Historias

- HU-20
- HU-21
- HU-22

## Entregables

- Arquitectura documentada
- Notebook demostrativo
- Gobierno técnico básico

---

# Sprint 6 — Productivización

## Historias

- HU-23 → HU-29

## Entregables

- Modelos avanzados
- Explainability
- Persistencia
- API REST
- Dashboard

---

# Roles Recomendados

| Rol | Responsabilidad |
|---|---|
| Data Engineer | Calidad y pipelines de datos |
| Data Scientist | Modelado estadístico |
| ML Engineer | Productivización ML |
| Analista Educativo | Interpretación institucional |
| Arquitecto Técnico | Diseño modular |
| Scrum Master | Coordinación ágil |

---

# Herramientas Recomendadas

| Área | Herramienta |
|---|---|
| Versionado | GitHub |
| ML | Scikit-learn |
| Visualización | Matplotlib / Seaborn |
| Notebook | Jupyter |
| API | FastAPI |
| MLOps | MLflow / Docker |
| Gestión Ágil | Jira / Trello |

---

# Resultado Esperado del MVP

Al finalizar el MVP:

- Dataset validado
- Etiquetas generadas
- RiskIndex operativo
- Pipeline ML reproducible
- Logistic Regression funcional
- Matriz de confusión
- Notebook demostrativo
- Arquitectura modular
- Repositorio reproducible

---

# Conclusión

La versión 2 reorganiza completamente el proyecto hacia una arquitectura orientada a:

- calidad de datos,
- gobierno del ground truth,
- ingeniería de riesgo,
- reproducibilidad ML,
- interpretabilidad,
- y escalabilidad institucional.

La nueva estructura facilita:

- mantenimiento,
- trazabilidad,
- validación estadística,
- evolución técnica,
- y despliegue futuro en entornos educativos reales.

