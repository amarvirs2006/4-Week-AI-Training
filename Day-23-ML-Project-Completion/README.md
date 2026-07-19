# Day 23 – Food Health Score Prediction Project Completion

Today, I completed my machine learning project titled **Food Health Score Prediction**. The objective of this project was to predict the **health score of packaged food products** based on their nutritional information using a regression model.

## Project Title

**Food Health Score Prediction**

---

## Project Objective

The aim of this project was to develop a machine learning model capable of predicting the health score of food items by analyzing their nutritional values and food type.

---

## Work Completed

### 1. Loading the Dataset

* Loaded the dataset using Pandas.
* Performed initial exploration of the data.

---

### 2. Feature Selection

To improve the model and remove unnecessary information, several columns that were not useful for prediction were removed, including identifiers, brand information, and descriptive text columns.

Examples of removed columns include:

* `fdc_id`
* `food_name`
* `brand_name`
* `ingredients`
* `brand_owner`
* `food_category`
* `serving_unit`
* `household_serving`
* `vitamin_c_mg`

---

### 3. Splitting the Dataset

The dataset was divided into:

* **Training Set (70%)**
* **Testing Set (30%)**

using Scikit-learn's `train_test_split()` function.

---

### 4. Handling Missing Values

The numerical columns containing missing values were cleaned using **KNN Imputer**.

KNN Imputer estimates missing values based on the nearest neighboring samples, which helps preserve relationships between features.

### Example

```python
from sklearn.impute import KNNImputer

knn = KNNImputer(n_neighbors=5)

X_train[num_cols] = knn.fit_transform(X_train[num_cols])
X_test[num_cols] = knn.transform(X_test[num_cols])
```

---

### 5. Encoding Categorical Data

The **food_type** column was converted into numerical format using **One-Hot Encoding**.

This allows the machine learning model to process categorical values effectively.

### Example

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(
    sparse_output=False,
    handle_unknown="ignore"
)
```

---

### 6. Model Selection

The project uses **Random Forest Regressor**, an ensemble learning algorithm that combines multiple decision trees to make accurate predictions.

### Advantages

* Handles complex datasets well.
* Reduces overfitting.
* Provides good prediction accuracy.
* Works well for regression problems.

### Example

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=100
)

model.fit(X_train, y_train)
```

---

### 7. Model Evaluation

The trained model was evaluated using the **R² Score**, which measures how well the model predicts the target values.

### Example

```python
from sklearn.metrics import r2_score

score = r2_score(y_test, y_pred)
```

A higher R² score indicates better model performance.

---

## Machine Learning Workflow Followed

1. Selected the project.
2. Collected the dataset.
3. Explored the dataset.
4. Removed unnecessary features.
5. Handled missing values using KNN Imputer.
6. Encoded categorical data using One-Hot Encoding.
7. Split the dataset into training and testing sets.
8. Trained a Random Forest Regressor.
9. Evaluated the model using the R² Score.

---

## What I Learned Today

* Completed my first end-to-end machine learning project.
* Applied data preprocessing techniques learned during training.
* Performed feature selection by removing unnecessary columns.
* Used KNN Imputer to handle missing values.
* Applied One-Hot Encoding to categorical features.
* Trained a Random Forest Regressor for prediction.
* Evaluated the model using the R² Score.
* Understood the complete workflow involved in developing a machine learning project.
