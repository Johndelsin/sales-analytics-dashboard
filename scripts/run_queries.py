# Import Libraries
import sqlite3
import pandas as pd

# Open the Connection
conn = sqlite3.connect ("data/sales_analysis.db")

# The Queries Dictionary
queries = {
    "Monthly Sales Trend": """
        SELECT order_month,
            ROUND (SUM(Sales), 2) AS total_sales
        FROM cleaned_Sales
        GROUP BY order_month
        ORDER BY order_month;
""",

    "Top 5 Products": """
        SELECT "Product Name",
            ROUND (SUM(Sales), 2) AS total_sales
        FROM cleaned_sales
        GROUP BY "Product Name"
        ORDER BY total_sales DESC
        LIMIT 5;
""",

    "Sales by Region": """
        SELECT Region,
            ROUND (SUM(Sales), 2) AS total_sales
        FROM cleaned_sales
        GROUP BY Region
        ORDER BY total_sales DESC;
""",

    "Profit by Category": """
        SELECT Category,
            ROUND(SUM(Profit), 2) AS total_profit
        FROM cleaned_sales
        GROUP BY Category
        ORDER BY total_profit DESC;
""",

    "Average Order Value": """
        SELECT ROUND(AVG(Sales), 2) AS avg_order_value
        FROM cleaned_sales;
"""
}
# =========================================
# RUN ALL QUERIES
# =========================================

for query_name, query in queries.items():

    print("\n" + "=" * 50)
    print(f"{query_name}")
    print("=" * 50)

    # Run SQL query
    df = pd.read_sql_query(query, conn)

    # Display results
    print(df)

    # Save results to CSV
    file_name = query_name.lower().replace(" ", "_") + ".csv"

    df.to_csv(f"data/{file_name}", index=False)

    print(f"\nSaved to data/{file_name}")

# =========================================
# CLOSE CONNECTION
# =========================================

conn.close()

print("\nAll queries executed successfully!")

# The Loop Setup
# Visual Formatting
# Fetching the Data
# Displaying the Result
# Creating the File Name
# Saving to the Computer
# Loop Status Confirmation
# Cleanup