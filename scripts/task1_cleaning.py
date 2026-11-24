from common import *
import pandas as pd

df = pd.read_csv(require(iris_path()))
print("Before:", df.shape, "duplicates:", df.duplicated().sum())
print("Missing values:\n", df.isna().sum())

# Remove exact duplicate records.
df = df.drop_duplicates().copy()

# Standardize category text and data types.
df["species"] = df["species"].astype("string").str.strip().str.lower()
for col in ["sepal_length", "sepal_width", "petal_length", "petal_width"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Numeric missing-value treatment: median imputation.
num_cols = df.select_dtypes(include="number").columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Remove rows if the target category is missing.
df = df.dropna(subset=["species"])

out = OUT / "iris_cleaned.csv"
df.to_csv(out, index=False)
print("After:", df.shape, "duplicates:", df.duplicated().sum())
print("Saved:", out)
