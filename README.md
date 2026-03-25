# Customer Purchase Propensity  
### Data Cleaning & Feature Engineering Pipeline

---

## Project Overview

This project focuses on building a **complete data preprocessing and feature engineering pipeline** for an e-commerce dataset.

The goal is to prepare raw data for a future **Machine Learning model** that predicts whether a customer will make a purchase.

> Note: This project does NOT include model training. It focuses entirely on **data preprocessing and feature engineering**.

---

## Objective

- Clean and preprocess raw data from multiple sources  
- Perform exploratory data analysis (EDA)  
- Handle missing values and outliers  
- Apply encoding and scaling techniques  
- Create meaningful features  
- Generate a final ML-ready dataset  

---

## Data Sources

The project uses multiple real-world data formats:

- **Excel** → `customers.xlsx` (customer details)  
- **JSON** → `transactions.json` (transaction data)  
- **SQL** → `products.sql` (product information)  
- **API** → `https://dummyjson.com/users` (additional user data)  

---

## Data Pipeline Flow

Transactions (Main Data)  
↓  
Merge Customers (customer_id)  
↓  
Merge Products (product_id)  
↓  
Merge API Data (customer_id)  
↓  
Data Cleaning & Feature Engineering  
↓  
Final Dataset → processed_customer_data.csv  

---

## Exploratory Data Analysis (EDA)

- **Univariate Analysis**
  - Distribution of transaction amount  

- **Bivariate Analysis**
  - Payment mode vs transaction amount  

- **Multivariate Analysis**
  - Correlation heatmap  
  - Pairplot (feature relationships)  

---

## Data Preprocessing

### Missing Values Handling
- Simple Imputer (Median)  
- KNN Imputer  
- MICE (Iterative Imputer)  
- Missing Indicator Feature  

---

### Outlier Handling
- Z-score Method  
- IQR Method  
- Winsorization (capping extreme values)  

---

### Date & Time Features
- Converted date to datetime  
- Created:
  - `days_since_last_purchase`  

---

## Encoding Techniques

- Label Encoding  
- One-Hot Encoding  
- Ordinal Encoding  
- Binning (income groups)  

---

## Feature Scaling

- StandardScaler  
- MinMaxScaler  
- RobustScaler  
- Normalizer  
- MaxAbsScaler  
- ColumnTransformer  

---

## Feature Engineering

- `purchase_per_day`  
- Log Transformation  
- Square Root Transformation  
- Power Transformation  
- Binary Feature (`high_value_customer`)  

---

## Final Output

- Cleaned dataset:  
  `processed_customer_data.csv`  

---

## Key Insights

- Transaction data is **right-skewed**  
- Extreme outliers exist (₹100K+ transactions)  
- Data contains **missing values and inconsistencies**  
- Feature transformations improved data distribution  
- Multi-source data integration simulates real-world pipelines  

---

## Tech Stack

- Python
- Pandas  
- NumPy  
- Scikit-learn  
- Seaborn & Matplotlib  
- SQLite  
- Requests (API)  
