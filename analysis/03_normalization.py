from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np

BASE_DIR = Path(__file__).resolve().parent          # .../single_cell_pipeline/analysis
csv_path = (BASE_DIR / ".." / "data" / "expression_like_data.csv").resolve()

df = pd.read_csv(csv_path)

gene_cols = df.columns[1:]
df["total_expression"] = df[gene_cols].sum(axis=1)

df['total_expression_safe'] = df["total_expression"].replace(0, pd.NA)

scale = 10000
norm_gene = df[gene_cols].div(df["total_expression_safe"], axis=0) * scale

log_norm_gene = np.log1p(norm_gene)

norm_out = pd.concat([df[["cell_id"]], norm_gene], axis=1)
log_norm_out = pd.concat([df[["cell_id"]], log_norm_gene], axis=1)

print(norm_out)
print(log_norm_out)

output_path = (BASE_DIR / ".." / "outputs").resolve()
datetime_str = str(datetime.now())
norm_out.to_csv(output_path / (datetime_str + "_normalized_expression_level.csv"))
log_norm_out.to_csv(output_path / (datetime_str + "_log_normalized_expression_level.csv"))