# Arquitectura del Proyecto — Predicción de Abandono Escolar

## Descripción General

El proyecto presenta una arquitectura modular orientada a producción, centrada en:

- trazabilidad del dato,
- consistencia estadística,
- mantenibilidad,
- separación entre:
  - reglas operativas,
  - ingeniería de variables,
  - Machine Learning,
  - visualización,
  - inferencia.

El objetivo del sistema es:

1. Detectar abandono escolar confirmado (ground truth).
2. Calcular vulnerabilidad futura mediante un RiskIndex.
3. Permitir intervención educativa temprana.
---

# Principios de Diseño

La arquitectura se basa en los siguientes principios:

| Principio | Objetivo |
|---|---|
| Modularidad | Separación clara de responsabilidades |
| Reproducibilidad | Resultados consistentes |
| Trazabilidad	| Explicabilidad del scoring |
| Escalabilidad | Fácil evolución futura |
| Robustez | Gestión correcta de errores y missing values |
| Homogeneización	| Variables normalizadas en escala [0,1] |
| Interpretabilidad | Riesgo explicable para entornos educativos |
---

# Estructura General del Proyecto
```text
proyecto_abandono_escolar/
│
├── data/
│   ├── raw/
│   │   └── estudiantes.csv
│   │
│   └── processed/
│       └── estudiantes_procesado.csv
│
├── notebooks/
│   └── analisis_exploratorio.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── evaluation.py
│   ├── visualization.py
│   ├── config.py
│   ├── utils.py
│   └── main.py
│
├── outputs/
│   ├── reports/
│   ├── metrics/
│   ├── models/
│   └── figures/
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_features.py
│   └── test_model.py
│
├── requirements.txt
├── README.md
└── arquitectura.md
```

# Arquitectura Funcional
```text
Dataset
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
Ground Truth (abandono)
   │
   ▼
Ingeniería de variables
   │
   ▼
Cálculo RiskIndex
   │
   ▼
Transformación ML
   │
   ▼
Entrenamiento
   │
   ▼
Evaluación
   │
   ▼
Visualización
   │
   ▼
Resultados
```
---
# Definición Operativa del Sistema
## Objetivos del Sistema

El sistema distingue dos conceptos fundamentales:

|Concepto |	Objetivo |
|---|---|
|abandono_escolar	| Confirmar abandono real |
|RiskIndex	| Estimar vulnerabilidad futura |

Esto evita:
- contaminación del target,
- mezcla entre scoring y clasificación,
- sesgos de interpretación.

## Ground Truth — Etiqueta Objetivo
Variable objetivo
abandono_escolar

Valores:

|Valor | Significado |
|---|---|
|1 | Abandono confirmado |
|0 | No abandono |

## Reglas Operativas de Etiquetado
### R1 — Abandono administrativo
```text
matricula_activa == 0
```
#### R2 — Inactividad crítica
```text
dias_sin_actividad >= 60
AND asistencia_pct < 20
```
#### R3 — Desvinculación académica severa
```text
evaluaciones_realizadas == 0
AND asistencia_pct < 30
AND (
    nota_media is null
    OR nota_media < 3
)
```
### Regla de estabilidad
```text
matricula_activa == 1
AND asistencia_pct >= 75
AND evaluaciones_realizadas > 0
```
---

# Arquitectura Modular
```text
src/
│
├── preprocessing.py
├── feature_engineering.py
├── model.py
├── evaluation.py
├── visualization.py
├── config.py
├── utils.py
└── main.py
```
# Descripción de los Módulos
## 1. preprocessing.py
### Responsabilidad

Gestionar:

validación estructural,
limpieza,
tipado,
imputación,
validación de rangos,
preparación ML.
### Funcionalidades principales
Carga de datos
cargar_dataset()
Validación estructural
validar_dataset()

Verifica:

columnas obligatorias,
dataset vacío,
integridad básica.
Tipado de variables
tipar_variables()

Convierte:

Tipo	Variables
float	notas, asistencia
int	suspensas, actividad
bool/int	binarias
Validación de rangos
validar_rangos()

Ejemplos:

Variable	Rango
asistencia_pct	[0,100]
nota_media	[0,10]
nivel_socioeconomico	[1,6]
Gestión de missing values
gestionar_missing_values()

Reglas:

Tipo	Estrategia
Numéricas	Mediana por oferta educativa
Binarias	Categoría auxiliar
Variables críticas	Exclusión

Variables críticas:

asistencia_pct
matricula_activa
dias_sin_actividad
Ingeniería de variables
generar_variables_riesgo()
Cálculo del índice
generar_risk_index()
Pipeline ML
preparar_features()

Incluye:

imputación,
encoding,
escalado,
transformación automática.

## 2. feature_engineering.py
### Responsabilidad

Centralizar toda la lógica matemática del modelo operativo.

Variables de riesgo normalizadas

Todas las variables se transforman a:

[0,1]

donde:

Valor	Interpretación
0	Riesgo mínimo
1	Riesgo máximo
Variables académicas
Riesgo por asistencia
R_asistencia = 1 - (asistencia_pct / 100)
Riesgo por notas
R_notas = 1 - (nota_media / 10)
Riesgo por suspensas
R_suspensas = (
    materias_suspensas /
    numero_materias_curso
)
Riesgo por inactividad
R_inactividad = min(
    dias_sin_actividad / 30,
    1
)
Variables socioeconómicas
Riesgo socioeconómico
R_socioeco = (
    nivel_socioeconomico - 1
) / 5
Riesgo por internet
R_internet = 1 if acceso_internet == 0 else 0
Riesgo por familia
R_familia = 1 if apoyo_familiar == 0 else 0
Riesgo por trabajo
R_trabajo = 1 if trabaja == 1 else 0
Riesgo por distancia

Depende del entorno:

|Zona	| Umbral |
|---|---|
|Urbana | 10 km |
|Semiurbana	| 20 km |
|Rural |	40 km |

R_distancia = min(
    distancia_escuela / umbral_zona,
    1
)
Riesgo por oferta educativa
|Oferta | Riesgo |
|---|---|
|ESO | 0.3 |
|Bachillerato | 0.2 |
|FP Básica | 0.8 |
|FP Medio |	0.5 |

## 3. RiskIndex
### Fórmula final
RiskIndex =
    0.22 * R_asistencia +
    0.18 * R_inactividad +
    0.12 * R_notas +
    0.08 * R_suspensas +
    0.12 * R_socioeco +
    0.08 * R_familia +
    0.07 * R_trabajo +
    0.05 * R_internet +
    0.05 * R_distancia +
    0.03 * R_oferta

Normalización final
RiskIndex = min(RiskIndex, 1)

### Clasificación Operativa
|Índice | Nivel |
|---|---|
|0.00 – 0.29 |	Bajo |
|0.30 – 0.49 |	Medio |
|0.50 – 0.69 |	Alto |
|≥ 0.70	| Crítico |

## 4. model.py
### Responsabilidad

Entrenamiento y evaluación de modelos ML.

Modelos iniciales
- Logistic Regression
Evolución futura
- Random Forest
- XGBoost
- LightGBM
- CatBoost
### Funcionalidades
Entrenamiento
entrenar_modelo()
Predicción
realizar_predicciones()
Probabilidades
predecir_probabilidades()
Persistencia
guardar_modelo()

## 5. evaluation.py
### Responsabilidad

Evaluación estadística y operativa.

Métricas principales
|Métrica | Objetivo |
|---|---|
| Accuracy | Rendimiento general |
| Precision	 | Reducir falsos positivos |
| Recall	| Detectar abandono real |
| F1-score |	Balance |
| ROC-AUC |	Separabilidad |

Métricas prioritarias

En abandono escolar:

Recall > Accuracy

Porque es más crítico:

no detectar un abandono,
que
generar falsas alertas.

## 6. visualization.py
### Responsabilidad

Visualización analítica y operativa.

Visualizaciones
Matriz de confusión
graficar_matriz_confusion()
Importancia de variables
graficar_importancia_variables()
Distribución de riesgo
graficar_distribucion_riesgo()
Segmentación de niveles
graficar_segmentacion_riesgo()

## 7. config.py
### Responsabilidad

Centralizar configuración global.

Contenido esperado
SEED = 42

TEST_SIZE = 0.2

PESOS_RISK_INDEX = {
    ...
}

## 8. utils.py
### Responsabilidad

Funciones auxiliares reutilizables.

Ejemplos
guardar_csv()
guardar_json()
cargar_configuracion()

## 9. main.py
### Responsabilidad

Orquestación completa del sistema.

### Flujo Operativo Completo
```text
Inicio
   │
   ▼
Carga dataset
   │
   ▼
Validación estructural
   │
   ▼
Tipado y limpieza
   │
   ▼
Missing values
   │
   ▼
Ground truth
   │
   ▼
Variables riesgo
   │
   ▼
RiskIndex
   │
   ▼
Preparación ML
   │
   ▼
Train/Test
   │
   ▼
Entrenamiento
   │
   ▼
Predicción
   │
   ▼
Evaluación
   │
   ▼
Visualización
   │
   ▼
Persistencia outputs
   │
   ▼
Fin
```
### Buenas Prácticas Aplicadas
| Práctica | Beneficio |
|---|---|
| Separación de responsabilidades |	Código mantenible |
| Validación temprana	| Evita errores silenciosos |
| Normalización homogénea	| Riesgo interpretable |
| Pipelines sklearn	| Reproducibilidad |
| Configuración centralizada |	Escalabilidad |
| Ingeniería explicable	| Transparencia educativa |