# Day 20 – Perceptron and Artificial Neural Networks (ANN)

Today, I learned the theoretical concepts of **Perceptron** and **Artificial Neural Networks (ANN)**. I understood how neural networks are structured, the role of different layers, activation functions, loss functions, and optimizers. No practical coding was performed in today's session.

## Topics Learned

* Introduction to Perceptron
* Artificial Neural Networks (ANN)
* Input Layer
* Hidden Layer
* Output Layer
* Activation Functions
* Loss Function
* Optimizer

---

# Perceptron

A **Perceptron** is the simplest type of artificial neural network and serves as the basic building block of deep learning. It receives input values, applies weights, calculates a weighted sum, and produces an output after applying an activation function.

### Components of a Perceptron

* Input values
* Weights
* Bias
* Activation Function
* Output

---

# Artificial Neural Network (ANN)

An **Artificial Neural Network (ANN)** is a machine learning model inspired by the human brain. It consists of interconnected neurons organized into different layers that work together to learn patterns from data.

ANNs are widely used for:

* Image Classification
* Speech Recognition
* Natural Language Processing
* Recommendation Systems
* Medical Diagnosis

---

# Layers in ANN

## Input Layer

* The first layer of the network.
* Receives input features from the dataset.
* Passes the information to the hidden layers.

---

## Hidden Layer

* Performs computations on the input data.
* Learns complex patterns and relationships.
* A neural network may contain one or multiple hidden layers.

---

## Output Layer

* Produces the final prediction.
* The number of neurons depends on the problem being solved.

---

# Activation Functions

Activation functions determine whether a neuron should be activated and introduce non-linearity into the neural network.

## Linear Activation Function

* Produces output proportional to the input.
* Mostly used in regression problems.

---

## Sigmoid Activation Function

* Produces output values between **0 and 1**.
* Commonly used for binary classification.

---

## Tanh Activation Function

* Produces output values between **-1 and 1**.
* Zero-centered and often performs better than Sigmoid in some cases.

---

## ReLU (Rectified Linear Unit)

* Returns the input if it is positive; otherwise returns 0.
* One of the most widely used activation functions in deep learning.

---

## Leaky ReLU

* Similar to ReLU but allows a small negative output instead of returning 0 for all negative values.
* Helps reduce the "dying ReLU" problem.

---

# Loss Function

A **Loss Function** measures the difference between the predicted output and the actual output.

The objective during training is to minimize the loss so that the model makes more accurate predictions.

---

# Optimizer

An **Optimizer** updates the model's weights during training to minimize the loss function.

It helps the neural network learn efficiently by improving the weights after each iteration.

Some commonly used optimizers include:

* Gradient Descent
* SGD (Stochastic Gradient Descent)
* Adam
* RMSProp

---

## What I Learned Today

* Learned the basic concept of a Perceptron.
* Understood the structure of Artificial Neural Networks.
* Studied the roles of the input, hidden, and output layers.
* Learned the purpose of different activation functions.
* Understood how loss functions measure prediction errors.
* Learned that optimizers update model weights to improve learning.
* Gained a theoretical understanding of the fundamentals of deep learning.
