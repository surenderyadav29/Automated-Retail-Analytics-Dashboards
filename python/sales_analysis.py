import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA
print("Loading Dataset...")

df = pd.read_csv(
    "data/raw_sales_data.csv",
    sep="\t"
)

print("\nDataset Loaded Successfully\n")

# SHOW DATA
print(df.head())

# DATA INFO
print("\nDataset Info:\n")
print(df.info())

# CHECK MISSING VALUES
print("\nMissing Values:\n")
print(df.isnull().sum())

# DATA CLEANING
print("\nCleaning Data...\n")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values
df.fillna(0, inplace=True)

# Convert date column
df['Order_Date'] = pd.to_datetime(
    df['Order_Date'],
    dayfirst=True
)

print("\nDate Converted Successfully\n")