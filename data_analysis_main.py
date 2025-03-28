from data_loader import load_data
from feature_stats import compute_feature_stats
from linear_regression import scatter_with_regression
from violinplots import generate_violin_plots
from histograms import generate_histograms
from error_bars import generate_error_plots
from heatmap import generate_correlation_heatmap
from pca import generate_pca_plot
from boxplots import generate_boxplots

import os

def main():
    # Load dataset
    df = load_data()

    # Create global output directory
    os.makedirs("plots", exist_ok=True)
    os.makedirs("feature_stats_output", exist_ok=True)

    # --- Feature stats ---
    numeric_stats_df, categorical_stats_df = compute_feature_stats(df)
    numeric_stats_df.to_csv("feature_stats_output/numeric_feature_stats.csv", index=False)
    categorical_stats_df.to_csv("feature_stats_output/categorical_feature_stats.csv", index=False)
    print("Feature stats saved.")

    # --- Visualizations ---
    generate_violin_plots(df)
    generate_histograms(df)
    generate_error_plots(df)
    generate_correlation_heatmap(df)
    generate_pca_plot(df)
    generate_boxplots(df)

    print("All plots generated and saved to 'plots/' folder.")

    scatter_with_regression(df, "overall", "value_eur", reg_type="linear")
    scatter_with_regression(df, "overall", "value_eur", reg_type="lowess")
    scatter_with_regression(df, "overall", "value_eur", reg_type="log")
if __name__ == "__main__":
    main()
