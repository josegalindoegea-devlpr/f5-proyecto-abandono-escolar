# Historias de Usuario — Proyecto Predicción de Abandono Escolar

# Descripción General

Este documento define la propuesta inicial de Historias de Usuario para el proyecto:

## Predicción de Riesgo de Abandono Escolar mediante Machine Learning

La organización sigue un enfoque ágil basado en:

- Épicas
- Historias de Usuario
- Product Backlog
- Sprints iterativos

---

# Objetivo del Proyecto

Construir un sistema predictivo capaz de clasificar:

- `0 → Estudiante estable`
- `1 → Riesgo de abandono`

Utilizando variables educativas y socioeconómicas mediante Logistic Regression.

---

# Arquitectura Funcional del Proyecto

```text
Datos
   ↓
Preprocesamiento
   ↓
Entrenamiento ML
   ↓
Predicción
   ↓
Visualización
   ↓
Interpretación
```

---

# Épicas del Proyecto

| ID | Épica | Objetivo |
|---|---|---|
| EP-01 | Gestión de Datos | Preparar información educativa |
| EP-02 | Entrenamiento del Modelo | Construir sistema predictivo |
| EP-03 | Visualización y Análisis | Interpretar resultados |
| EP-04 | Documentación y Presentación | Comunicar funcionamiento |
| EP-05 | Evolución Técnica | Escalabilidad y mejoras futuras |

---

# EP-01 — Gestión de Datos

## Objetivo

Preparar y transformar correctamente los datos educativos.

---

## HU-01 — Cargar Dataset

### Historia

Como analista de datos,  
quiero cargar un dataset CSV de estudiantes,  
para utilizar información educativa dentro del modelo.

### Prioridad

Alta

### Criterios de aceptación

- El sistema carga `estudiantes.csv`
- Se valida existencia del archivo
- Los datos se almacenan en un DataFrame
- No existen errores de carga

---

## HU-02 — Validar Calidad de Datos

### Historia

Como científico de datos,  
quiero detectar inconsistencias y valores nulos,  
para asegurar calidad del entrenamiento.

### Prioridad

Alta

### Criterios de aceptación

- Detectar valores faltantes
- Validar tipos de datos
- Identificar inconsistencias
- Mostrar resumen de validación

---

## HU-03 — Preparar Variables Predictoras

### Historia

Como desarrollador ML,  
quiero separar variables predictoras y objetivo,  
para entrenar correctamente el modelo.

### Prioridad

Alta

### Criterios de aceptación

- Separación correcta de `X` e `y`
- Exclusión de variable objetivo
- Validación dimensional

---

## HU-04 — Dividir Datos Train/Test

### Historia

Como científico de datos,  
quiero dividir los datos en entrenamiento y prueba,  
para evaluar correctamente el rendimiento.

### Prioridad

Alta

### Criterios de aceptación

- División 80/20
- Uso de `random_state`
- Tamaños correctos

---

## HU-05 — Escalar Variables

### Historia

Como desarrollador ML,  
quiero normalizar variables numéricas,  
para mejorar estabilidad matemática del modelo.

### Prioridad

Alta

### Criterios de aceptación

- Uso de `StandardScaler`
- Escalado correcto
- Sin fuga de información

---

# EP-02 — Entrenamiento del Modelo

## Objetivo

Construir el sistema predictivo basado en Machine Learning.

---

## HU-06 — Entrenar Modelo Logistic Regression

### Historia

Como científico de datos,  
quiero entrenar un modelo Logistic Regression,  
para detectar riesgo de abandono.

### Prioridad

Alta

### Criterios de aceptación

- Modelo entrenado
- Sin errores de convergencia
- Persistencia temporal en memoria

---

## HU-07 — Generar Predicciones

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

---

## HU-08 — Evaluar Accuracy

### Historia

Como científico de datos,  
quiero medir precisión del modelo,  
para validar rendimiento predictivo.

### Prioridad

Alta

### Criterios de aceptación

- Accuracy calculado
- Classification report generado
- Métricas visibles

---

# EP-03 — Visualización y Análisis

## Objetivo

Interpretar visualmente el comportamiento del modelo.

---

## HU-09 — Generar Matriz de Confusión

### Historia

Como director escolar,  
quiero visualizar aciertos y errores del modelo,  
para comprender calidad predictiva.

### Prioridad

Alta

### Criterios de aceptación

- Heatmap generado
- Etiquetas claras
- Visualización legible

---

## HU-10 — Analizar Importancia de Variables

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

---

## HU-11 — Interpretar Resultados

### Historia

Como director institucional,  
quiero interpretar patrones de riesgo,  
para intervenir tempranamente.

### Prioridad

Media

### Criterios de aceptación

- Hallazgos documentados
- Riesgos identificados
- Recomendaciones incluidas

---

# EP-04 — Documentación y Presentación

## Objetivo

Documentar el sistema y facilitar comprensión académica.

---

## HU-12 — Crear Notebook Demostrativo

### Historia

Como evaluador académico,  
quiero un notebook ejecutable y documentado,  
para reproducir el análisis completo.

### Prioridad

Media

### Criterios de aceptación

- Notebook funcional
- Explicaciones Markdown
- Flujo reproducible

---

## HU-13 — Documentar Arquitectura

### Historia

Como desarrollador,  
quiero documentar la arquitectura modular,  
para facilitar mantenimiento y colaboración.

### Prioridad

Media

### Criterios de aceptación

- Diagramas incluidos
- Explicación modular
- Flujo documentado

---

## HU-14 — Presentar Impacto Social

### Historia

Como institución educativa,  
quiero comprender el impacto social del modelo,  
para utilizarlo como herramienta preventiva.

### Prioridad

Media

### Criterios de aceptación

- Casos de uso definidos
- Beneficios explicados
- Riesgos identificados

---

# EP-05 — Evolución Técnica

## Objetivo

Escalar el proyecto y mejorar capacidades futuras.

---

## HU-15 — Implementar Nuevos Algoritmos

### Historia

Como científico de datos,  
quiero comparar modelos avanzados,  
para mejorar precisión predictiva.

### Prioridad

Baja

### Criterios de aceptación

- Random Forest implementado
- XGBoost implementado
- Comparativa documentada

---

## HU-16 — Crear Dashboard Interactivo

### Historia

Como director escolar,  
quiero visualizar métricas en tiempo real,  
para monitorear estudiantes vulnerables.

### Prioridad

Baja

### Criterios de aceptación

- Dashboard funcional
- Visualizaciones dinámicas
- Métricas actualizadas

## HU-17 — Generar Etiquetas de Abandono Escolar

### Historia

Como científico de datos,
quiero generar automáticamente la variable abandono_escolar,
para construir un ground truth consistente y reproducible.

### Prioridad

Alta

### Criterios de aceptación

- Implementación de reglas R1, R2 y R3
- Etiquetas binarias válidas
- Gestión de edge cases
- Validación de coherencia
- Reproducibilidad del etiquetado

## HU-18 — Calcular RiskIndex

### Historia

Como institución educativa,
quiero calcular un índice continuo de riesgo,
para priorizar intervenciones preventivas.

### Prioridad

Alta

### Criterios de aceptación

- Variables normalizadas en [0,1]
- Fórmula ponderada implementada
- Resultado acotado en [0,1]
- Clasificación Bajo/Medio/Alto/Crítico
- Sin inconsistencias matemáticas

## HU-19 — Generar Variables de Riesgo

### Historia

Como científico de datos,
quiero transformar variables educativas en métricas normalizadas de riesgo,
para homogenizar el cálculo del índice de abandono.

### Prioridad

Alta

### Criterios de aceptación

- Variables normalizadas en [0,1]
- Dirección semántica coherente
- Validación matemática
- Variables derivadas generadas correctamente

## HU-20 — Gestionar Missing Values

### Historia

Como científico de datos,
quiero aplicar políticas diferenciadas de imputación,
para preservar la calidad estadística del dataset.

### Prioridad

Alta

### Criterios de aceptación

- Imputación por mediana
- Gestión diferenciada por tipo
- Exclusión de registros inválidos
- Variables auxiliares missing generadas

## HU-21 — Prevenir Data Leakage

### Historia

Como científico de datos,
quiero evitar fugas de información entre entrenamiento y prueba,
para garantizar evaluaciones realistas del modelo.

### Prioridad

Alta

### Criterios de aceptación

- Split antes de fit
- Escalado solo con train
- Imputación solo con train
- Pipeline reproducible
---

# Product Backlog Priorizado

| Prioridad | Historias |
|---|---|
| Alta | HU-01 → HU-09 |
| Media | HU-10 → HU-14 |
| Baja | HU-15 → HU-16 |

---

# Propuesta de Sprints

# Sprint 1 — Base de Datos y Preprocesamiento

## Objetivo

Construir la base técnica del pipeline de datos.

## Historias incluidas

| Historia | Descripción |
|---|---|
| HU-01 | Carga dataset |
| HU-02 | Validación datos |
| HU-03 | Variables predictoras |
| HU-04 | División train/test |
| HU-05 | Escalado |

## Entregables

- Dataset funcional
- Preprocesamiento modular
- Validación inicial

---

# Sprint 2 — Modelo Predictivo

## Objetivo

Construir y evaluar el modelo ML.

## Historias incluidas

| Historia | Descripción |
|---|---|
| HU-06 | Entrenamiento modelo |
| HU-07 | Predicciones |
| HU-08 | Accuracy |
| HU-09 | Matriz de confusión |

## Entregables

- Logistic Regression funcional
- Métricas iniciales
- Visualización de evaluación

---

# Sprint 3 — Interpretación y Presentación

## Objetivo

Analizar resultados y documentar el proyecto.

## Historias incluidas

| Historia | Descripción |
|---|---|
| HU-10 | Variables importantes |
| HU-11 | Interpretación |
| HU-12 | Notebook |
| HU-13 | Arquitectura |
| HU-14 | Impacto social |

## Entregables

- Notebook completo
- Arquitectura documentada
- Presentación académica

---

# Sprint 4 — Evolución Técnica

## Objetivo

Escalar funcionalidades futuras.

## Historias incluidas

| Historia | Descripción |
|---|---|
| HU-15 | Nuevos algoritmos |
| HU-16 | Dashboard |

## Entregables

- Comparativa de modelos
- Dashboard inicial

---

# Roles Recomendados

| Rol | Responsabilidad |
|---|---|
| Data Engineer | Preparación de datos |
| Data Scientist | Modelado ML |
| ML Engineer | Arquitectura técnica |
| Analista Educativo | Interpretación |
| Scrum Master | Coordinación ágil |

---

# Herramientas Recomendadas

| Área | Herramienta |
|---|---|
| Versionado | GitHub |
| Notebooks | Jupyter |
| Machine Learning | Scikit-learn |
| Visualización | Matplotlib / Seaborn |
| Gestión Ágil | Trello / Jira |

---

# Resultado Esperado del MVP

Al finalizar el MVP:

- Dataset procesado
- Modelo entrenado
- Predicciones funcionales
- Matriz de confusión
- Notebook demostrativo
- Arquitectura modular
- Repositorio reproducible

---

# Conclusión

La propuesta inicial organiza el proyecto utilizando principios ágiles y arquitectura modular.

La división en:

- épicas,
- historias de usuario,
- backlog,
- sprints,

permite desarrollar el sistema de forma incremental, mantenible y orientada a resultados.

