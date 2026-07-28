# Day 31 – Facial Emotion Recognition CNN Model

Today, I completed the **Convolutional Neural Network (CNN)** model for our final project, **Facial Emotion Recognition**. The model was built using TensorFlow and Keras and trained on the **FER-2013** dataset. I also learned several techniques to improve model performance, including data augmentation, batch normalization, dropout, callbacks, and learning rate scheduling.

## Project Title

**Facial Emotion Recognition**

---

## Dataset

The model was trained using the **FER-2013** dataset, which contains facial images representing seven different human emotions.

The dataset was divided into:

* Training Dataset
* Testing Dataset

Images were resized to **48 × 48 pixels** before training.

---

## Topics Learned

* Loading Image Dataset
* Data Augmentation
* Image Rescaling
* CNN Architecture
* Convolution Layers
* Batch Normalization
* Max Pooling
* Global Average Pooling
* Dense Layers
* Dropout
* Softmax Activation
* Model Compilation
* Model Checkpoint
* Early Stopping
* Reduce Learning Rate on Plateau
* Model Training

---

# Loading the Dataset

The FER-2013 dataset was loaded using TensorFlow's `image_dataset_from_directory()` function.

### Example

```python
train_dataset = tf.keras.utils.image_dataset_from_directory(
    "train/",
    image_size=(48,48),
    batch_size=32
)
```

---

# Data Augmentation

Data augmentation was used to increase the diversity of training images and reduce overfitting.

The following techniques were applied:

* Random Horizontal Flip
* Random Rotation
* Random Zoom

### Example

```python
data_augmentation = Sequential([
    RandomFlip("horizontal"),
    RandomRotation(0.1),
    RandomZoom(0.1)
])
```

---

# Image Rescaling

Before training, image pixel values were normalized to the range **0–1**.

### Example

```python
Rescaling(1.0 / 255)
```

---

# CNN Architecture

The CNN model consisted of:

* Input Layer
* Three Convolution Blocks
* Batch Normalization
* Max Pooling Layers
* Global Average Pooling Layer
* Two Fully Connected (Dense) Layers
* Dropout Layers
* Output Layer

---

# Convolution Layers

Three convolution blocks were used to extract image features such as edges, textures, and facial patterns.

Each block consisted of:

* Conv2D
* BatchNormalization
* Conv2D
* BatchNormalization
* MaxPooling2D

This architecture allows the network to learn increasingly complex facial features.

---

# Batch Normalization

Batch Normalization was added after each convolution layer to stabilize and speed up training.

### Benefits

* Faster convergence
* Better training stability
* Improved model performance

---

# Max Pooling

Max Pooling was used after each convolution block to reduce feature map dimensions while preserving important information.

---

# Global Average Pooling

Instead of using a Flatten layer, **GlobalAveragePooling2D** was used to reduce the number of trainable parameters and help reduce overfitting.

---

# Dense and Dropout Layers

Two fully connected layers were added before the output layer.

Dropout was applied to reduce overfitting during training.

### Example

```python
Dense(256, activation="relu")
Dropout(0.5)

Dense(128, activation="relu")
Dropout(0.3)
```

---

# Output Layer

The output layer contains **7 neurons**, one for each facial emotion class.

The **Softmax** activation function was used for multi-class classification.

### Example

```python
Dense(7, activation="softmax")
```

---

# Model Compilation

The model was compiled using:

* Optimizer: Adam
* Loss Function: Sparse Categorical Crossentropy
* Evaluation Metric: Accuracy

### Example

```python
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
```

---

# Callbacks

To improve training, three callbacks were used.

## Model Checkpoint

Automatically saves the best-performing model during training.

## Early Stopping

Stops training if the validation loss does not improve for several epochs, helping prevent overfitting.

## Reduce Learning Rate on Plateau

Automatically decreases the learning rate when validation performance stops improving, allowing the model to continue learning effectively.

---

# Model Training

The CNN model was trained for up to **50 epochs** using the training dataset while monitoring validation performance.

### Example

```python
history = model.fit(
    train_dataset,
    validation_data=test_dataset,
    epochs=50,
    callbacks=[checkpoint, early_stop, reduce_lr]
)
```

---

## What I Learned Today

* Built a complete CNN model for the Facial Emotion Recognition project.
* Loaded and prepared the FER-2013 dataset.
* Applied data augmentation to improve model generalization.
* Normalized image pixel values using rescaling.
* Designed a deep CNN with multiple convolution blocks.
* Used Batch Normalization and Max Pooling for better feature extraction.
* Learned the advantage of Global Average Pooling over Flatten.
* Added Dense and Dropout layers to improve classification performance.
* Used Softmax activation for seven-class emotion classification.
* Implemented Model Checkpoint, Early Stopping, and ReduceLROnPlateau callbacks.
* Successfully trained the CNN model for emotion recognition.
