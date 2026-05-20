# Comparativa Evolutiva del Proyecto

# 1. Visión General

El proyecto ha evolucionado desde un ejercicio académico simple de clasificación binaria utilizando Logistic Regression hacia una arquitectura de Machine Learning aplicada con orientación semiprofesional y enfoque operativo institucional.

La evolución ha afectado principalmente a:

- modelado de negocio,
- calidad de datos,
- ingeniería de variables,
- arquitectura software,
- trazabilidad metodológica,
- interpretabilidad,
- y capacidad futura de despliegue.

# 2. Comparativa Global
| Área | Requerimiento Inicial | Estado Actual | Nivel de Evolución |
|---|---|---|---|
| Objetivo ML |	Clasificación básica abandono/no abandono	| Sistema operativo de riesgo + clasificación	| Alto |
| Modelo	| Logistic Regression	| Logistic Regression modular y escalable	| Medio|
| Variables	| Variables simples	| Modelo semántico completo normalizado	| Alto|
| Ingeniería de datos | No definida	| Pipeline estructurado	| Alto|
| Arquitectura | Script simple	| Arquitectura modular profesional	| Alto|
| Etiquetado | Manual/simple	| Ground truth formalizado	| Muy Alto|
| Gestión missing values | No definida	| Política operativa definida	| Alto|
| Métricas | Accuracy | Roadmap hacia métricas avanzadas	| Medio|
| Visualización	| Matriz de confusión	| Visualización modular	| Medio|
| Interpretabilidad	| No considerada	| Riesgo interpretable por componentes	| Alto|
| Riesgo institucional | No contemplado	| Índice continuo RiskIndex	| Muy Alto|
| Escalabilidad	| No considerada | Roadmap MLOps/API | Alto|

# 3. Evolución Funcional del Proyecto
## 3.1 Objetivo del Sistema
Requisito original
Clasificar si un estudiante abandona o no.
Estado actual

El sistema ahora tiene dos capas diferenciadas:

### A. Clasificación binaria
abandono_escolar ∈ {0,1}

Basada en:

reglas operativas,
actividad académica,
asistencia,
matrícula,
desconexión.

### B. Sistema continuo de riesgo
RiskIndex ∈ [0,1]

Permite:

detección temprana,
priorización institucional,
segmentación operativa,
intervención preventiva.
Mejora conseguida

Separación correcta entre:

| Concepto	| Objetivo |
|---|---|
| Ground truth	| Confirmar abandono |
| RiskIndex	| Estimar vulnerabilidad futura |

Esto evita:

contaminación del target,
leakage conceptual,
problemas de interpretación.
## 3.2 Variables y Modelo de Negocio
Requisito original

Variables generales:

distancia,
internet,
nivel socioeconómico.
Estado actual

Se ha construido un modelo multidimensional:

|Dominio | Variables |
|---|---|
|Académico | asistencia, notas, suspensas |
|Temporal |	inactividad, ausencias |
|Administrativo	| matrícula |
|Socioeconómico | NSE, internet, trabajo |
|Territorial | urbanización + distancia |
|Contextual	| oferta educativa |
Mejora conseguida

El sistema ahora refleja:

causalidad educativa,
comportamiento longitudinal,
vulnerabilidad estructural.

Ya no es únicamente un clasificador tabular básico.

## 3.3 Definición del Ground Truth
Requisito original

No definido formalmente.

Estado actual

Se implementó una definición operativa basada en reglas:

R1 → matrícula inactiva
R2 → inactividad crítica
R3 → desvinculación académica severa
Mejora conseguida

Ahora existe:

trazabilidad,
explicabilidad,
reproducibilidad,
coherencia institucional.
Punto de mejora pendiente

Actualmente las reglas son deterministas.

## 3.4 Ingeniería de Variables
Requisito original

No definida.

Estado actual

Se implementó:

normalización semántica,
homogenización de dirección del riesgo,
escalado [0,1],
fórmulas causales,
variables derivadas.

Ejemplos:

R_asistencia
R_notas
R_inactividad
R_socioeco
R_distancia
Mejora conseguida

El modelo ahora es:

interpretable,
explicable,
matemáticamente consistente.
Punto crítico detectado

Actualmente coexistirán:

|Tipo |	Riesgo |
|---|---|
|Variables originales |	Escala natural |
|Variables riesgo |	Escala normalizada |

Esto puede generar:

multicolinealidad,
redundancia,
leakage semántico.
Recomendación

Separar explícitamente:

features_raw/
features_risk/

Y decidir qué capa consume el modelo ML.

## 3.5 Arquitectura Software
Requisito original

Modelo simple.

Estado actual

Arquitectura modular:

preprocessing.py
model.py
visualization.py
main.py

Con roadmap hacia:

validation/
config/
inference/
pipelines/
monitoring/
Mejora conseguida

Se alcanzó:

separación de responsabilidades,
mantenibilidad,
escalabilidad,
facilidad de testing.

## 3.6 Preprocessing
Requisito original

No definido.

Estado actual

El preprocessing ya contempla:

validación estructural,
validación de rangos,
imputación,
gestión de missing values,
generación de variables de riesgo,
preparación ML.
Mejora conseguida

El pipeline ya está cercano a un enfoque de producción.

Problemas detectados
A. Naming inconsistente

Actualmente aparecen simultáneamente:

abandono
abandono_escolar

Y también:

R_disciplinario
R_vulnerabilidad
R_final_disciplinario
Recomendación

## 3.7 Modelo ML
Requisito original

Logistic Regression.

Estado actual

Sigue alineado correctamente.

La elección es adecuada porque:

Ventaja	Valor
Interpretabilidad	Alta
Explicabilidad	Alta
Coste computacional	Bajo
Base lineal	Buena para MVP

## 3.8 Métricas
Requisito original

Matriz de confusión.

Estado actual

Ya existe:

accuracy,
classification_report,
matriz de confusión.

## 3.9 Product Backlog / Agile
Requisito original

Crear backlog de variables prioritarias.

Estado actual

Ya existe implícitamente mediante:

ponderaciones,
variables de riesgo,
roadmap técnico.

## 3.10 Interpretabilidad Institucional
Requisito original

Ayudar al director escolar.

Estado actual

El sistema ya permite:

clasificación,
scoring,
priorización,
dashboards futuros.
Evolución muy importante

El proyecto pasó de:

predicción ML

a:

sistema de apoyo a decisiones educativas

## 4. Bloques Técnicos Faltantes
### 4.1 Persistencia

Falta:

joblib.dump()
joblib.load()

## 4.2 Logging

Falta:

logging

profesional.

## 4.3 Configuración Centralizada

Falta:

config.py

Para:

pesos,
umbrales,
rutas,
parámetros.

## 4.4 Trazabilidad

Falta versionado de:

datasets,
modelos,
features,
pesos.

## 4.5 Testing

No existen:

tests/

## 4.6 Validación estadística

Falta:

cross-validation,
calibración,
análisis de drift,
estabilidad temporal.

# 5. Riesgos Técnicos Detectados
| Riesgo |	Impacto |
|---|---|
| Leakage entre reglas y features |	Alto |
| Ausencia de pipeline sklearn completo	| Medio |
| Accuracy como métrica principal |	Alto |
| Variables duplicadas semánticamente |	Alto |
| Naming inconsistente	| Medio |
| Sin control de balanceo	| Alto |
| Sin persistencia	| Medio |

# 6. Evaluación Global del Proyecto
| Área | Estado |
|---|---|
| Diseño conceptual	| Muy sólido |
| Arquitectura	| Buena |
| Ingeniería ML	| Media-Alta |
| Calidad operativa	| Media |
| Producción real	| Inicial |
| Escalabilidad	| Buena |
| Interpretabilidad	| Muy Alta |

# 7. Conclusión

El proyecto ha evolucionado correctamente desde un ejercicio académico simple hacia un sistema operativo de predicción de abandono escolar con orientación institucional y capacidad futura de producción.

La principal fortaleza actual es:

la coherencia conceptual entre:
- reglas de negocio,
- ingeniería de variables,
- RiskIndex,
- y arquitectura modular.

Los siguientes saltos evolutivos prioritarios deberían centrarse en:

consolidar preprocessing profesional,
evitar leakage y redundancias,
mejorar evaluación estadística,
implementar pipelines sklearn completos,
añadir persistencia y trazabilidad,
preparar despliegue e inferencia.