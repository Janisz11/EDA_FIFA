import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def generate_histograms(df: pd.DataFrame):
    """Generates and saves various histogram-based visualizations."""
    os.makedirs("plots", exist_ok=True)

    # --- Age Histogram ---
    df_age = df[df["age"].notna()]
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_age, x="age", bins=20, kde=True, color="skyblue")
    plt.title("Distribution of Player Age")
    plt.xlabel("Age")
    plt.ylabel("Number of Players")
    plt.tight_layout()
    plt.savefig("plots/histogram_age.png")
    plt.close()

    # --- Overall Histogram ---
    df_overall = df[df["overall"].notna()]
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df_overall, x="overall", bins=25, kde=True, color="mediumseagreen")
    plt.title("Distribution of Player Overall Ratings")
    plt.xlabel("Overall Rating")
    plt.ylabel("Number of Players")
    plt.tight_layout()
    plt.savefig("plots/histogram_overall.png")
    plt.close()

    # --- Main Position Barplot ---
    df_pos = df[df["player_positions"].notna()].copy()
    df_pos["main_position"] = df_pos["player_positions"].apply(lambda x: x.split(",")[0].strip())
    position_counts = df_pos["main_position"].value_counts().reset_index()
    position_counts.columns = ["position", "count"]

    plt.figure(figsize=(12, 6))
    sns.barplot(data=position_counts, x="position", y="count", palette="pastel")
    plt.title("Number of Players by Main Position")
    plt.xlabel("Main Position")
    plt.ylabel("Number of Players")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("plots/barplot_main_position.png")
    plt.close()

    # --- Finishing Histogram by Preferred Foot ---
    df_finish = df[df["preferred_foot"].isin(["Left", "Right"]) & df["attacking_finishing"].notna()]
    plt.figure(figsize=(10, 6))

    sns.histplot(
        data=df_finish,
        x="attacking_finishing",
        hue="preferred_foot",
        multiple="dodge",
        bins=20,
        palette="Pastel1",
        stat="density",
        alpha=0.6
    )

    sns.kdeplot(
        data=df_finish[df_finish["preferred_foot"] == "Left"],
        x="attacking_finishing",
        color="skyblue",
        label="Left foot (KDE)",
        linewidth=2
    )

    sns.kdeplot(
        data=df_finish[df_finish["preferred_foot"] == "Right"],
        x="attacking_finishing",
        color="salmon",
        label="Right foot (KDE)",
        linewidth=2
    )

    plt.title("Finishing Distribution by Preferred Foot (with KDE)")
    plt.xlabel("Finishing")
    plt.ylabel("Density")
    plt.legend()
    plt.tight_layout()
    plt.savefig("plots/histogram_finishing_by_foot.png")
    plt.close()

    # --- Overall by League Level ---
    df_lvl = df[df["overall"].notna() & df["league_level"].notna()].copy()
    df_lvl["league_level"] = df_lvl["league_level"].astype("category")

    plt.figure(figsize=(10, 6))
    sns.histplot(
        data=df_lvl,
        x="overall",
        hue="league_level",
        bins=25,
        multiple="stack",
        palette="Set2"
    )

    plt.title("Overall Rating Distribution by League Level")
    plt.xlabel("Overall Rating")
    plt.ylabel("Count")
    plt.legend(title="League Level", loc="upper right")
    plt.tight_layout()
    plt.savefig("plots/histogram_overall_by_league_level.png")
    plt.close()
