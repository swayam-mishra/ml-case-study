import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

data = load_wine()
X, y = data.data, data.target

X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print("Explained variance ratio:", pca.explained_variance_ratio_)
print(f"Total variance explained: {pca.explained_variance_ratio_.sum():.4f}")

colors = ['red', 'green', 'blue']
for cls in range(3):
    mask = y == cls
    plt.scatter(X_pca[mask, 0], X_pca[mask, 1],
                c=colors[cls], label=data.target_names[cls], alpha=0.7, edgecolors='k', linewidths=0.3)

plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
plt.title("PCA of Wine Dataset (2 Components)")
plt.legend()
plt.tight_layout()
plt.show()
