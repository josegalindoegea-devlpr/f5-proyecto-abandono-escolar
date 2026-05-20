# ==========================================
# preprocessing.py
# Preparación y transformación de datos
# ==========================================

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def cargar_dataset(ruta_dataset):
    """
    Carga el dataset desde un archivo CSV.
    """

    df = pd.read_csv(ruta_dataset)

    return df


def preparar_datos(df):
    """
    Separa variables predictoras y objetivo.
    """

    X = df.drop("abandono", axis=1)

    y = df["abandono"]

    return X, y


def dividir_datos(X, y, test_size=0.2):
    """
    Divide los datos en entrenamiento y prueba.
    """

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=42
    )


def escalar_datos(X_train, X_test):
    """
    Escala las variables numéricas.
    """

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler