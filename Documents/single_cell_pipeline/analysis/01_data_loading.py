# I take a quick look at the dataset (/data/expression_like_data.csv)
# using the describe() function from pandas
# to understand its basic structure and summary statistics.

from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent          # .../single_cell_pipeline/analysis
csv_path = (BASE_DIR / ".." / "data" / "expression_like_data.csv").resolve()

df = pd.read_csv(csv_path)

print("Data shape:", df.shape)
print(df.head())

numeric_cols = df.columns[1:]
print("\nSummary statistics:")
print(df[numeric_cols].describe())