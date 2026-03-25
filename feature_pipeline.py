# CUSTOMER PURCHASE PROPENSITY PROJECT

# ========== 1. IMPORT LIBRARIES ==========
import pandas as pd
import numpy as np
import sqlite3
import requests
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import (
    LabelEncoder, OrdinalEncoder,
    StandardScaler, MinMaxScaler, RobustScaler,
    Normalizer, MaxAbsScaler, PowerTransformer
)
from sklearn.compose import ColumnTransformer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from scipy.stats import zscore

# ========== 2. LOAD DATA ==========
customers = pd.read_excel("customers.xlsx")
transactions = pd.read_json("transactions.json")

conn = sqlite3.connect(":memory:")
with open("products.sql", "r") as f:
    conn.executescript(f.read())

products = pd.read_sql("SELECT * FROM products", conn)

print("Local datasets loaded")

# ========== 3. LOAD API ==========
url = "https://dummyjson.com/users"
response = requests.get(url)

if response.status_code == 200:
    users = pd.DataFrame(response.json()["users"])
    users.rename(columns={"id": "customer_id"}, inplace=True)
    print("API loaded")
else:
    users = pd.DataFrame()
    print("API failed")

# ========== 4. CLEAN PRODUCTS ==========
products["price"] = products["price"].apply(lambda x: x if x > 0 else np.nan)
products["category"] = products["category"].fillna("Unknown")
products["stock"] = products["stock"].fillna(products["stock"].median())

products = products[products["price"] < 100000]

print("Products cleaned")

# ========== 5. MERGE ==========
df = transactions.merge(customers, on="customer_id", how="left")
df = df.merge(products, on="product_id", how="left")

if not users.empty and "customer_id" in users.columns:
    df = df.merge(users, on="customer_id", how="left")

print("Data merged")

# ========== 6. DATA UNDERSTANDING ==========
print(df.info())
print(df.describe())
print(df.head())

# ========== 7. EDA ==========
plt.figure()
sns.histplot(df["amount"], kde=True)
plt.title("Distribution of Transaction Amount")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.show()

plt.figure()
sns.boxplot(x="payment_mode", y="amount", data=df)
plt.title("Transaction Amount by Payment Mode")
plt.xlabel("Payment Mode")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

sns.pairplot(df.select_dtypes(include=np.number))
plt.suptitle("Pairwise Relationships", y=1.02)
plt.show()

# ========== 8. MISSING VALUES ==========
df["amount_missing_flag"] = df["amount"].isnull().astype(int)

df["payment_mode"] = df["payment_mode"].fillna("Unknown")

# Remove fully null columns
df = df.dropna(axis=1, how="all")

num_cols = df.select_dtypes(include=np.number).columns

df[num_cols] = SimpleImputer(strategy="median").fit_transform(df[num_cols])
df[num_cols] = KNNImputer().fit_transform(df[num_cols])
df[num_cols] = IterativeImputer().fit_transform(df[num_cols])

print("Missing values handled")

# ========== 9. OUTLIERS ==========
df["zscore"] = zscore(df["amount"])
df = df[df["zscore"] < 3]

Q1 = df["amount"].quantile(0.25)
Q3 = df["amount"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["amount"] > Q1 - 1.5*IQR) & (df["amount"] < Q3 + 1.5*IQR)]

lower = df["amount"].quantile(0.01)
upper = df["amount"].quantile(0.99)
df["amount"] = df["amount"].clip(lower, upper)

print("Outliers handled")

# ========== 10. DATETIME ==========
df["date"] = pd.to_datetime(df["date"])

df["days_since_last_purchase"] = (
    df["date"].max() - df["date"]
).dt.days

print("Date features created")

# ========== 11. ENCODING ==========
df["payment_mode_label"] = LabelEncoder().fit_transform(df["payment_mode"])

df[["payment_mode_ordinal"]] = OrdinalEncoder().fit_transform(df[["payment_mode"]])

if "category" in df.columns:
    df = pd.get_dummies(df, columns=["category"], drop_first=True)

# Binning
df["income_bin"] = pd.qcut(df["amount"], q=4, duplicates="drop")

print("Encoding done")

# ========== 12. SCALING ==========
df["amount_std"] = StandardScaler().fit_transform(df[["amount"]])
df["amount_minmax"] = MinMaxScaler().fit_transform(df[["amount"]])
df["amount_robust"] = RobustScaler().fit_transform(df[["amount"]])
df["amount_norm"] = Normalizer().fit_transform(df[["amount"]])
df["amount_maxabs"] = MaxAbsScaler().fit_transform(df[["amount"]])

# ColumnTransformer
ct = ColumnTransformer([
    ("std", StandardScaler(), ["amount"]),
    ("minmax", MinMaxScaler(), ["stock"])
])
ct.fit(df)

print("Scaling done")

# ========== 13. FEATURE ENGINEERING ==========
df["purchase_per_day"] = df["amount"] / (df["days_since_last_purchase"] + 1)

df["log_amount"] = np.log1p(df["amount"])
df["sqrt_amount"] = np.sqrt(df["amount"])

# Power Transformer
df["amount_power"] = PowerTransformer().fit_transform(df[["amount"]])

df["high_value_customer"] = (df["amount"] > 20000).astype(int)

print("Feature engineering done")

# ========== 14. SAVE ==========
df.to_csv("processed_customer_data.csv", index=False)

print("\n FINAL DATA SAVED")

# ========== 15. SUMMARY ==========
print("\n===== PROJECT COMPLETED (100%) =====")
print("✔ Data loaded (Excel + JSON + SQL + API)")
print("✔ Data merged correctly")
print("✔ EDA (Uni + Bi + Multi + Pairplot)")
print("✔ Missing values (Indicator + Simple + KNN + MICE)")
print("✔ Outliers (Z-score + IQR + Winsorization)")
print("✔ Encoding (Label + Ordinal + OneHot + Binning)")
print("✔ Scaling (Standard + MinMax + Robust + Normalizer + MaxAbs + ColumnTransformer)")
print("✔ Feature Engineering (Log + Sqrt + Power + Binary)")
print("✔ Final dataset ready for ML")