# Arquitectura del Proyecto — Predicción de Abandono Escolar

## Descripción General

El proyecto sigue una arquitectura modular orientada a separación de responsabilidades.

El objetivo es construir un sistema de Machine Learning mantenible, escalable y fácil de entender para predecir riesgo de abandono escolar.

---

# Estructura General del Proyecto

```text
proyecto_abandono_escolar/
│
├── data/
│   └── estudiantes.csv
│
├── notebooks/
│   └── analisis.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── model.py
│   ├── visualization.py
│   └── main.py
│
├── outputs/
│   ├── matriz_confusion.png
│   └── reporte_modelo.txt
│
├── README.md
└── requirements.txt
```

---

# Arquitectura Modular

La arquitectura divide el sistema en módulos especializados.

```text
Dataset
   ↓
preprocessing.py
   ↓
model.py
   ↓
visualization.py
   ↓
Resultados
```

---

# Descripción de los Módulos

## 1. preprocessing.py

### Responsabilidad

Gestionar toda la preparación y transformación de datos.

### Funciones principales

- Cargar dataset
- Limpiar información
- Separar variables
- Dividir entrenamiento/prueba
- Escalar variables

### Entrada

```text
estudiantes.csv
```

### Salida

```text
X_train
X_test
y_train
y_test
```

### Beneficios

- Centraliza preprocesamiento
- Facilita reutilización
- Mejora mantenimiento

---

# 2. model.py

## Responsabilidad

Gestionar el entrenamiento y evaluación del modelo de Machine Learning.

## Modelo utilizado

- Logistic Regression

## Funciones principales

- Entrenar modelo
- Generar predicciones
- Calcular métricas

## Entrada

```text
Datos procesados
```

## Salida

```text
Predicciones
Accuracy
Classification Report
```

## Beneficios

- Aísla lógica ML
- Facilita reemplazo futuro del algoritmo
- Mejora testing

---

# 3. visualization.py

## Responsabilidad

Generar visualizaciones y gráficos de evaluación.

## Funciones principales

- Matriz de confusión
- Importancia de variables
- Visualización de resultados

## Entrada

```text
Predicciones y métricas
```

## Salida

```text
Gráficos y análisis visual
```

## Beneficios

- Mejora interpretación
- Facilita presentaciones
- Ayuda a toma de decisiones

---

# 4. main.py

## Responsabilidad

Coordinar la ejecución completa del sistema.

## Funciones principales

- Ejecutar flujo general
- Conectar módulos
- Mostrar resultados

## Beneficios

- Centraliza ejecución
- Simplifica automatización
- Facilita despliegue futuro

---

# Flujo Completo del Sistema

```text
Inicio
   │
   ▼
Carga Dataset
   │
   ▼
Preprocesamiento
   │
   ▼
División Train/Test
   │
   ▼
Escalado
   │
   ▼
Entrenamiento Modelo
   │
   ▼
Predicciones
   │
   ▼
Evaluación
   │
   ▼
Visualización
   │
   ▼
Resultados
   │
   ▼
Fin
```

---

# Ejemplo de Flujo Real

## Paso 1 — Cargar Dataset

```python
df = cargar_dataset("../data/estudiantes.csv")
```

---

## Paso 2 — Preparar Datos

```python
X, y = preparar_datos(df)
```

---

## Paso 3 — Dividir Datos

```python
X_train, X_test, y_train, y_test = dividir_datos(X, y)
```

---

## Paso 4 — Escalar Información

```python
X_train, X_test, scaler = escalar_datos(X_train, X_test)
```

---

## Paso 5 — Entrenar Modelo

```python
modelo = entrenar_modelo(X_train, y_train)
```

---

## Paso 6 — Realizar Predicciones

```python
y_pred = realizar_predicciones(modelo, X_test)
```

---

## Paso 7 — Evaluar Resultados

```python
accuracy, reporte = evaluar_modelo(y_test, y_pred)
```

---

## Paso 8 — Generar Visualizaciones

```python
graficar_matriz_confusion(y_test, y_pred)
```

---

# Ventajas de la Arquitectura

| Característica | Beneficio |
|---|---|
| Modularidad | Código organizado |
| Escalabilidad | Fácil agregar funcionalidades |
| Reutilización | Componentes independientes |
| Testing | Validación aislada |
| Mantenimiento | Menor complejidad |
| Colaboración | Trabajo paralelo en equipo |

---

# Buenas Prácticas Aplicadas

## Separación de responsabilidades

Cada archivo tiene un propósito único.

---

## Reutilización de funciones

Las funciones pueden utilizarse en:

- notebooks,
- APIs,
- dashboards,
- pipelines automáticos.

---

## Código mantenible

La estructura facilita:

- lectura,
- debugging,
- evolución del proyecto.

---

# Evolución Futura Recomendada

## Nuevos módulos posibles

```text
src/
│
├── validation.py
├── utils.py
├── config.py
├── inference.py
├── pipelines/
└── models/
```

---

# Posibles Mejoras Técnicas

## Machine Learning

- Random Forest
- XGBoost
- Redes Neuronales
- Validación cruzada

---

## Ingeniería de Software

- Docker
- CI/CD
- Testing automático
- APIs con FastAPI

---

# Conclusión

La arquitectura modular propuesta permite construir un proyecto profesional, escalable y fácil de mantener.

La separación entre:

- preprocesamiento,
- entrenamiento,
- visualización,
- ejecución principal

facilita tanto el desarrollo individual como el trabajo colaborativo en equipo.
