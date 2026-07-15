# Deep Learning Fundamentals and Neural Network Implementation

## Overview

This repository contains a collection of Deep Learning concepts, implementations, and assignments developed using Python, NumPy, Pandas, and Matplotlib.

The project covers:

- Dataset creation and preprocessing
- Batch processing and epochs
- Gradient Descent optimization
- Stochastic Gradient Descent (SGD)
- Adam Optimizer
- Neural Network Architecture
- Forward Propagation
- Backpropagation
- Loss Functions
- Activation Functions
- Mini-Batch Training
- Complete Neural Network Training Pipeline

---

# Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

---

# Topics Covered

## 1. Dataset Creation Using Pandas

Created sample datasets representing:

- Hours Studied
- Exam Scores

Example:

| Hours Studied | Exam Score |
|--------------|------------|
| 1 | 20 |
| 2 | 30 |
| 3 | 40 |
| 4 | 50 |

Converted data into:

```python
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values
```

---

## 2. Batch Processing

Implemented Mini-Batch Processing using:

```python
batch_size = 2
```

Dataset divided into multiple batches and processed sequentially.

### Example

Batch 1:

| Hours | Score |
|--------|--------|
| 1 | 20 |
| 2 | 30 |

Batch 2:

| Hours | Score |
|--------|--------|
| 3 | 40 |
| 4 | 50 |

---

## 3. Epochs

Implemented training across multiple epochs.

```python
epochs = 3
```

An epoch means one complete pass through the entire dataset.

---

## 4. Gradient Descent (GD)

Implemented Batch Gradient Descent from scratch.

### Formula

\[
Weight_{new} = Weight_{old} - LearningRate \times Gradient
\]

Steps:

1. Forward Propagation
2. Calculate Loss
3. Compute Gradients
4. Update Weights and Biases

---

## 5. Stochastic Gradient Descent (SGD)

Implemented SGD where model parameters are updated after every individual training sample.

### Advantages

- Faster updates
- Better for large datasets

### Disadvantages

- Noisy updates
- Less stable convergence

---

## 6. Adam Optimizer

Implemented Adam (Adaptive Moment Estimation) from scratch.

### Features

- Momentum
- Adaptive Learning Rates
- Faster Convergence
- Better Optimization Stability

### Hyperparameters

```python
learning_rate = 0.1
beta1 = 0.9
beta2 = 0.999
epsilon = 1e-8
```

---

# Activation Functions

## 1. Binary Step Function

### Formula

\[
f(x)=
\begin{cases}
1,& x \ge 0\\
0,& x < 0
\end{cases}
\]

### Characteristics

- Output: 0 or 1
- Used in early perceptrons

---

## 2. Linear Activation Function

### Formula

\[
f(x)=x
\]

### Characteristics

- Output equals input
- Commonly used in regression outputs

---

## 3. Sigmoid Function

### Formula

\[
\sigma(x)=\frac{1}{1+e^{-x}}
\]

### Output Range

```
0 to 1
```

### Applications

- Binary Classification
- Probability Prediction

---

## 4. Tanh Function

### Formula

\[
tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
\]

### Output Range

```
-1 to 1
```

### Advantages

- Zero-centered
- Often converges faster than sigmoid

---

## 5. ReLU Function

### Formula

\[
ReLU(x)=max(0,x)
\]

### Example

```
ReLU(-5) = 0
ReLU(0)  = 0
ReLU(7)  = 7
```

### Advantages

- Fast computation
- Reduces vanishing gradient problem

---

## 6. Softmax Function

### Formula

\[
Softmax(x_i)=\frac{e^{x_i}}{\sum e^{x_j}}
\]

### Characteristics

- Outputs probabilities
- Sum of outputs equals 1

### Example

Input Scores:

```python
[2.0, 1.0, 0.1]
```

Output Probabilities:

```python
[0.659, 0.242, 0.099]
```

---

# Neural Network Fundamentals

## Example Architecture

```
Input Layer      Hidden Layer      Output Layer

x1  --------\
x2  --------- > H1
x3  --------/  H2  --------> O1
                H3
                H4
```

### Network Structure

- Input Layer = 3 neurons
- Hidden Layer = 4 neurons
- Output Layer = 1 neuron

---

## Weight Calculation

### Input → Hidden

```
3 × 4 = 12 weights
```

### Hidden → Output

```
4 × 1 = 4 weights
```

### Total Weights

```
12 + 4 = 16
```

---

## Bias Calculation

### Hidden Layer Biases

```
4
```

### Output Layer Biases

```
1
```

### Total Biases

```
4 + 1 = 5
```

---

# Importance of Weights and Biases

## Weight

Determines how strongly an input influences a neuron.

### Higher Weight

More influence on output.

---

## Bias

Adds flexibility to the model by shifting the activation function.

Allows neurons to activate even when inputs are zero.

---

# Why Weights Should Not Be Initialized with Zero

If all weights start as zero:

- Neurons produce identical outputs
- Updates remain identical
- Neurons learn the same features
- Model cannot learn complex patterns

This is known as the **Symmetry Problem**.

Therefore, weights are initialized randomly.

Example:

```python
weights = np.random.randn(3)
bias = np.random.randn()
```

---

# Batch and Epoch Concepts

## Batch

A subset of the dataset used for one training step.

### Formula

\[
Batches = \frac{DatasetSize}{BatchSize}
\]

---

## Epoch

One complete pass through the entire dataset.

---

### Example

Dataset Size:

```
100
```

Batch Size:

```
25
```

Number of Batches:

```
100 / 25 = 4
```

Therefore:

```
4 batches per epoch
```

---

# Optimizers

## Gradient Descent

Updates after entire dataset.

### Advantage

Stable updates.

### Disadvantage

Slow for large datasets.

---

## Stochastic Gradient Descent (SGD)

Updates after every sample.

### Advantage

Fast updates.

### Disadvantage

Noisy training.

---

## Adam Optimizer

Combines:

- Momentum
- Adaptive Learning Rate

### Advantages

- Fast convergence
- Less tuning required
- Works well on most deep learning problems

---

# Deep Learning Mini Project

## Objective

Predict Exam Scores based on Hours Studied using a Neural Network built completely from scratch.

---

## Dataset

Generated synthetic dataset:

```python
hours = np.arange(1, 21)
scores = hours * 4.5 + noise
```

Dataset Shape:

```python
(20, 2)
```

---

## Neural Network Architecture

### Input Layer

```
1 neuron
```

### Hidden Layer

```
4 neurons
```

Activation:

```python
ReLU
```

### Output Layer

```
1 neuron
```

Activation:

```python
Linear
```

---

## Forward Propagation

Implemented:

```python
Z1 = XW1 + b1
A1 = ReLU(Z1)

Z2 = A1W2 + b2
y_pred = Z2
```

---

## Loss Function

Mean Squared Error (MSE)

### Formula

\[
MSE=\frac1n \sum (y-y_{pred})^2
\]

Implemented using:

```python
np.mean((y_true - y_pred) ** 2)
```

---

## Backpropagation

Computed gradients for:

- W1
- b1
- W2
- b2

Used chain rule to propagate errors backward through the network.

---

## Parameter Update

Implemented Gradient Descent updates:

```python
W = W - learning_rate * dW
b = b - learning_rate * db
```

---

## Mini-Batch Training

Batch Size:

```python
4
```

Each epoch processes:

```python
20 samples / 4 = 5 batches
```

---

## Training Configuration

```python
learning_rate = 0.001
epochs = 100
batch_size = 4
```

---

## Training Progress Tracking

Stored loss values:

```python
loss_history = []
```

Plotted:

```python
Training Loss Curve
```

using Matplotlib.

---

## Model Testing

Predictions generated for:

```python
Hours Studied = 3
Hours Studied = 11
Hours Studied = 18
```

Model outputs predicted exam scores for unseen data.

---

# Key Learning Outcomes

After completing this project, the following concepts were understood and implemented from scratch:

✅ Dataset Creation

✅ Batch Processing

✅ Epoch Training

✅ Gradient Descent

✅ Stochastic Gradient Descent

✅ Adam Optimizer

✅ Binary Step Function

✅ Linear Activation

✅ Sigmoid Function

✅ Tanh Function

✅ ReLU Function

✅ Softmax Function

✅ Neural Network Architecture

✅ Weight Initialization

✅ Forward Propagation

✅ Backpropagation

✅ Mean Squared Error Loss

✅ Mini-Batch Learning

✅ Parameter Optimization

✅ Deep Learning Training Loop

✅ Loss Visualization

✅ Prediction Using Trained Neural Networks

---

# Conclusion

This project provides a complete hands-on introduction to Deep Learning fundamentals by implementing neural network components from scratch without using high-level frameworks such as TensorFlow or PyTorch. It demonstrates how datasets are processed, how neural networks learn through forward propagation and backpropagation, and how optimizers like Gradient Descent, SGD, and Adam improve model performance over time.

The project serves as a strong foundation for understanding modern Deep Learning architectures and preparing for advanced frameworks and real-world AI applications.
