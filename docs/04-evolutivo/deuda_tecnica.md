# Elementos Faltantes para Cubrir los Requisitos Iniciales
Priorizados por importancia
#Prioridad 1 — Críticos

Estos elementos impactan directamente en el cumplimiento funcional del objetivo original del proyecto.

## 1. Generación automática del target abandono_escolar
Estado actual

Las reglas están documentadas pero todavía no están implementadas completamente en código.

Falta implementar
generar_target_abandono(df)

Aplicando:

R1 → matrícula inactiva
R2 → inactividad crítica
R3 → desvinculación académica
Impacto

Sin esto:

el modelo no está alineado con el negocio,
el dataset no tiene ground truth operativo,
el entrenamiento pierde coherencia conceptual.

## 2. Pipeline completo de preprocessing
Estado actual

Existe diseño parcial.

Falta implementar

Pipeline real:

Carga
→ Validación
→ Tipado
→ Missing values
→ Ingeniería riesgo
→ RiskIndex
→ Split
→ Transformación ML
Impacto

Actualmente el preprocessing no refleja todavía la lógica operativa completa.

## 3. Métricas adecuadas para abandono escolar
Estado actual

Solo:

accuracy,
classification_report.
Falta implementar

Prioridad:

Recall
F1-score
ROC-AUC
Precision
Impacto

Accuracy puede ocultar fallos graves si abandono es minoritario.

## 4. Gestión del desbalanceo de clases
Estado actual

No implementado.

Falta implementar

Opciones:

class_weight="balanced"

o:

SMOTE
Impacto

Muy alto.

En abandono escolar:

falsos negativos son críticos

## 5. Persistencia del modelo
Estado actual

No existe.

Falta implementar
joblib.dump()
joblib.load()
Impacto

Sin persistencia:

no hay reutilización,
no existe inferencia real,
no hay despliegue posible.
Prioridad 2 — Alta

Elementos importantes para robustez y alineación profesional.

## 6. Validación de rangos operativos
Estado actual

Definido conceptualmente.

Falta implementar

Validaciones como:

0 <= asistencia_pct <= 100
0 <= nota_media <= 10
dias_sin_actividad >= 0
Impacto

Evita corrupción silenciosa del dataset.

## 7. Gestión avanzada de missing values
Estado actual

Parcialmente definida.

Falta implementar
imputación por oferta educativa,
flags auxiliares,
exclusión registros críticos.
Impacto

Muy relevante para calidad ML.

## 8. Pipeline sklearn profesional
Estado actual

Escalado aislado.

Falta implementar
Pipeline()
ColumnTransformer()
Impacto

Facilita:

producción,
inferencia,
serialización,
reproducibilidad.

## 9. Separación explícita entre variables raw y variables riesgo
Estado actual

Mezcla conceptual.

Falta implementar

Estructura clara:

raw_features
risk_features
target
Impacto

Evita:

leakage,
multicolinealidad,
redundancia semántica.

## 10. Logging técnico
Estado actual

No existe.

Falta implementar
logging
Impacto

Clave para debugging y trazabilidad.

Prioridad 3 — Media

Elementos de evolución y calidad técnica.

## 11. Configuración centralizada
Falta implementar
config.py

Con:

pesos,
umbrales,
rutas,
parámetros.

## 12. Exportación de resultados
Falta implementar

Guardar automáticamente:

métricas,
gráficos,
modelos,
predicciones.

## 13. Product Backlog formal
Falta implementar

Documento:

product_backlog.md

## 14. Notebook demostrativo institucional
Estado actual

Mencionado, no consolidado.

Falta implementar

Notebook que explique:

problema,
pipeline,
métricas,
interpretación.

## 15. Interpretabilidad avanzada
Falta implementar
SHAP,
feature importance robusta,
análisis causal parcial.
Prioridad 4 — Evolución futura

No son necesarias para el MVP, pero sí estratégicas.

## 16. API REST

Con:

FastAPI

## 17. Dashboard institucional

Para:

alertas,
segmentación,
priorización.

## 18. Monitorización del modelo
drift,
estabilidad temporal,
degradación.
## 19. Automatización ETL

Pipeline automatizado de carga y validación.

## 20. MLOps
versionado,
CI/CD,
registry,
despliegue continuo.

# Elementos Adecuados para la Evolución e Integridad del Proyecto
## 1. Separación entre abandono confirmado y vulnerabilidad
Estado

Muy correcto.

Valor

Evita:

contaminación conceptual,
targets ambiguos,
scoring incorrecto.

## 2. Arquitectura modular
Estado

Correctamente planteada.

Valor

Facilita:

mantenimiento,
testing,
escalabilidad.

## 3. Normalización semántica de variables
Estado

Muy bien diseñada.

Valor

Permite:

coherencia matemática,
interpretabilidad,
comparabilidad.

## 4. RiskIndex interpretable
Estado

Muy sólido conceptualmente.

Valor

Convierte el sistema en:

herramienta de apoyo institucional

y no solo en un clasificador.

## 5. Uso de Logistic Regression para MVP
Estado

Correcto.

Valor

Ideal para:

explicabilidad,
baseline,
velocidad,
interpretabilidad.

## 6. Definición operativa del abandono
Estado

Muy madura.

Valor

Da:

trazabilidad,
consistencia,
gobernanza del dato.

## 7. Uso de reglas causales
Estado

Bien orientado.

Valor

El modelo refleja:

lógica educativa,
comportamiento institucional,
vulnerabilidad real.

## 8. Roadmap técnico escalonado
Estado

Muy coherente.

Valor

La evolución:

MVP → producción → MLOps

está correctamente secuenciada.

## 9. Orientación institucional
Estado

Excelente enfoque.

Valor

El proyecto ya no es solamente académico.

Tiene potencial real para:

prevención,
priorización,
intervención educativa.

## 10. Diseño preparado para escalabilidad
Estado

Bien encaminado.

Valor

La modularidad actual facilita:

APIs,
dashboards,
pipelines automáticos,
inferencia futura.

---