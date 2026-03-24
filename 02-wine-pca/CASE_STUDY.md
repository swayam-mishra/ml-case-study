# Case Study 2 — Wine Feature Extraction with PCA

## What are we doing?

We're taking a dataset with 13 chemical measurements per wine sample and squishing it down to just 2 dimensions so we can visualize it — while keeping as much of the original information as possible.

## The Data

We use sklearn's built-in **Wine dataset**, which contains 178 wine samples from three different cultivars (grape varieties). Each sample has 13 features:

- Alcohol content, Malic acid, Ash, Alkalinity of ash, Magnesium
- Total phenols, Flavanoids, Nonflavanoid phenols, Proanthocyanins
- Color intensity, Hue, OD280/OD315 diluted wines, Proline

13 features are impossible to visualize directly. That's where PCA comes in.

## The Method

**PCA (Principal Component Analysis)** finds the directions in the data where the values vary the most, and projects all the data onto those directions. We keep only the top 2 directions (called principal components), which lets us plot everything on a 2D graph.

Before applying PCA, we **standardize** the data using `StandardScaler` — this scales every feature to have mean 0 and standard deviation 1. This step is important because features measured in different units (e.g. milligrams vs ratios) would otherwise dominate the result unfairly.

## How We Evaluate

We print the **explained variance ratio** for each component — the fraction of total variance captured. For example, if PC1 = 0.36 and PC2 = 0.19, together they explain 55% of the original data's information.

## The Plot

A 2D scatter plot where each dot is a wine sample, colored by its cultivar class (red, green, blue). Well-separated clusters mean PCA successfully found structure in the data — you can tell the wine types apart from just 2 numbers instead of 13.

## Key Takeaway

PCA is not a classifier — it doesn't use the labels during transformation. It's purely about finding a compact representation. The fact that the three classes separate cleanly in 2D tells us the chemical profiles of the three cultivars are genuinely different.
