import pandas as pd

# All columns except *_id and *_url
columns_to_keep = [
    'short_name', 'long_name', 'player_positions', 'overall', 'potential', 'value_eur', 'wage_eur', 'age', 'dob',
    'height_cm', 'weight_kg', 'club_name', 'league_name', 'league_level', 'club_position', 'club_jersey_number',
    'club_loaned_from', 'club_joined', 'club_contract_valid_until', 'nationality_name', 'nation_position',
    'nation_jersey_number', 'preferred_foot', 'weak_foot', 'skill_moves', 'international_reputation', 'work_rate',
    'body_type', 'real_face', 'release_clause_eur', 'player_tags', 'player_traits', 'pace', 'shooting', 'passing',
    'dribbling', 'defending', 'physic', 'attacking_crossing', 'attacking_finishing', 'attacking_heading_accuracy',
    'attacking_short_passing', 'attacking_volleys', 'skill_dribbling', 'skill_curve', 'skill_fk_accuracy',
    'skill_long_passing', 'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed', 'movement_agility',
    'movement_reactions', 'movement_balance', 'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength',
    'power_long_shots', 'mentality_aggression', 'mentality_interceptions', 'mentality_positioning', 'mentality_vision',
    'mentality_penalties', 'mentality_composure', 'defending_marking_awareness', 'defending_standing_tackle',
    'defending_sliding_tackle', 'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
    'goalkeeping_positioning', 'goalkeeping_reflexes', 'goalkeeping_speed', 'ls', 'st', 'rs', 'lw', 'lf', 'cf', 'rf',
    'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb', 'lb', 'lcb', 'cb',
    'rcb', 'rb', 'gk'
]

def compute_feature_stats(df: pd.DataFrame):

    df_filtered = df[columns_to_keep].copy()

    numeric_stats = []
    categorical_stats = []

    for col in df_filtered.columns:
        missing_count = df_filtered[col].isnull().sum()

        if pd.api.types.is_numeric_dtype(df_filtered[col]):
            numeric_stats.append({
                "feature": col,
                "mean": df_filtered[col].mean(),
                "median": df_filtered[col].median(),
                "min": df_filtered[col].min(),
                "max": df_filtered[col].max(),
                "std": df_filtered[col].std(),
                "5th_percentile": df_filtered[col].quantile(0.05),
                "95th_percentile": df_filtered[col].quantile(0.95),
                "missing_values": missing_count
            })
        else:
            categorical_stats.append({
                "feature": col,
                "unique_classes": df_filtered[col].nunique(dropna=True),
                "missing_values": missing_count,
                "class_proportions": df_filtered[col].value_counts(dropna=False, normalize=True).to_dict()
            })

    return pd.DataFrame(numeric_stats), pd.DataFrame(categorical_stats)