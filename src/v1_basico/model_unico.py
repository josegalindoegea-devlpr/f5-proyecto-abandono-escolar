# modulo: model.py
# version: 1.0
# =========================
# IMPORTAR LIBRERÍAS
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# =========================
# CARGAR DATASET
# =========================

df = pd.read_csv("data/estudiantes.csv")

print(df.head())

# =========================
# VARIABLES
# =========================

X = df.drop("abandono", axis=1)
y = df["abandono"]

# =========================
# DIVIDIR DATOS
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# ESCALAR VARIABLES
# =========================

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =========================
# CREAR MODELO
# =========================

modelo = LogisticRegression()

modelo.fit(X_train, y_train)

# =========================
# PREDICCIONES
# =========================

y_pred = modelo.predict(X_test)

# =========================
# EVALUACIÓN
# =========================

accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")

print("\nReporte de clasificación:\n")
print(classification_report(y_test, y_pred))

# =========================
# MATRIZ DE CONFUSIÓN
# =========================

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No abandona', 'Abandona'],
    yticklabels=['No abandona', 'Abandona']
)

plt.xlabel("Predicción")
plt.ylabel("Valor Real")
plt.title("Matriz de Confusión")

plt.show()

# =========================
# IMPORTANCIA DE VARIABLES
# =========================

coeficientes = pd.DataFrame({
    'Variable': X.columns,
    'Coeficiente': modelo.coef_[0]
})

coeficientes = coeficientes.sort_values(
    by='Coeficiente',
    ascending=False
)

print("\nImportancia de Variables:\n")
print(coeficientes)
