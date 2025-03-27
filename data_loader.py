import pandas as pd

file_path = "data/players22.csv"
fifa_data = pd.read_csv(file_path,low_memory=False)


print(fifa_data.head(25))

