# Case Study 4 — Iris Clustering with KMeans

## What are we doing?

We're using the same Iris dataset as Case Study 3, but this time we pretend we don't know the species labels. The goal is to let an algorithm discover natural groupings in the data entirely on its own.

## The Data

Same as CS-3 — 150 Iris flower samples with 4 features each (sepal length, sepal width, petal length, petal width). The difference here is that we don't give the model the species labels during training.

## The Model

**KMeans** works by:
1. Randomly placing k cluster centers in the feature space
2. Assigning each data point to the nearest center
3. Moving each center to the mean of its assigned points
4. Repeating steps 2–3 until the assignments stop changing

We set k=3 because we know (from the real world) there are 3 species. In a real unsupervised setting, you'd use tools like the elbow method to pick k.

## How We Evaluate

- **Inertia** — the sum of squared distances from each point to its cluster center. Lower means tighter, more compact clusters.
- **Crosstab (actual vs cluster)** — since we have the true labels, we can compare what KMeans found against the real species. This is a sanity check — in real unsupervised work you wouldn't have this.

Note: cluster numbers (0, 1, 2) are arbitrary and may not align with species IDs (0=setosa, etc.), but the crosstab shows whether the groupings match up.

## The Plot

A 2D scatter using the first two features (sepal length vs sepal width), with points colored by cluster label. Cluster centroids are marked with an **X**. This gives a visual sense of how well-separated the discovered clusters are.

## Key Takeaway

KMeans can recover structure that closely matches the real categories — without ever seeing the labels. However, it works best when clusters are roughly spherical and similarly sized. Setosa is very distinct; versicolor and virginica overlap slightly, which is where KMeans may struggle.
