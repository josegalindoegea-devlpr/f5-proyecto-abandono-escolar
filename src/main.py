# ==========================================
# main.py
# Ejecución principal del proyecto
# ==========================================

from preprocessing import (
    cargar_dataset,
    preparar_datos,
    dividir_datos,
    escalar_datos
)

from model import (
    entrenar_modelo,
    realizar_predicciones,
    evaluar_modelo
)

from visualization import (
    graficar_matriz_confusion,
    graficar_importancia_variables
)

# ==========================================
# CARGA Y PREPROCESAMIENTO
# ==========================================

df = cargar_dataset("../data/estudiantes.csv")

X, y = preparar_datos(df)

X_train, X_test, y_train, y_test = dividir_datos(X, y)

X_train, X_test, scaler = escalar_datos(
    X_train,
    X_test
)

# ==========================================
# MODELO
# ==========================================

modelo = entrenar_modelo(X_train, y_train)

y_pred = realizar_predicciones(modelo, X_test)

accuracy, reporte = evaluar_modelo(
    y_test,
    y_pred
)

# ==========================================
# RESULTADOS
# ==========================================

print(f"Accuracy: {accuracy:.2f}")

print("\nReporte:\n")

print(reporte)

# ==========================================
# VISUALIZACIONES
# ==========================================

graficar_matriz_confusion(
    y_test,
    y_pred
)

graficar_importancia_variables(
    modelo,
    X.columns
)
