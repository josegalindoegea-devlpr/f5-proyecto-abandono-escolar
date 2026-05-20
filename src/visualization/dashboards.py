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
    VISUALIZATIONS_DIR, 
    ARCHIVO_METRICAS_MODELO,
    ARCHIVO_DASHBOARD_PRINCIPAL
)


# -------------------------------------------------------------------------
# CONFIGURACION GLOBAL
# -------------------------------------------------------------------------

plt.style.use("ggplot")


# -------------------------------------------------------------------------
# CREAR DIRECTORIO SI NO EXISTE
# -------------------------------------------------------------------------

VISUALIZATIONS_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# -------------------------------------------------------------------------
# DASHBOARD PRINCIPAL
# -------------------------------------------------------------------------

def generar_dashboard_principal(
    df,
    y_true,
    y_pred,
    metricas
):
    """
    Genera dashboard institucional principal.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset procesado.

    y_true : array-like
        Valores reales.

    y_pred : array-like
        Predicciones modelo.

    metricas : dict
        Métricas calculadas.
    """

    # -------------------------------------------------------------
    # FIGURA GENERAL
    # -------------------------------------------------------------

    fig = plt.figure(
        figsize=(18, 12)
    )

    fig.suptitle(
        "Dashboard - Sistema Predicción Abandono Escolar",
        fontsize=18,
        fontweight="bold"
    )

    # -------------------------------------------------------------
    # 1. MATRIZ DE CONFUSION
    # -------------------------------------------------------------

    ax1 = plt.subplot(2, 2, 1)

    matriz = confusion_matrix(
        y_true,
        y_pred
    )

    im = ax1.imshow(
        matriz,
        interpolation="nearest"
    )

    ax1.set_title("Matriz de Confusión")

    ax1.set_xticks([0, 1])
    ax1.set_yticks([0, 1])

    ax1.set_xticklabels([
        "No abandono",
        "Abandono"
    ])

    ax1.set_yticklabels([
        "No abandono",
        "Abandono"
    ])

    for i in range(2):
        for j in range(2):

            ax1.text(
                j,
                i,
                matriz[i, j],
                ha="center",
                va="center",
                fontsize=12
            )

    # -------------------------------------------------------------
    # 2. DISTRIBUCION RISK INDEX
    # -------------------------------------------------------------

    ax2 = plt.subplot(2, 2, 2)

    ax2.hist(
        df["RiskIndex"],
        bins=20
    )

    ax2.set_title(
        "Distribución RiskIndex"
    )

    ax2.set_xlabel(
        "Nivel de Riesgo"
    )

    ax2.set_ylabel(
        "Número Estudiantes"
    )

    # -------------------------------------------------------------
    # 3. DISTRIBUCION TARGET
    # -------------------------------------------------------------

    ax3 = plt.subplot(2, 2, 3)

    abandono_counts = (
        df["abandono_escolar"]
        .value_counts()
        .sort_index()
    )

    ax3.bar(
        ["Estable", "Abandono"],
        abandono_counts.values
    )

    ax3.set_title(
        "Distribución Abandono Escolar"
    )

    ax3.set_ylabel(
        "Número Estudiantes"
    )

    # -------------------------------------------------------------
    # 4. METRICAS MODELO
    # -------------------------------------------------------------

    ax4 = plt.subplot(2, 2, 4)

    nombres = list(metricas.keys())

    valores = list(metricas.values())

    ax4.bar(
        nombres,
        valores
    )

    ax4.set_ylim(0, 1)

    ax4.set_title(
        "Métricas Modelo"
    )

    for i, valor in enumerate(valores):

        ax4.text(
            i,
            valor + 0.02,
            f"{valor:.2f}",
            ha="center"
        )

    # -------------------------------------------------------------
    # AJUSTE LAYOUT
    # -------------------------------------------------------------

    plt.tight_layout()

    # -------------------------------------------------------------
    # GUARDAR DASHBOARD
    # -------------------------------------------------------------

    output_path = (
        VISUALIZATIONS_DIR /
        ARCHIVO_DASHBOARD_PRINCIPAL
    )

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )

    print("\nDashboard generado:")
    print(output_path)

    plt.close()


# -------------------------------------------------------------------------
# DASHBOARD EJECUTIVO SIMPLE
# -------------------------------------------------------------------------

def generar_dashboard_ejecutivo(
    metricas
):
    """
    Dashboard ejecutivo simplificado.
    """

    print("\n" + "=" * 60)
    print("RESUMEN EJECUTIVO MODELO")
    print("=" * 60)

    for nombre, valor in metricas.items():

        print(
            f"{nombre.upper():<15}: {valor:.4f}"
        )

    print("=" * 60)


# -------------------------------------------------------------------------
# EXPORTAR METRICAS
# -------------------------------------------------------------------------

def exportar_metricas_csv(
    metricas,
    nombre_archivo=ARCHIVO_METRICAS_MODELO
):
    """
    Exporta metricas a CSV.
    """

    df_metricas = pd.DataFrame(
        [metricas]
    )

    output_path = (
        VISUALIZATIONS_DIR /
        nombre_archivo
    )

    df_metricas.to_csv(
        output_path,
        index=False
    )

    print("\nMétricas exportadas:")
    print(output_path)
