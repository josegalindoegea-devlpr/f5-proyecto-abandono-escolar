# Métricas del Modelo — Predicción de Abandono Escolar

# Descripción General

Este documento define las métricas utilizadas para evaluar el rendimiento del sistema de predicción de abandono escolar.

El objetivo es:

- medir capacidad predictiva,
- detectar errores del modelo,
- evaluar estabilidad estadística,
- y garantizar interpretabilidad institucional.

Las métricas seleccionadas están alineadas con:

- clasificación binaria,
- detección temprana,
- y análisis de riesgo educativo.

---

# Objetivos de Evaluación

El sistema debe ser capaz de:

1. Detectar correctamente estudiantes en abandono.
2. Minimizar falsos negativos.
3. Mantener interpretabilidad.
4. Permitir seguimiento institucional.
5. Facilitar intervención temprana.

---

# Naturaleza del Problema

## Tipo de problema

```text
Clasificación binaria supervisada
```

---

## Variable objetivo

```text
abandono_escolar
```

Valores:

```text
0 → estudiante estable
1 → abandono confirmado
```

---

# Métricas Principales

# Accuracy

## Definición

Mide el porcentaje total de predicciones correctas.

---

## Fórmula

```text
Accuracy =
(TP + TN) /
(TP + TN + FP + FN)
```

Donde:

| Sigla | Significado |
|---|---|
| TP | True Positives |
| TN | True Negatives |
| FP | False Positives |
| FN | False Negatives |

---

## Interpretación

| Valor | Interpretación |
|---|---|
| > 0.90 | Excelente |
| 0.80 – 0.90 | Muy bueno |
| 0.70 – 0.80 | Aceptable |
| < 0.70 | Revisar modelo |

---

## Limitaciones

Accuracy puede resultar engañosa si:

- existe desbalance de clases,
- el abandono es minoritario,
- predominan estudiantes estables.

Por ello se complementa con:

- precision,
- recall,
- F1-score.

---

# Precision

## Definición

Mide cuántos estudiantes predichos como abandono realmente abandonan.

---

## Fórmula

```text
Precision = TP / (TP + FP)
```

---

## Interpretación

Alta precision implica:

- pocas falsas alarmas,
- menor sobreintervención institucional.

---

# Recall (Sensibilidad)

## Definición

Mide cuántos abandonos reales fueron detectados.

---

## Fórmula

```text
Recall = TP / (TP + FN)
```

---

## Importancia Institucional

En abandono escolar:

```text
Recall es crítico
```

porque:

- un falso negativo implica no detectar un estudiante vulnerable.

---

## Interpretación

| Valor | Interpretación |
|---|---|
| > 0.85 | Muy buena detección |
| 0.70 – 0.85 | Adecuada |
| < 0.70 | Riesgo institucional |

---

# F1-Score

## Definición

Combina:

- precision,
- recall.

---

## Fórmula

```text
F1 =
2 * (Precision * Recall)
/
(Precision + Recall)
```

---

## Interpretación

Permite equilibrar:

- falsas alarmas,
- y abandonos no detectados.

---

# Classification Report

## Objetivo

Generar un resumen completo del comportamiento del modelo.

---

## Métricas incluidas

- precision
- recall
- F1-score
- support

---

## Ejemplo esperado

```text
              precision    recall  f1-score   support

           0       0.91      0.95      0.93       200
           1       0.82      0.71      0.76        70

    accuracy                           0.89       270
```

---

# Matriz de Confusión

# Objetivo

Visualizar:

- aciertos,
- errores,
- falsos positivos,
- falsos negativos.

---

# Estructura

| | Predicción 0 | Predicción 1 |
|---|---|---|
| Real 0 | TN | FP |
| Real 1 | FN | TP |

---

# Interpretación Operativa

## True Positives

Estudiantes correctamente identificados como abandono.

---

## True Negatives

Estudiantes correctamente identificados como estables.

---

## False Positives

Estudiantes identificados erróneamente como abandono.

Impacto:

- intervención innecesaria,
- sobrecoste institucional.

---

## False Negatives

Estudiantes vulnerables no detectados.

Impacto:

- riesgo crítico,
- fallo preventivo.

---

# Métricas de Riesgo Operativo

Además del modelo predictivo, el sistema incorpora:

```text
RiskIndex
```

---

# Naturaleza del RiskIndex

## No es una probabilidad estadística pura

El índice:

- es heurístico,
- ponderado,
- interpretable,
- orientado a priorización.

---

# Clasificación del RiskIndex

| Rango | Nivel |
|---|---|
| 0.00 – 0.29 | Bajo |
| 0.30 – 0.49 | Medio |
| 0.50 – 0.69 | Alto |
| ≥ 0.70 | Crítico |

---

# Objetivos del RiskIndex

Permitir:

- intervención temprana,
- priorización institucional,
- dashboards educativos,
- análisis longitudinal,
- segmentación de riesgo.

---

# Métricas Futuras Recomendadas

# ROC-AUC

## Objetivo

Evaluar capacidad discriminativa global.

---

## Interpretación

| AUC | Calidad |
|---|---|
| > 0.90 | Excelente |
| 0.80 – 0.90 | Muy buena |
| 0.70 – 0.80 | Aceptable |
| < 0.70 | Débil |

---

# Cross-Validation

## Objetivo

Validar estabilidad del modelo.

---

## Beneficios

- menor sobreajuste,
- evaluación más robusta,
- mejor generalización.

---

# Métricas de Desbalanceo

## Problema

El abandono escolar suele ser minoritario.

---

## Métricas recomendadas

- balanced accuracy,
- ROC-AUC,
- precision-recall curve,
- macro F1.

---

# Métricas de Interpretabilidad

# Importancia de Variables

## Objetivo

Identificar:

- variables más influyentes,
- factores críticos de abandono.

---

# Variables esperadas más relevantes

- asistencia_pct,
- dias_sin_actividad,
- nota_media,
- nivel_socioeconomico,
- materias_suspensas.

---

# SHAP Values (Futuro)

## Objetivo

Explicar decisiones individuales del modelo.

---

## Beneficios

- interpretabilidad institucional,
- auditoría algorítmica,
- transparencia educativa.

---

# Riesgos de Interpretación

# Accuracy elevada no garantiza utilidad

Ejemplo:

```text
95% accuracy
```

puede ocultar:

```text
detección deficiente del abandono
```

si las clases están desbalanceadas.

---

# Riesgo de Sesgo

Variables socioeconómicas pueden introducir:

- sesgo estructural,
- discriminación indirecta,
- correlaciones espurias.

---

# Mitigaciones Recomendadas

- auditorías periódicas,
- revisión institucional,
- explicabilidad,
- control de fairness.

---

# Objetivos de Calidad del MVP

| Métrica | Objetivo Inicial |
|---|---|
| Accuracy | > 0.80 |
| Recall abandono | > 0.75 |
| F1-score abandono | > 0.75 |
| Data leakage | 0 |
| Pipeline reproducible | Sí |

---

# Estrategia de Evaluación

# Entrenamiento

```text
80% train
20% test
```

---

# Prevención de Leakage

Las transformaciones:

- imputación,
- escalado,
- encoding,

se ajustan únicamente sobre entrenamiento.

---

# Pipeline de Evaluación

```text
Dataset
   ↓
Preprocessing
   ↓
Train/Test Split
   ↓
Entrenamiento
   ↓
Predicciones
   ↓
Métricas
   ↓
Visualización
```

---

# Interpretación Institucional

Las métricas deben utilizarse como:

- apoyo a decisión,
- sistema preventivo,
- mecanismo de priorización.

Nunca como:

- decisión automática exclusiva,
- sustitución de evaluación humana.

---

# Evolución Futura

## Mejoras previstas

- calibración probabilística,
- ensemble methods,
- detección de drift,
- monitorización continua,
- fairness metrics,
- MLOps.

---

# Conclusión

La evaluación del modelo debe equilibrar:

- precisión estadística,
- interpretabilidad,
- y utilidad institucional.

El sistema prioriza especialmente:

- detección temprana,
- reducción de falsos negativos,
- y capacidad preventiva.

La combinación entre:

- métricas ML,
- reglas operativas,
- y RiskIndex,

permite c