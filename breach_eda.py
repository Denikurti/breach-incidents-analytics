"""
Breach Incidents Analytics (Terminal workflow)
- Load data from data/raw/breaches.csv
- Clean: columns, types, dates
- Metrics: records_exposed by year/sector, root cause mix, time-to-discovery
- Exports: figures/*.png, data/processed/*.parquet + *.csv
"""

import os, pandas as pd, numpy as np, matplotlib.pyplot as plt

os.makedirs("figures", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

RAW = "data/raw/breaches.csv"

# 1) LOAD
df = pd.read_csv(RAW)  # put the CSV in place in next step
print("✅ Loaded:", df.shape)
print(df.head())
# 2) CLEAN
df.columns = df.columns.str.strip().str.lower().str.replace('"', '').str.replace(" ", "_")

print("\n📦 Columns:", list(df.columns))
print("\n🧹 Null counts:")
print(df.isna().sum())

# Example numeric conversion
for col in df.columns:
    if col not in ["index"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# 3) FIRST CHART (works with the sample height/weight CSV)
plt.figure(figsize=(8, 6))
plt.scatter(df.get("height(inches)", df.get("height_inches", df.select_dtypes(float).iloc[:,0])),
            df.get("weight(pounds)", df.get("weight_pounds", df.select_dtypes(float).iloc[:,1])),
            s=12, alpha=0.6)
plt.title("Height vs Weight (sample data)")
plt.xlabel("Height (inches)")
plt.ylabel("Weight (pounds)")
plt.tight_layout()
out_png = "figures/height_vs_weight.png"
plt.savefig(out_png, dpi=150)
plt.close()
print(f"✅ Saved figure → {out_png}")

# 4) SAVE CLEANED DATA
clean_path = "data/processed/clean_sample.parquet"
df.to_parquet(clean_path, index=False)
print(f"💾 Saved cleaned data → {clean_path}")

