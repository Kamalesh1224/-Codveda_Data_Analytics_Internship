from common import *
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

df = pd.read_csv(require(iris_path())).drop_duplicates()
X = df.select_dtypes(include="number")
scaler = StandardScaler()
Xs = scaler.fit_transform(X)

inertias = []
ks = range(1, 11)
for k in ks:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(Xs)
    inertias.append(km.inertia_)

plt.figure()
plt.plot(list(ks), inertias, marker="o")
plt.xlabel("Number of clusters (k)"); plt.ylabel("Inertia")
plt.title("K-Means elbow method")
plt.tight_layout(); plt.savefig(OUT / "kmeans_elbow.png", dpi=150); plt.close()

# k=3 is a reasonable demonstration for this 3-species teaching dataset;
# also inspect the elbow plot before finalizing.
model = KMeans(n_clusters=3, random_state=42, n_init=10)
df["cluster"] = model.fit_predict(Xs)
pca = PCA(n_components=2, random_state=42)
coords = pca.fit_transform(Xs)
df["PC1"], df["PC2"] = coords[:, 0], coords[:, 1]

plt.figure()
sns.scatterplot(data=df, x="PC1", y="PC2", hue="cluster", palette="tab10")
plt.title("Iris K-Means clusters (PCA projection)")
plt.tight_layout(); plt.savefig(OUT / "kmeans_clusters_2d.png", dpi=150); plt.close()
df.to_csv(OUT / "iris_clustered.csv", index=False)
print(df.groupby("cluster")[X.columns.tolist()].mean())
