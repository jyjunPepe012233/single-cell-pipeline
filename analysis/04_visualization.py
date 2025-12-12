from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent          # .../single_cell_pipeline/analysis

# Load raw data
raw_data_csv_path = (BASE_DIR / ".." / "data" / "expression_like_data.csv").resolve()
raw = pd.read_csv(raw_data_csv_path)

gene_cols = raw.columns[1:]

# Compute total expression
raw["total_expression"] = raw[gene_cols].sum(axis=1)

# Load normalized Data
norm_data_csv_path = (BASE_DIR / ".." / "outputs" / "example_normalized_expression_level.csv").resolve()
norm = pd.read_csv(norm_data_csv_path)

# Visulization A - Total Expression Levels Before QC
plt.figure()
plt.hist(raw["total_expression"], bins=10)
plt.title("Total Expression per Cell (Before QC)")
plt.xlabel("Total Expression")
plt.ylabel("Number of Cells")
plt.show()

# Visualization B - Gene distribution before vs after normalization
gene = gene_cols[0]

plt.figure()
plt.hist(raw[gene], bins=10)
plt.title(f"{gene} Distribution (Raw)")
plt.xlabel("Expression")
plt.ylabel("Number of Cells")
plt.show()

plt.figure()
plt.hist(norm[gene], bins=10)
plt.title(f"{gene} Distribution (After Normalization)")
plt.xlabel("Normalized Expression")
plt.ylabel("Number of Cells")
plt.show()