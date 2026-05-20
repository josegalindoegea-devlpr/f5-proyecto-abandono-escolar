# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: modeling
# modulo: train.py
# Funcionalidad: 
# Version: 2.0
# ==========================================
# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
from sklearn.linear_model import LogisticRegression

# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------

def entrenar_modelo(X_train, y_train):
    """
    Entrenar el modelo con LogisticRegression.
    """
    model = LogisticRegression()

    model.fit(X_train, y_train)

    return model