import pandas as pd

def load_data() -> pd.DataFrame:
    filepath: str = "data/players22.csv"
    try:
        df = pd.read_csv(filepath, low_memory=False)
        print("Data loaded successfully. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("File not found: {filepath}")
        return pd.DataFrame()
    except Exception as e:
        print("An error occurred: {e}")
        return pd.DataFrame()





