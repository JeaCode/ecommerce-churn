# src/plots.py
import matplotlib.pyplot as plt

def plot_hist(df, col, bins=30):
    df[col].hist(bins=bins)
    plt.title(f"Distribución de {col}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")

def plot_hist_by_churn(df, col, target="Churn", bins=30):
    df[df[target] == 0][col].hist(bins=bins, alpha=0.5)
    df[df[target] == 1][col].hist(bins=bins, alpha=0.5)
    plt.legend(["No churn", "Churn"])
    plt.title(f"Distribución de {col} por {target}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")