# Case Study 3 — Iris Flower Classification with KNN

## What are we doing?

We're training a model to identify which species of iris flower a sample belongs to, based on four physical measurements.

## The Data

We use sklearn's built-in **Iris dataset** — one of the most well-known datasets in machine learning. It contains 150 flower samples from three species:

- **Setosa**
- **Versicolor**
- **Virginica**

Each sample has 4 features measured in centimeters:
- Sepal length, Sepal width, Petal length, Petal width

The task is: given those 4 measurements, predict the species.

## The Model

We use **KNN (K-Nearest Neighbors)** with k=5. The idea is simple — when you want to classify a new flower, find the 5 most similar flowers in the training set (by Euclidean distance) and take a majority vote of their labels.

No explicit "training" happens — KNN just memorizes the training data and computes distances at prediction time.

## How We Evaluate

- **Accuracy** — percentage of test samples predicted correctly
- **Classification Report** — per-class breakdown of:
  - *Precision*: of all predictions for this class, how many were correct
  - *Recall*: of all actual samples of this class, how many did we catch
  - *F1 Score*: harmonic mean of precision and recall
- **Confusion Matrix** — a heatmap grid showing where predictions matched and where they got confused between classes

## The Plot

A seaborn heatmap of the confusion matrix. The diagonal cells (top-left to bottom-right) show correct predictions. Any off-diagonal values show misclassifications — which class got confused for which.

## Key Takeaway

KNN is intuitive and works well on small, clean datasets like Iris. It struggles with high-dimensional or noisy data, but here it achieves very high accuracy because the three species are fairly well-separated in feature space.
