import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def generate_correlation_heatmap(df: pd.DataFrame):
    """Generates a heatmap of selected player attributes and saves it to the 'plots' directory."""
    os.makedirs("plots", exist_ok=True)

    attributes = [
        'age', 'height_cm', 'weight_kg', 'overall',
        'value_eur', 'wage_eur',
        'international_reputation', 'weak_foot', 'skill_moves',
        'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic'
    ]

    plt.figure(figsize=(14, 10))
    sns.heatmap(df[attributes].corr(), annot=True, cmap='coolwarm', center=0)
    plt.title("Correlation Heatmap of Selected Player Attributes")
    plt.tight_layout()
    plt.savefig("plots/correlation_heatmap_attributes.png")
    plt.close()
