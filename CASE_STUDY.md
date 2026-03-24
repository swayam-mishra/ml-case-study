# ML Case Studies — What Are We Doing Here?

This project is a hands-on walkthrough of five fundamental machine learning concepts. Each case study is self-contained, uses a small dataset, and focuses on one core idea. Here's what each one does in plain terms.

---

## Case Study 1 — Predicting House Prices (Linear Regression)
**Folder:** `01-house-price-regression/house_price_regression.ipynb`

We want to predict the price of a house based on three things: its size in square feet, its location (suburban, urban, or downtown), and how many rooms it has. We generate a small fake dataset where price is roughly `150 × size + 20,000 × location + 10,000 × rooms`, with some random noise added to make it realistic.

We split the data into a training set and a test set, fit a straight-line (linear regression) model on the training data, and then check how well it predicts on unseen test data using two metrics — MSE (how far off the predictions are on average) and R² (how much of the variation in price our model explains). Finally we plot actual prices vs predicted prices; a perfect model would put all dots on the diagonal line.

---

## Case Study 2 — Simplifying the Wine Dataset (PCA)
**Folder:** `02-wine-pca/wine_pca.py`

The Wine dataset has 13 chemical measurements for 178 wine samples from three different cultivars. 13 features are hard to visualize. PCA (Principal Component Analysis) is a technique that finds the directions in the data that carry the most information and projects everything down to fewer dimensions.

We standardize the features first (so that measurements on different scales don't dominate), then reduce from 13 dimensions down to just 2. We print how much of the original variance those 2 components capture, and plot the wines as colored dots in 2D. If the clusters are clearly separated in the plot, it means those two components alone do a good job of telling the three wine types apart.

---

## Case Study 3 — Classifying Iris Flowers (KNN)
**Folder:** `03-iris-classification/iris_classification.ipynb`

The Iris dataset has 150 flower samples from three species (setosa, versicolor, virginica), each described by four measurements: sepal length, sepal width, petal length, petal width. The task is classification — given the measurements, predict which species it is.

We use KNN (K-Nearest Neighbors), which classifies a new point by looking at the 5 closest training examples and taking a majority vote. We print a classification report (precision, recall, F1 per class) and a confusion matrix — a heatmap that shows at a glance where the model got confused between classes.

---

## Case Study 4 — Grouping Iris Flowers Without Labels (KMeans)
**Folder:** `04-iris-clustering/iris_clustering.ipynb`

This is the unsupervised version of Case Study 3. We use the same Iris data but pretend we don't know the species labels. KMeans tries to find natural groupings in the data by minimizing the distance between each point and its assigned cluster center.

We ask it to find 3 clusters (since we know there are 3 species), fit it, and then compare its discovered clusters against the real labels using a cross-tabulation table. We also plot the flowers in 2D (using the first two features) colored by cluster, with the cluster centroids marked as X's. It's interesting to see how closely an algorithm can recover the real categories without ever being told what they are.

---

## Case Study 5 — Reading Handwritten Digits (CNN)
**Folder:** `05-mnist-cnn/mnist_cnn.ipynb`

MNIST is the classic benchmark dataset for image recognition — 70,000 grayscale images of handwritten digits (0–9), each 28×28 pixels. The task is to look at an image and predict which digit it shows.

We build a CNN (Convolutional Neural Network) — a type of neural network specifically designed for images. It uses convolutional layers to detect patterns like edges and curves, pooling layers to reduce spatial size, and dense layers at the end to make the final prediction. We train it for 5 epochs and it typically reaches ~99% accuracy on the test set. At the end we show 5 sample predictions with the true label and predicted label so you can see it working on real images.

---

## Common Thread

| Concept | Case Study |
|---------|------------|
| Supervised regression | CS-1 |
| Unsupervised dimensionality reduction | CS-2 |
| Supervised classification | CS-3 |
| Unsupervised clustering | CS-4 |
| Deep learning / image classification | CS-5 |

Each study follows the same pattern: load data → preprocess → train model → evaluate → visualize.
