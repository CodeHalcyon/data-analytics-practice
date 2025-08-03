# Car Price Prediction Project

This repository contains Jupyter Notebooks (`car.ipynb` and `carpriceprediction.ipynb`) dedicated to predicting car prices based on various features. The notebooks demonstrate a complete machine learning workflow, including data loading, preprocessing, exploratory data analysis (EDA), outlier detection, feature engineering, and model training/evaluation using Linear Regression.

## Overview of Contents:

* **Data Loading and Initial Inspection**:
    * Loads the `car.csv` dataset into a pandas DataFrame.
    * Displays general information about the DataFrame, including data types and non-null counts, to understand its structure and identify potential issues.

* **Categorical and Numerical Column Identification**:
    * Automatically identifies and separates columns into `object` (categorical) and non-`object` (numerical) types for streamlined processing.

* **Unique Value and Missing Value Analysis**:
    * Calculates the number of unique values for each categorical column.
    * Computes the percentage of missing values across all relevant columns to assess data completeness.

* **Data Cleaning and Transformation**:
    * **Categorical Mapping**: Converts 'Owner', 'FuelType', and 'Transmission' categorical columns into numerical representations using mapping.
    * **Numerical Extraction and Cleaning**: Cleans 'kmDriven' and 'AskPrice' by removing commas, currency symbols (for 'AskPrice'), and other non-numeric characters, then extracts numerical values and converts them to float.
    * **Missing Value Imputation**: Fills missing values in 'kmDriven' and 'AskPrice' columns with their respective mean values.
    * **Type Conversion**: Ensures 'Age' is an integer and 'AskPrice' is a float for consistent numerical operations.
    * **One-Hot Encoding**: Applies one-hot encoding to 'Brand' and 'model' columns to transform them into a format suitable for machine learning algorithms, dropping the first category to avoid multicollinearity.

* **Outlier Detection (Numerical Columns)**:
    * Utilizes the Interquartile Range (IQR) method to detect outliers in numerical columns ('Year' and 'Age').
    * Calculates and prints the count and percentage of outliers, as well as their lower and upper bounds.
    * Lists the specific outlier data points identified.

* **Exploratory Data Analysis (EDA) - Categorical Features**:
    * **Count Plots**: Generates count plots for the top 10 categories within 'Brand', 'model', 'Transmission', 'Owner', and 'FuelType' to visualize their distribution.
    * **Pie Charts**: For categorical columns with 6 or fewer unique values ('Transmission', 'Owner', 'FuelType'), pie charts are created to illustrate their proportional distribution.

* **Model Training and Evaluation**:
    * **Feature and Target Selection**: Defines the feature matrix `X` (including 'Age', 'kmDriven', 'Owner', and the one-hot encoded 'Brand' and 'model' columns) and the target variable `y` ('AskPrice').
    * **Train-Test Split**: Splits the preprocessed data into 80% training and 20% testing sets to prepare for model training and unbiased evaluation.
    * **Linear Regression Model**: Initializes and trains a `LinearRegression` model using the training data.
    * **Prediction**: Generates predictions on the unseen test set.
    * **Evaluation Metrics**: Evaluates the model's performance using standard regression metrics:
        * **R2 Score**: 0.7923
        * **Mean Absolute Error (MAE)**: 323170.89
        * **Mean Squared Error (MSE)**: 556649080355.21
        * **Root Mean Squared Error (RMSE)**: 746089.19
