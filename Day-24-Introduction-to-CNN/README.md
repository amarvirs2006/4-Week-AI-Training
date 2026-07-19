# Day 24 – Introduction to Convolutional Neural Networks (CNN)

Today, I learned the basic concepts of **Convolutional Neural Networks (CNNs)**. The session focused on understanding the architecture of CNNs, how they process image data, and the purpose of each layer. No practical coding was performed today.

## Topics Learned

* Introduction to CNN
* Why CNN is Used
* Image Representation
* Convolution Layer
* Filters (Kernels)
* Feature Maps
* Activation Function
* Pooling Layer
* Fully Connected Layer
* Applications of CNN

---

## What is CNN?

A **Convolutional Neural Network (CNN)** is a type of deep learning model mainly used for processing image data. Unlike traditional neural networks, CNNs automatically learn important features from images, making them highly effective for computer vision tasks.

---

## Why CNN is Used?

CNNs are widely used because they can automatically detect patterns, edges, textures, and shapes in images without requiring manual feature extraction.

### Advantages of CNN

* Automatically extracts image features.
* Reduces the need for manual feature engineering.
* Provides high accuracy in image-related tasks.
* Efficient for large image datasets.

---

## Image Representation

A digital image is made up of tiny units called **pixels**.

* A grayscale image contains one value per pixel.
* A color image is represented using three channels:

  * Red (R)
  * Green (G)
  * Blue (B)

These pixel values are used as input to the CNN.

---

## Convolution Layer

The **Convolution Layer** is the first important layer in a CNN. It applies small filters (kernels) to the input image to detect important features such as edges, corners, and textures.

---

## Filters (Kernels)

A **filter** or **kernel** is a small matrix that slides over the image during the convolution operation.

Different filters detect different types of features, such as:

* Horizontal edges
* Vertical edges
* Corners
* Patterns
* Textures

---

## Feature Maps

The output generated after applying a filter is called a **feature map**.

Feature maps highlight the important features extracted from the input image.

---

## Activation Function

After convolution, an activation function such as **ReLU (Rectified Linear Unit)** is applied.

ReLU introduces non-linearity into the network and helps the model learn more complex patterns.

---

## Pooling Layer

The **Pooling Layer** reduces the size of feature maps while preserving the most important information.

The most commonly used pooling technique is **Max Pooling**, which selects the maximum value from each region.

### Benefits of Pooling

* Reduces computation.
* Decreases memory usage.
* Helps reduce overfitting.
* Retains important image features.

---

## Fully Connected Layer

After several convolution and pooling operations, the extracted features are passed to one or more **Fully Connected Layers**.

These layers use the extracted features to perform the final classification or prediction.

---

## Applications of CNN

CNNs are commonly used in:

* Image Classification
* Face Recognition
* Object Detection
* Medical Image Analysis
* Handwriting Recognition
* Self-Driving Cars

---

## What I Learned Today

* Learned the basic architecture of a Convolutional Neural Network (CNN).
* Understood why CNNs are widely used for image processing tasks.
* Learned the roles of convolution layers, filters, and feature maps.
* Understood how pooling reduces the size of feature maps.
* Learned the purpose of fully connected layers in making final predictions.
* Explored some real-world applications of CNNs.
