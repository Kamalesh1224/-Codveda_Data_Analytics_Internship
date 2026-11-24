from common import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(require(iris_path())).drop_duplicates()
means = df.groupby("species", as_index=False)["petal_length"].mean()

plt.figure()
sns.barplot(data=means, x="species", y="petal_length")
plt.title("Average petal length by species")
plt.xlabel("Species"); plt.ylabel("Average petal length (cm)")
plt.tight_layout(); plt.savefig(OUT / "viz_bar_species.png", dpi=150); plt.close()

# A line chart of mean sepal length across sorted records (illustrative sequence).
line_df = df.sort_values("sepal_length").reset_index(drop=True)
plt.figure()
plt.plot(line_df.index, line_df["sepal_length"], label="Sepal length")
plt.title("Sepal length across sorted observations")
plt.xlabel("Observation (sorted)"); plt.ylabel("Sepal length (cm)")
plt.legend(); plt.tight_layout()
plt.savefig(OUT / "viz_line_sepal_length.png", dpi=150); plt.close()

plt.figure()
sns.scatterplot(data=df, x="petal_length", y="petal_width", hue="species")
plt.title("Petal length vs petal width")
plt.tight_layout(); plt.savefig(OUT / "viz_scatter_iris.png", dpi=150); plt.close()
print("Charts exported to", OUT)
