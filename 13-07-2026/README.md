# CNN and OpenCV Image Processing Project

## Overview

This project demonstrates fundamental concepts of Computer Vision, Image Processing, OpenCV, and Convolutional Neural Networks (CNNs) using Python.

The project covers:

- Image Loading and Visualization
- Image Preprocessing
- Image Resizing
- Grayscale Conversion
- Pixel Manipulation
- Image Transformations
- Image Filtering
- Edge Detection
- Contour Detection
- CNN Architecture Design
- CNN Model Training
- Early Stopping
- Model Saving and Loading
- Performance Evaluation

---

# Technologies Used

- Python
- NumPy
- Matplotlib
- OpenCV
- TensorFlow
- Keras
- PIL (Python Imaging Library)
- Scikit-Learn
- Google Colab

---

# Project Structure

The project consists of two major sections:

## Part 1: Image Processing using PIL and OpenCV

## Part 2: Convolutional Neural Network (CNN) Implementation

---

# Part 1: Image Processing

## Image Upload and Loading

Images are uploaded using Google Colab:

```python
from google.colab import files
uploaded = files.upload()
```

Images are loaded using:

```python
from PIL import Image
img = Image.open(filename)
```

---

## Image Information Extraction

The following properties were analyzed:

```python
print(img.size)
print(img.format)
print(img.mode)
```

### Output

- Image Size
- Image Format
- Color Mode

---

## Image Resizing

Images were resized for CNN compatibility.

```python
img.resize((224,224))
```

### Purpose

- Standardized image dimensions
- Reduced computational complexity
- CNN input compatibility

---

## Grayscale Conversion

RGB images converted into grayscale.

```python
gray = img.convert("L")
```

### Benefits

- Reduced memory usage
- Faster processing
- Simplified feature extraction

---

## Image Normalization

Pixel values converted from:

```text
0-255
```

to

```text
0-1
```

using:

```python
image_array = image_array / 255.0
```

### Benefits

- Better model convergence
- Stable neural network training

---

## CNN Input Preparation

Reshaped image into CNN-compatible format:

```python
(1,224,224,1)
```

Where:

- 1 = Batch Size
- 224 = Height
- 224 = Width
- 1 = Grayscale Channel

---

# OpenCV Operations

---

## Reading Images

```python
image = cv2.imread(filename)
```

OpenCV stores images in:

```text
BGR Format
```

Converted to:

```python
cv2.COLOR_BGR2RGB
```

for visualization.

---

## Image Properties

Extracted:

```python
image.shape
image.size
image.dtype
```

### Information Obtained

- Height
- Width
- Channels
- Total Pixels
- Data Type

---

## Pixel Manipulation

Individual pixel values were accessed and modified.

Example:

```python
image[100,100]
```

Modified pixel:

```python
image[100,100] = [0,0,255]
```

---

## Image Saving

Processed images saved using:

```python
cv2.imwrite()
```

---

## Image Resizing

### Fixed Resize

```python
cv2.resize(image,(300,300))
```

### Scale Resize

```python
fx=0.5
fy=0.5
```

---

## Image Cropping

Selected a region of interest:

```python
cropped = image[100:500,200:600]
```

---

## Image Rotation

Implemented:

```python
cv2.ROTATE_90_CLOCKWISE
cv2.ROTATE_180
cv2.ROTATE_90_COUNTERCLOCKWISE
```

---

## Image Flipping

### Horizontal

```python
cv2.flip(image,1)
```

### Vertical

```python
cv2.flip(image,0)
```

### Both Directions

```python
cv2.flip(image,-1)
```

---

## Image Translation

Shifted image position using affine transformation.

```python
cv2.warpAffine()
```

Translation matrix:

```python
M = [[1,0,100],
     [0,1,50]]
```

---

## Color Space Conversion

### RGB to Grayscale

```python
cv2.COLOR_RGB2GRAY
```

### RGB to HSV

```python
cv2.COLOR_BGR2HSV
```

---

## Channel Splitting

Separated:

```python
Blue Channel
Green Channel
Red Channel
```

using:

```python
cv2.split()
```

Merged back using:

```python
cv2.merge()
```

---

## Drawing Features

### Line

```python
cv2.line()
```

### Rectangle

```python
cv2.rectangle()
```

### Circle

```python
cv2.circle()
```

### Ellipse

```python
cv2.ellipse()
```

### Text Annotation

```python
cv2.putText()
```

---

# Image Filtering

---

## Average Blur

```python
cv2.blur()
```

Purpose:

- Noise reduction
- Smoothing

---

## Gaussian Blur

```python
cv2.GaussianBlur()
```

Purpose:

- Smooth image
- Preserve important structures

---

## Median Blur

```python
cv2.medianBlur()
```

Purpose:

- Remove salt-and-pepper noise

---

## Bilateral Filtering

```python
cv2.bilateralFilter()
```

Purpose:

- Smooth image
- Preserve edges

---

## Thresholding

Implemented:

### Binary Threshold

```python
cv2.THRESH_BINARY
```

### Inverse Binary Threshold

```python
cv2.THRESH_BINARY_INV
```

---

## Edge Detection

Implemented using:

```python
cv2.Canny()
```

Purpose:

- Detect object boundaries
- Feature extraction

---

## Contour Detection

Contours extracted using:

```python
cv2.findContours()
```

Displayed using:

```python
cv2.drawContours()
```

Applications:

- Shape Detection
- Object Recognition

---

# Image Processing Pipeline

A complete image processing workflow was implemented:

### Stage 1

Original Image

↓

### Stage 2

Resize

↓

### Stage 3

Grayscale Conversion

↓

### Stage 4

Gaussian Blur

↓

### Stage 5

Edge Detection

---

# Part 2: Convolutional Neural Network (CNN)

---

## CNN Overview

A Convolutional Neural Network was created from scratch using TensorFlow and Keras.

The network included:

- Convolution Layers
- Pooling Layers
- Batch Normalization
- Dropout
- Dense Layers
- Softmax Output

---

## CNN Architecture

### Input Layer

```python
(32,32,3)
```

---

### First Convolution Block

```python
Conv2D(32,(3,3))
```

Activation:

```python
ReLU
```

Followed by:

```python
BatchNormalization
MaxPooling2D
```

---

### Second Convolution Block

```python
Conv2D(64,(3,3))
```

Followed by:

```python
BatchNormalization
MaxPooling2D
```

---

### Fully Connected Layers

```python
Flatten()
Dense(128)
Dropout(0.5)
```

---

### Output Layer

```python
Dense(10)
```

Activation:

```python
Softmax
```

Purpose:

- Multi-Class Classification

---

# Model Compilation

Model compiled using:

```python
Adam Optimizer
```

Loss Function:

```python
Categorical Crossentropy
```

Metric:

```python
Accuracy
```

---

# Dataset Generation

Random training data generated:

```python
100 Training Images
20 Validation Images
```

Image Shape:

```python
32x32x3
```

Classes:

```python
10 Classes
```

---

# Model Training

Training performed using:

```python
model.fit()
```

Training Parameters:

```python
Epochs = 15
Batch Size = 32
```

---

# Early Stopping

Implemented EarlyStopping callback.

```python
EarlyStopping(
monitor="val_loss",
patience=3
)
```

Benefits:

- Prevents overfitting
- Saves training time

---

# Model Checkpointing

Implemented:

```python
ModelCheckpoint()
```

Purpose:

- Save best model automatically
- Restore highest-performing model

---

# Accuracy Visualization

Training and validation accuracy plotted using:

```python
matplotlib
```

Graph:

```text
Training Accuracy
vs
Validation Accuracy
```

---

# Model Saving and Loading

Save:

```python
cnn_model.save("cnn_model.keras")
```

Load:

```python
load_model("cnn_model.keras")
```

---

# Making Predictions

Single image prediction performed using:

```python
cnn_model.predict()
```

Class selected using:

```python
np.argmax()
```

---

# Model Evaluation

Performance evaluated using:

## Confusion Matrix

```python
confusion_matrix()
```

Provides:

- True Positives
- False Positives
- False Negatives
- True Negatives

---

## Classification Report

```python
classification_report()
```

Metrics:

- Precision
- Recall
- F1-Score
- Accuracy

---

# Key Concepts Learned

✅ Image Loading

✅ Image Resizing

✅ Image Normalization

✅ Grayscale Conversion

✅ Pixel Manipulation

✅ Color Spaces

✅ Channel Processing

✅ Cropping

✅ Rotation

✅ Flipping

✅ Translation

✅ Drawing Operations

✅ Image Filtering

✅ Thresholding

✅ Edge Detection

✅ Contour Detection

✅ CNN Fundamentals

✅ Convolution Layers

✅ Pooling Layers

✅ Batch Normalization

✅ Dropout Regularization

✅ Adam Optimizer

✅ Early Stopping

✅ Model Checkpointing

✅ Model Serialization

✅ Classification Metrics

---

# Conclusion

This project provides a practical introduction to Computer Vision and Deep Learning. Through OpenCV, various image processing operations such as enhancement, filtering, transformation, and feature extraction were implemented. Using TensorFlow and Keras, a Convolutional Neural Network was built, trained, evaluated, and deployed for image classification tasks.

The project demonstrates the complete pipeline from raw image preprocessing to CNN-based prediction, providing a strong foundation for advanced topics such as object detection, image segmentation, transfer learning, and real-world computer vision applications.
