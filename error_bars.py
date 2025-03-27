import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def generate_error_plots(df: pd.DataFrame):

    os.makedirs("plots", exist_ok=True)

    # --- Plot 1: Pace vs Age with Full Range Error Bars ---
    df_pace = df.dropna(subset=["pace", "age"])

    plt.figure(figsize=(12, 6))
    sns.pointplot(
        data=df_pace,
        x="age",
        y="pace",
        errorbar=lambda x: (x.min(), x.max()),
        capsize=0.2,
        color="teal"
    )
    plt.title("Player Pace by Age (Full Range Error Bars)")
    plt.xlabel("Age")
    plt.ylabel("Pace")
    plt.tight_layout()
    plt.savefig("plots/pace_by_age_errorbar_range.png")
    plt.close()

    # --- Plot 2: Potential Gap vs Age with LOESS Regression ---
    df_gap = df[df["age"].notna() & df["potential"].notna() & df["overall"].notna()].copy()
    df_gap["potential_gap"] = df_gap["potential"] - df_gap["overall"]

    plt.figure(figsize=(10, 6))
    sns.regplot(
        data=df_gap,
        x="age",
        y="potential_gap",
        lowess=True,
        scatter_kws={'alpha': 0.3},
        line_kws={'color': 'green'}
    )
    plt.title("Potential Gap vs Age (Smoothed LOESS)")
    plt.xlabel("Age")
    plt.ylabel("Potential - Overall")
    plt.tight_layout()
    plt.savefig("plots/potential_gap_vs_age_loess.png")
    plt.close()
