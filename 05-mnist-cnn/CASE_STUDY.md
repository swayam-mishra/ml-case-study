# Case Study 5 — MNIST Digit Classification with a CNN

## What are we doing?

We're building a deep learning model that looks at a 28×28 pixel image of a handwritten digit and predicts which number (0–9) it is.

## The Data

**MNIST** is the "hello world" of image classification. It contains:
- 60,000 training images
- 10,000 test images
- Each image is 28×28 pixels in grayscale, labeled with the digit it shows (0–9)

We normalize pixel values from the range [0, 255] down to [0, 1] — this helps the network train faster and more stably. We also reshape each image from `(28, 28)` to `(28, 28, 1)` to add a channel dimension, which is what Keras convolutional layers expect.

## The Model

We use a **CNN (Convolutional Neural Network)** — a type of neural network designed specifically for image data. Instead of treating each pixel as an independent input, CNNs scan the image with small filters to detect local patterns like edges, curves, and shapes.

The architecture:

| Layer | What it does |
|-------|-------------|
| `Conv2D(32, 3, relu)` | 32 filters of size 3×3, detects low-level features like edges |
| `MaxPooling2D` | Halves the spatial size, keeps the strongest activations |
| `Conv2D(64, 3, relu)` | 64 filters, detects more complex patterns |
| `MaxPooling2D` | Reduces size again |
| `Flatten` | Converts the 2D feature maps into a 1D vector |
| `Dense(128, relu)` | Fully connected layer, combines all learned features |
| `Dense(10, softmax)` | Output layer — one probability per digit class |

## Training

- **Optimizer:** Adam — an adaptive learning rate optimizer that works well out of the box
- **Loss:** Sparse categorical crossentropy — standard for multi-class classification with integer labels
- **Epochs:** 5 — five full passes over the training data
- **Batch size:** 64 — weights are updated every 64 images
- **Validation split:** 10% of training data held out to monitor overfitting during training

## How We Evaluate

- **Test Accuracy** — percentage of the 10,000 test images correctly classified. A well-trained CNN here typically exceeds 99%.

## The Plot

5 sample test images displayed side by side. Each shows the true label and the predicted label in the title — green if correct, red if wrong. This gives a human-readable sanity check on what the model is actually doing.

## Key Takeaway

CNNs are extremely effective for image tasks because they exploit spatial structure — nearby pixels are related, and the same pattern (like a curve) can appear anywhere in the image. This inductive bias makes them far more efficient than plain dense networks for vision problems.
