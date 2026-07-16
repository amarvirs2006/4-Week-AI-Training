# Day 22 – Machine Learning Project Selection and Data Preprocessing

Today, our instructor asked us to select a machine learning project and begin working on it by performing the initial stages of the machine learning pipeline, including dataset collection, exploration, preprocessing, and cleaning.

After exploring different ideas, I selected the following project:

## Project Title

**Food Health Score Prediction**

### Project Objective

The goal of this project is to build a machine learning model that predicts the **health score of packaged food products** based on their nutritional information and other available features. This project aims to help users better understand the nutritional quality of food items through data-driven predictions.

---

## Work Completed Today

### 1. Project Selection

* Selected **Food Health Score Prediction** as the final machine learning project.

### 2. Dataset Collection

* Searched for a suitable dataset related to packaged food products.
* Downloaded the dataset for the project.

### 3. Dataset Exploration

Performed some initial analysis to understand the dataset.

The following tasks were completed:

* Loaded the dataset using Pandas.
* Checked the dataset shape.
* Viewed the available columns.
* Inspected the dataset information.
* Checked for missing values.

---

## Data Preprocessing

The next step was cleaning the dataset.

### Handling Missing Values

The dataset contained missing values in several numerical columns.

To handle these missing values, I used the **KNN Imputer**, which estimates missing values based on the values of the nearest neighboring samples instead of replacing them with simple statistics such as the mean or median.

This approach helps preserve relationships between features and often provides better imputations for machine learning datasets.

---

## What I Learned Today

* Selected a real-world machine learning project.
* Collected a suitable dataset for the project.
* Explored the dataset to understand its structure.
* Identified missing values in the dataset.
* Learned how to handle numerical missing values using **KNN Imputer**.
* Completed the initial data preprocessing required before model development.

The next steps of the project will include feature engineering, encoding, feature selection, model training, evaluation, and prediction.
