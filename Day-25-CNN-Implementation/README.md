# Day 25 – CNN Implementation

Today, I learned how to implement a **Convolutional Neural Network (CNN)** using TensorFlow and Keras. The model was trained on a **Cat vs Dog image classification dataset**. I understood the complete workflow from loading image datasets to training a CNN model for binary image classification.

## Topics Learned

* Loading Image Dataset
* Image Preprocessing
* Image Normalization
* Convolution Layer (Conv2D)
* Batch Normalization
* Max Pooling Layer
* Flatten Layer
* Dense Layers
* Dropout Layer
* Binary Classification
* Model Compilation
* Model Training

---

# Project Overview

The objective of today's implementation was to classify images into two categories:

* Cat
* Dog

The dataset was divided into:

* Training Dataset
* Validation Dataset

---

# Loading the Dataset

The image dataset was loaded directly from folders using TensorFlow's `image_dataset_from_directory()` function.

### Example

```python
train_ds = tf.keras.utils.image_dataset_from_directory(
    "dataset/train",
    image_size=(256,256),
    batch_size=32
)
```

This function automatically assigns labels based on the folder names.

---

# Image Preprocessing

Before training, all image pixel values were normalized by dividing them by **255** so that the pixel values lie between **0 and 1**.

### Example

```python
def process(image, label):
    image = tf.cast(image / 255., tf.float32)
    return image, label
```

Normalization helps the neural network train faster and improves model stability.

---

# Building the CNN Model

A CNN model was created using TensorFlow's **Sequential API**.

The architecture consisted of:

* Three Convolution Layers
* Three Batch Normalization Layers
* Three Max Pooling Layers
* Flatten Layer
* Two Dense Layers
* Dropout Layers
* Output Layer

---

# Convolution Layer (Conv2D)

Convolution layers extract important image features such as edges, textures, and shapes.

### Example

```python
model.add(Conv2D(
    filters=32,
    kernel_size=(3,3),
    activation="relu"
))
```

---

# Batch Normalization

Batch Normalization normalizes the outputs of each layer, making training faster and improving model stability.

### Example

```python
model.add(BatchNormalization())
```

---

# Max Pooling Layer

Max Pooling reduces the size of feature maps while preserving important information.

### Example

```python
model.add(MaxPooling2D(pool_size=(2,2)))
```

---

# Flatten Layer

The Flatten layer converts the extracted feature maps into a one-dimensional vector before passing them to the fully connected layers.

### Example

```python
model.add(Flatten())
```

---

# Dense Layers

Dense layers learn high-level patterns from the extracted features before making the final prediction.

### Example

```python
model.add(Dense(128, activation="relu"))
```

---

# Dropout Layer

Dropout randomly disables a fraction of neurons during training to reduce overfitting.

### Example

```python
model.add(Dropout(0.1))
```

---

# Output Layer

Since the problem involves two classes (Cat and Dog), the output layer contains one neuron with the **Sigmoid** activation function.

### Example

```python
model.add(Dense(1, activation="sigmoid"))
```

---

# Compiling the Model

The CNN model was compiled using:

* Optimizer: **Adam**
* Loss Function: **Binary Crossentropy**
* Metric: **Accuracy**

### Example

```python
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
```

---

# Training the Model

The CNN model was trained using the training dataset and validated on the validation dataset.

### Example

```python
model.fit(
    train_ds,
    epochs=10,
    validation_data=val_ds
)
```

---

## What I Learned Today

* Learned how to load image datasets using TensorFlow.
* Understood image preprocessing and normalization.
* Built a CNN model using the Sequential API.
* Implemented Conv2D, Batch Normalization, and Max Pooling layers.
* Learned the purpose of Flatten, Dense, and Dropout layers.
* Used the Sigmoid activation function for binary image classification.
* Compiled and trained a CNN model using the Adam optimizer and Binary Crossentropy loss function.
* Gained practical experience in implementing a complete CNN for image classification.
