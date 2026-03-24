# Case Study 1 — Predicting House Prices with Linear Regression

## What are we doing?

We're building a model that predicts the price of a house based on three simple features: its size, its location, and the number of rooms it has.

## The Data

There's no external dataset here — we generate 200 fake house records ourselves using NumPy. Each house has:

- **Size** — a random value between 500 and 3500 square feet
- **Location** — encoded as 0 (suburban), 1 (urban), or 2 (downtown)
- **Rooms** — a random integer between 1 and 6

The price is calculated as:

```
price = 150 × size + 20,000 × location + 10,000 × rooms + noise
```

The noise is random so the data isn't perfectly linear — just like real life.

## The Model

We use **Linear Regression** — the simplest supervised ML model. It fits a straight line (or hyperplane in multiple dimensions) through the data by finding the best weights for each feature.

We split the data 80/20 into train and test sets, train only on the training portion, and evaluate on the unseen test set.

## How We Evaluate

- **MSE (Mean Squared Error)** — the average squared difference between predicted and actual prices. Lower is better.
- **R² Score** — how much of the variance in price our model explains. 1.0 is perfect, 0.0 means the model is no better than just predicting the mean price.

## The Plot

A scatter plot of actual prices (x-axis) vs predicted prices (y-axis). A perfect model would put every point exactly on the red diagonal line. Points scattered around it show prediction error.

## Key Takeaway

Linear regression works well when the relationship between features and target is roughly linear. Since we constructed the data that way, the model fits very well here.
