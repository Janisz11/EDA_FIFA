import os
import seaborn as sns
import matplotlib.pyplot as plt
from simplified_positions import simplify_position

def generate_violin_plots(df):

    os.makedirs("plots", exist_ok=True)

    # --- VIOLIN 1: DEFENDING BY WORK RATE ---
    df_wr = df[df["work_rate"].notna()].copy()
    top_work_rates = df_wr["work_rate"].value_counts().nlargest(6).index
    df_wr = df_wr[df_wr["work_rate"].isin(top_work_rates)]

    plt.figure(figsize=(12, 6))
    sns.violinplot(data=df_wr, x="work_rate", y="defending", palette="Set3", inner="quartile")
    plt.title("Defending Attribute by Work Rate")
    plt.xlabel("Work Rate (Attack / Defense)")
    plt.ylabel("Defending")
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig("plots/violin_defending_by_workrate.png")
    plt.close()

    # --- Add simplified position ---
    df["simplified_position"] = df["player_positions"].apply(simplify_position)

    # --- VIOLIN 2: HEIGHT BY POSITION (horizontal) ---
    g = sns.catplot(
        data=df,
        y="simplified_position",
        x="height_cm",
        kind="violin",
        inner="stick",
        palette="pastel",
        orient='h',
        height=6,
        aspect=1.2
    )
    g.fig.suptitle("Height Distribution by Player Position", y=1.02)
    g.set_axis_labels("Height (cm)", "Player Position")
    plt.tight_layout()
    g.savefig("plots/violin_height_by_position.png")
    plt.close()

    # --- VIOLIN 3: AGE BY POSITION (vertical) ---
    g2 = sns.catplot(
        data=df,
        x="simplified_position",
        y="age",
        kind="violin",
        inner="stick",
        palette="Set2",
        height=6,
        aspect=1.5
    )
    g2.fig.suptitle("Age Distribution by Player Position", y=1.02)
    g2.set_axis_labels("Player Position", "Age")
    plt.xticks(rotation=20)
    plt.tight_layout()
    g2.savefig("plots/violin_age_by_position.png")
    plt.close()
