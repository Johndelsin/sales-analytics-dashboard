import pandas as pd

#Load dataset
df = pd.read_csv(r"C:\Users\johnd\OneDrive\Desktop\sales-analysis-project\data\Sample - Superstore.csv", encoding="latin1")
df = df.drop_duplicates()

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Create order_month column
df["order_month"] = df["Order Date"].dt.strftime("%Y-%m")

# Create profit_margin column
df["profit_margin"] = df["Profit"] / df["Sales"]

# Handle missing values
df = df.dropna()

# Save cleaned dataset
df.to_csv("data/cleaned_sales.csv", index=False)

print("Data cleaned successfully!")
print(df.head())

import pandas as pd
from sqlalchemy import create_engine

# creating the database file inside the 'data' folder
engine = create_engine('sqlite:///data/sales_analysis.db')
df.to_sql('cleaned_sales', con=engine, if_exists="replace", index=False)

print("Data saved to data/sales_analysis.db!")
