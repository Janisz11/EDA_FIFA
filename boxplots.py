import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from simplified_positions import simplify_position

def generate_boxplots(df: pd.DataFrame):
    os.makedirs("plots", exist_ok=True)

    top_leagues = [
        "English Premier League", "Spain Primera Division",
        "German 1. Bundesliga", "Italian Serie A", "French Ligue 1"
    ]

    df_top5 = df[df["league_name"].isin(top_leagues)]

    # Plot 1
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df_top5, x="league_name", y="overall")
    plt.title("Overall rating in Top 5 European Leagues")
    plt.xlabel("League")
    plt.ylabel("Overall")
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.savefig("plots/overall_by_league.png")
    plt.close()

    # Prepare filtered df
    df_top5_copy = df_top5.copy()
    df_top5_copy["simplified_position"] = df_top5_copy["player_positions"].apply(simplify_position)
    df_top5_copy = df_top5_copy.dropna(subset=["wage_eur", "simplified_position"])
    df_filtered = df_top5_copy[df_top5_copy["wage_eur"] <= 150000]

    # Plot 2
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df_filtered, x="league_name", y="wage_eur", hue="simplified_position")
    plt.title("Wages by League and Position (Max 150k EUR)")
    plt.xlabel("League")
    plt.ylabel("Wage (EUR)")
    plt.xticks(rotation=45)
    plt.legend(title="Position")
    plt.tight_layout()
    plt.savefig("plots/wages_by_league_position.png")
    plt.close()

    # Plot 3
    bins = [0, 20, 25, 30, 55]
    labels = ["<20", "20-25", "26-30", "30+"]
    df_filtered["age_group"] = pd.cut(df_filtered["age"], bins=bins, labels=labels, right=False)

    plt.figure(figsize=(10, 6))
    flierprops = dict(marker='D', markerfacecolor='black', markersize=8, linestyle='none')
    sns.boxplot(
        data=df_filtered, x="league_name", y="wage_eur",
        hue="age_group", palette='Set2', flierprops=flierprops
    )
    plt.title("Wage (EUR) by League and Age Group — Top 5 Leagues")
    plt.xlabel("League")
    plt.ylabel("Wage (EUR)")
    plt.xticks(rotation=20)
    plt.legend(title="Age Group")
    plt.tight_layout()
    plt.savefig("plots/wages_by_league_agegroup.png")
    plt.close()
