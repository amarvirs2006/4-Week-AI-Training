# Day 19 – Support Vector Machine (SVM) and Naive Bayes

Today, I learned about **Support Vector Machine (SVM)** and **Naive Bayes**, two popular supervised machine learning algorithms. SVM can be used for both classification and regression tasks, while Naive Bayes is mainly used for classification based on probability.

## Topics Learned

* Introduction to Support Vector Machine (SVM)
* Support Vector Classification (SVC)
* Support Vector Regression (SVR)
* Hyperplane
* Support Vectors
* Introduction to Naive Bayes
* Bayes' Theorem
* Applications of Naive Bayes

---

# Support Vector Machine (SVM)

## What is SVM?

Support Vector Machine (SVM) is a supervised machine learning algorithm used for both **classification** and **regression** problems. Its objective is to find the best boundary (called a **hyperplane**) that separates different classes with the maximum possible margin.

### Advantages of SVM

* Works well with high-dimensional data.
* Effective for both linear and non-linear datasets.
* Performs well on small and medium-sized datasets.
* Can be used for both classification and regression.

---

## Hyperplane

A **hyperplane** is the decision boundary that separates different classes in the dataset.

The best hyperplane is the one that provides the **maximum margin** between the classes.

---

## Support Vectors

Support vectors are the data points that lie closest to the hyperplane.

These points determine the position of the decision boundary and play the most important role in training the SVM model.

---

## Support Vector Classification (SVC)

Support Vector Classification is used for classification problems where the output belongs to one of two or more classes.

### Example

```python
from sklearn.svm import SVC

model = SVC()

model.fit(X_train, y_train)
```

---

## Support Vector Regression (SVR)

Support Vector Regression is used to predict continuous numerical values.

### Example

```python
from sklearn.svm import SVR

model = SVR()

model.fit(X_train, y_train)
```

---

# Naive Bayes

## What is Naive Bayes?

Naive Bayes is a supervised machine learning algorithm used mainly for **classification**. It is based on **Bayes' Theorem** and assumes that all features are independent of each other.

Despite this assumption, Naive Bayes performs well in many real-world classification tasks.

---

## Bayes' Theorem

Bayes' Theorem calculates the probability of an event based on prior knowledge.

Commonly, it is written as:

**P(A|B) = (P(B|A) × P(A)) / P(B)**

---

## Advantages of Naive Bayes

* Simple and fast algorithm.
* Easy to implement.
* Works well with high-dimensional data.
* Requires less training data.
* Frequently used in text classification problems.

---

## Applications of Naive Bayes

* Email Spam Detection
* Sentiment Analysis
* Document Classification
* News Categorization
* Medical Diagnosis

---

## Difference Between SVM and Naive Bayes

| Support Vector Machine (SVM)           | Naive Bayes                        |
| -------------------------------------- | ---------------------------------- |
| Used for classification and regression | Mainly used for classification     |
| Finds the best decision boundary       | Uses probability to classify data  |
| Performs well with complex datasets    | Fast and computationally efficient |
| Does not assume feature independence   | Assumes features are independent   |

---

## What I Learned Today

* Learned the concept of Support Vector Machine (SVM).
* Understood the role of hyperplanes and support vectors.
* Learned that SVM can be used for both classification (SVC) and regression (SVR).
* Studied Naive Bayes and its probabilistic approach to classification.
* Learned the basic idea of Bayes' Theorem.
* Compared SVM and Naive Bayes and understood their common applications.
