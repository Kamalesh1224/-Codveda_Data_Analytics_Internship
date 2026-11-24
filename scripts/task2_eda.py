from common import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(require(iris_path())).drop_duplicates()
numeric = df.select_dtypes(include="number")

summary = numeric.agg(["mean", "median", "std"]).T
summary["mode"] = numeric.mode().iloc[0]
summary.to_csv(OUT / "iris_summary_statistics.csv")
print(summary)

for col in numeric.columns:
    plt.figure()
    sns.histplot(data=df, x=col, hue="species", kde=True)
    plt.title(f"Distribution of {col}")
    plt.tight_layout()
    plt.savefig(OUT / f"eda_hist_{col}.png", dpi=150)
    plt.close()

plt.figure()
sns.boxplot(data=df, x="species", y="petal_length")
plt.title("Petal length by species")
plt.tight_layout()
plt.savefig(OUT / "eda_boxplot.png", dpi=150)
plt.close()

plt.figure()
sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species")
plt.title("Petal length vs petal width")
plt.tight_layout()
plt.savefig(OUT / "eda_scatter.png", dpi=150)
plt.close()

corr = numeric.corr()
corr.to_csv(OUT / "iris_correlation.csv")
plt.figure(figsize=(7, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Iris feature correlation")
plt.tight_layout()
plt.savefig(OUT / "eda_correlation_heatmap.png", dpi=150)
plt.close()
print("EDA files saved in", OUT)
