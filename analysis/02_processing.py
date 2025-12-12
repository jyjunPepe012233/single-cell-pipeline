from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent          # .../single_cell_pipeline/analysis
csv_path = (BASE_DIR / ".." / "data" / "expression_like_data.csv").resolve()

df = pd.read_csv(csv_path)

gene_cols = df.columns[1:]
df["total_expression"] = df[gene_cols].sum(axis=1)

print(df[["cell_id", "total_expression"]])

# Not all cells in a single-cell dataset are suitable for analysis.
# Some cells may have extremely low total expression,
# which often indicates technical failure or poor-quality measurements.

threshold = 50
filtered_df = df[df["total_expression"] >= threshold]

# In this pipeline, cells with a total expression below a defined threshold are excluded.
# The exact threshold is not a fixed rule, but a decision based on data characteristics and analysis goals.

print("Cells before QC (delete outliers):", len(df))
print("Cells after QC (delete outliers):", len(filtered_df))