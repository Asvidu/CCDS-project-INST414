from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
INPUT_CSV = BASE / "global_food_wastage_dataset.csv"
OUTPUT_CSV = BASE / "global_food_wastage_dataset_cleaned.csv"

df = pd.read_csv(INPUT_CSV)

original_rows = df.shape[0]
print("Original shape:", df.shape)

# Trim whitespace for text fields
for c in ("Country","Food Category"):
    if c in df.columns:
        df[c] = df[c].astype(str).str.strip()

# Ensure numeric columns
numeric_cols = [
    "Year",
    "Total Waste (Tons)",
    "Economic Loss (Million $)",
    "Avg Waste per Capita (Kg)",
    "Population (Million)",
    "Household Waste (%)"
]
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop duplicates and rows missing key columns
df = df.drop_duplicates()
key_columns = [
    "Country",
    "Year",
    "Food Category",
    "Total Waste (Tons)",
    "Economic Loss (Million $)",
    "Population (Million)"
]
present_keys = [k for k in key_columns if k in df.columns]
df = df.dropna(subset=present_keys)

# Basic validity checks
if "Population (Million)" in df.columns:
    df = df[df["Population (Million)"] > 0]
for col, minimum in [("Avg Waste per Capita (Kg)", 0), ("Economic Loss (Million $)", 0)]:
    if col in df.columns:
        df = df[df[col] >= minimum]
if "Household Waste (%)" in df.columns:
    df = df[(df["Household Waste (%)"] >= 0) & (df["Household Waste (%)"] <= 100)]

# Remove extreme top 1% outliers for main numeric targets if present
if "Total Waste (Tons)" in df.columns:
    tw_cutoff = df["Total Waste (Tons)"].quantile(0.99)
    df = df[df["Total Waste (Tons)"] <= tw_cutoff]
if "Economic Loss (Million $)" in df.columns:
    el_cutoff = df["Economic Loss (Million $)"].quantile(0.99)
    df = df[df["Economic Loss (Million $)"] <= el_cutoff]

# Restrict year range if column exists
if "Year" in df.columns:
    df = df[(df["Year"] >= 2018) & (df["Year"] <= 2024)]

print("Cleaned shape:", df.shape)
print("Rows removed:", original_rows - df.shape[0])

df.to_csv(OUTPUT_CSV, index=False)
print(f"Saved: {OUTPUT_CSV.name}")
