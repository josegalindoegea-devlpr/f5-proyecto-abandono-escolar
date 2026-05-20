# ==========================================
# Proyecto: Abandono escolar
# Dominio funcional: visualization
# modulo: dashboards.py
# Funcionalidad: 
# Version: 2.0
# ==========================================

# -------------------------------------------------------------------------
# IMPORTS generales
# -------------------------------------------------------------------------
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import confusion_matrix
# -------------------------------------------------------------------------
# IMPORTS del Proyecto
# -------------------------------------------------------------------------
from config.settings import (
    VISUALIZATIONS_DIR
)