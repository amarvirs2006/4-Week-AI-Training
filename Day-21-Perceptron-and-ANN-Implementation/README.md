# Day 21 – Perceptron and Artificial Neural Network (ANN) Implementation

Today, I implemented both a **Perceptron** model and an **Artificial Neural Network (ANN)** using the **Iris dataset**. I learned how to preprocess data, encode categorical labels, scale features, build neural networks using TensorFlow/Keras, evaluate model performance, save trained models, and make predictions on new data.

## Topics Learned

* Iris Dataset
* Data Preprocessing
* Label Encoding
* Feature Scaling
* Perceptron Classifier
* Artificial Neural Network (ANN)
* Dense Layers
* ReLU Activation Function
* Softmax Activation Function
* Model Training
* Model Evaluation
* Saving and Loading Models
* Prediction on New Data

---

# Dataset

The **Iris dataset** was used for classification.

The target variable was **species**, which contains three flower classes.

---

# Data Preprocessing

Before training the models, the dataset was prepared by:

* Separating input and output variables.
* Encoding categorical labels.
* Splitting the dataset into training and testing sets.
* Scaling numerical features.

---

## Label Encoding

The species names were converted into numerical labels using **LabelEncoder**.

### Example

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

y = encoder.fit_transform(y)
```

---

## Feature Scaling

The features were standardized using **StandardScaler**.

### Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
```

---

# Perceptron

A Perceptron is a single-layer neural network used for classification.

### Training the Model

```python
from sklearn.linear_model import Perceptron

perceptron = Perceptron(max_iter=1000)

perceptron.fit(x_train, y_train)
```

---

## Model Evaluation

The Perceptron model was evaluated using **Accuracy Score** and **Classification Report**.

### Example

```python
from sklearn.metrics import accuracy_score

accuracy_score(y_test, y_pred)
```

---

# Artificial Neural Network (ANN)

An ANN was built using TensorFlow's **Sequential** model.

The network consisted of:

* Input Layer
* Hidden Layer (16 neurons)
* Hidden Layer (8 neurons)
* Output Layer (3 neurons)

---

## Activation Functions Used

* **ReLU** for hidden layers.
* **Softmax** for the output layer.

---

## Building the ANN

### Example

```python
model = Sequential([
    Input(shape=(4,)),
    Dense(16, activation="relu"),
    Dense(8, activation="relu"),
    Dense(3, activation="softmax")
])
```

---

## Compiling the Model

The ANN was compiled using:

* Optimizer: **Adam**
* Loss Function: **Categorical Crossentropy**
* Metric: **Accuracy**

### Example

```python
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
```

---

## Training the Model

The model was trained for **100 epochs**.

### Example

```python
model.fit(
    x_train,
    y_train,
    epochs=100,
    batch_size=8,
    validation_split=0.2
)
```

---

## Evaluating the ANN

The trained model was evaluated using the testing dataset.

### Example

```python
loss, accuracy = model.evaluate(x_test, y_test)
```

---

## Saving and Loading the Model

The trained ANN model was saved and later loaded for prediction.

### Example

```python
model.save("ann_model.h5")
```

```python
from tensorflow.keras.models import load_model

model = load_model("ann_model.h5")
```

---

## Making Predictions

A new flower sample was provided to the trained model to predict its species.

The input was first scaled and then passed to the ANN model for prediction.

---

## What I Learned Today

* Implemented a Perceptron classifier using Scikit-learn.
* Learned how to preprocess the Iris dataset.
* Used Label Encoding for categorical labels.
* Standardized features using StandardScaler.
* Built an Artificial Neural Network using TensorFlow and Keras.
* Used Dense layers with ReLU and Softmax activation functions.
* Trained and evaluated the ANN model.
* Saved and loaded the trained model.
* Predicted the species of a new flower sample using the trained ANN.
