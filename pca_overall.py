import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def generate_pca_plot(df: pd.DataFrame):
    """Generate PCA projection of attributes and color by 'overall', save to plots folder."""
    os.makedirs("plots", exist_ok=True)

    attributes = [
        'age', 'height_cm', 'weight_kg',
        'value_eur', 'wage_eur',
        'international_reputation', 'weak_foot', 'skill_moves',
        'pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic'
    ]

    df_filtered = df[attributes + ['overall']].dropna()

    # Standardize data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df_filtered[attributes])

    # Apply PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)

    # Create PCA DataFrame
    pca_df = pd.DataFrame(pca_result, columns=['PC1', 'PC2'])
    pca_df['overall'] = df_filtered['overall'].values

    # Plot
    plt.figure(figsize=(10, 6))
    scatter = sns.scatterplot(
        data=pca_df,
        x='PC1', y='PC2',
        hue='overall',
        palette='coolwarm',
        alpha=0.7,
        edgecolor=None,
        legend=False
    )

    plt.title('PCA of Player Attributes Colored by Overall Rating')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.colorbar(scatter.collections[0], label='Overall Rating')
    plt.tight_layout()
    plt.savefig("plots/pca_overall_colored.png")
    plt.close()
