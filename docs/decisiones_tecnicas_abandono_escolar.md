# Decisiones Técnicas — Proyecto Predicción de Abandono Escolar

# Descripción General

Este documento resume las principales decisiones técnicas tomadas durante el diseño y evolución del proyecto:

## Sistema Predictivo de Riesgo y Abandono Escolar mediante Machine Learning

El objetivo del documento es:

- centralizar criterios técnicos,
- justificar decisiones arquitectónicas,
- mantener trazabilidad,
- facilitar mantenimiento,
- y servir como referencia para futuras evoluciones.

---

# Principios Rectores del Proyecto

El sistema se diseñó bajo los siguientes principios:

| Principio | Objetivo |
|---|---|
| Modularidad | Separar responsabilidades |
| Reproducibilidad | Garantizar resultados repetibles |
| Escalabilidad | Permitir crecimiento futuro |
| Interpretabilidad | Facilitar comprensión institucional |
| Prevención de leakage | Garantizar evaluación válida |
| Gobernanza de datos | Mantener coherencia estadística |
| Trazabilidad | Justificar decisiones del modelo |

---

# Decisiones de Arquitectura

# DT-01 — Arquitectura Modular

## Decisión

Separar el sistema en módulos especializados.

## Justificación

Permite:

- reducir acoplamiento,
- mejorar mantenibilidad,
- facilitar testing,
- y permitir evolución independiente.

## Estructura adoptada

```text
src/
│
├── preprocessing.py
├── model.py
├── visualization.py
├── main.py
```

## Impacto

- Mejora legibilidad
- Facilita colaboración
- Reduce complejidad operativa

---

# DT-02 — Separación entre Ground Truth y RiskIndex

## Decisión

Separar explícitamente:

- `abandono_escolar`
- `RiskIndex`

## Justificación

Evita:

- contaminación del target,
- mezcla entre clasificación y scoring,
- ambigüedad conceptual.

## Implementación

| Variable | Función |
|---|---|
| abandono_escolar | Etiqueta supervisada |
| RiskIndex | Vulnerabilidad futura |

## Impacto

- Mejor interpretabilidad
- Arquitectura ML más limpia
- Mayor rigor estadístico

---

# DT-03 — Generación de Ground Truth mediante Reglas

## Decisión

Construir `abandono_escolar` mediante reglas operativas.

## Justificación

El dataset original no dispone de etiquetas reales consolidadas.

Se adopta un enfoque basado en:

- reglas institucionales,
- lógica educativa,
- y trazabilidad operacional.

## Reglas implementadas

### R1 — Abandono administrativo

```text
matricula_activa == 0
```

### R2 — Inactividad crítica

```text
dias_sin_actividad >= 60
AND asistencia_pct < 20
```

### R3 — Desvinculación académica severa

```text
evaluaciones_realizadas == 0
AND asistencia_pct < 30
AND nota_media < 3
```

## Impacto

- Etiquetado reproducible
- Transparencia institucional
- Fácil auditoría

---

# DT-04 — Uso de Logistic Regression como Modelo Base

## Decisión

Utilizar Logistic Regression como primer algoritmo.

## Justificación

Ventajas:

- interpretable,
- estable,
- rápida,
- adecuada para datasets pequeños y medianos,
- permite analizar coeficientes.

## Impacto

- Explicabilidad institucional
- Simplicidad operacional
- Base sólida para benchmark futuro

---

# DT-05 — Pipeline Reproducible con Scikit-learn

## Decisión

Construir pipelines ML usando:

- Pipeline
- ColumnTransformer
- SimpleImputer
- StandardScaler

## Justificación

Permite:

- evitar leakage,
- automatizar transformaciones,
- garantizar reproducibilidad.

## Impacto

- Menor riesgo estadístico
- Mejor mantenibilidad
- Integración futura más sencilla

---

# DT-06 — Prevención de Data Leakage

## Decisión

Separar train/test antes de:

- imputación,
- escalado,
- encoding.

## Justificación

Evita contaminación de información futura.

## Implementación

```text
Split → Fit(train) → Transform(test)
```

## Impacto

- Métricas más realistas
- Evaluación válida
- Mayor robustez científica

---

# DT-07 — Gestión Diferenciada de Missing Values

## Decisión

Aplicar imputación distinta según tipo de variable.

## Política adoptada

| Tipo | Estrategia |
|---|---|
| Numéricas | Mediana |
| Binarias | Categoría auxiliar |
| Variables críticas | Exclusión |

## Variables críticas

- asistencia_pct
- matricula_activa
- dias_sin_actividad

## Justificación

Las variables críticas afectan directamente:

- ground truth,
- RiskIndex,
- entrenamiento supervisado.

## Impacto

- Mayor consistencia estadística
- Menor distorsión del modelo

---

# DT-08 — Normalización de Variables de Riesgo

## Decisión

Transformar todas las variables de riesgo a rango [0,1].

## Justificación

Las variables originales:

- tienen escalas distintas,
- direcciones semánticas diferentes,
- y sensibilidades heterogéneas.

## Estrategia

Homogeneización mediante:

- inversión semántica,
- normalización,
- clipping.

## Ejemplo

```text
R_asistencia = 1 - (asistencia_pct / 100)
```

## Impacto

- Coherencia matemática
- Comparabilidad
- Cálculo estable del RiskIndex

---

# DT-09 — Construcción del RiskIndex Ponderado

## Decisión

Construir un índice continuo ponderado entre 0 y 1.

## Fórmula adoptada

```text
RiskIndex =
0.22 R_asistencia +
0.18 R_inactividad +
0.12 R_notas +
0.08 R_suspensas +
0.12 R_socioeco +
0.08 R_familia +
0.07 R_trabajo +
0.05 R_internet +
0.05 R_distancia +
0.03 R_oferta
```

## Justificación

Las ponderaciones reflejan:

- evidencia educativa,
- impacto institucional,
- y relevancia operativa.

## Impacto

- Priorización institucional
- Segmentación de estudiantes
- Alertas tempranas

---

# DT-10 — Clasificación Operativa del Riesgo

## Decisión

Definir niveles interpretables institucionalmente.

## Rangos adoptados

| Índice | Nivel |
|---|---|
| 0.00 – 0.29 | Bajo |
| 0.30 – 0.49 | Medio |
| 0.50 – 0.69 | Alto |
| >= 0.70 | Crítico |

## Justificación

Facilita:

- dashboards,
- intervención,
- priorización,
- reporting.

## Impacto

- Interpretabilidad institucional
- Facilidad operativa

---

# DT-11 — Exclusión de Variables con Riesgo de Sesgo

## Decisión

No utilizar `grado_urbanizacion` como riesgo directo.

## Justificación

Aplicar riesgo histórico directo podría:

- introducir sesgo territorial,
- penalizar entornos rurales,
- generar correlaciones espurias.

## Estrategia adoptada

Uso contextual únicamente.

La variable solo afecta:

```text
R_distancia
```

## Impacto

- Menor sesgo estructural
- Mejor causalidad

---

# DT-12 — Oferta Educativa mediante Riesgo Histórico

## Decisión

No normalizar linealmente `oferta_educativa`.

## Problema detectado

Las categorías:

- no representan magnitudes continuas,
- no poseen linealidad semántica.

## Estrategia adoptada

Asignación manual basada en riesgo histórico.

| Oferta | Riesgo |
|---|---|
| ESO | 0.3 |
| Bachillerato | 0.2 |
| FP Básica | 0.8 |
| FP Medio | 0.5 |

## Impacto

- Mayor coherencia semántica
- Mejor alineación educativa

---

# DT-13 — Visualización Explicable

## Decisión

Utilizar:

- matriz de confusión,
- importance plots,
- métricas legibles.

## Justificación

El proyecto tiene orientación:

- académica,
- institucional,
- y explicativa.

## Impacto

- Mejor comunicación
- Facilita validación humana

---

# DT-14 — Roadmap Evolutivo

## Decisión

Diseñar el MVP como base de evolución futura.

## Evolución prevista

### Corto plazo

- logging
- persistencia modelos
- métricas avanzadas

### Medio plazo

- cross-validation
- SHAP values
- balanceo de clases

### Largo plazo

- FastAPI
- dashboards
- MLOps
- monitorización

## Impacto

- Escalabilidad progresiva
- Preparación productiva
- Continuidad técnica

---

# DT-15 — Gobernanza y Documentación Técnica

## Decisión

Documentar:

- arquitectura,
- backlog,
- historias de usuario,
- decisiones técnicas,
- roadmap.

## Justificación

Permite:

- trazabilidad,
- alineación del equipo,
- mantenimiento futuro.

## Impacto

- Profesionalización del proyecto
- Mejor onboarding
- Mayor gobernanza técnica

---

# Riesgos Técnicos Identificados

| Riesgo | Mitigación |
|---|---|
| Dataset desbalanceado | Balanceo y métricas robustas |
| Leakage | Pipelines sklearn |
| Sesgo socioeconómico | Variables contextualizadas |
| Sobreajuste | Cross-validation |
| Drift futuro | Monitorización futura |
| Interpretabilidad limitada | SHAP y coeficientes |

---

# Decisiones Pendientes Futuras

| Área | Decisión futura |
|---|---|
| Modelado | XGBoost vs Random Forest |
| Persistencia | joblib vs MLflow |
| Serving | FastAPI vs Flask |
| Dashboard | Streamlit vs PowerBI |
| MLOps | Docker + CI/CD |
| Explainability | SHAP completo |

---

# Conclusión

Las decisiones técnicas adoptadas buscan construir un sistema:

- interpretable,
- modular,
- reproducible,
- estadísticamente consistente,
- y escalable.

La arquitectura actual prioriza:

- calidad de datos,
- trazabilidad,
- prevención de errores metodológicos,
- y aplicabilidad institucional.

El proyecto queda preparado para evolucionar desde un MVP académico hacia un producto empresarial.