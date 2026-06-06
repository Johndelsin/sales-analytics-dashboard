-- Monthly Sales
SELECT order_month,
ROUND(SUM(sales), 2) AS total_sales

FROM sales
GROUP BY order_month
ORDER BY order_month;

-- Top 5 Products
SELECT "Product Name",
ROUND(SUM(Sales), 2) AS total_sales

FROM sales
GROUP BY "Product Name"
ORDER BY total_sales DESC
LIMIT 5;

-- Sales by Region
SELECT Region,
ROUND(SUM(Sales), 2) AS total_sales

FROM sales
GROUP BY Region
ORDER BY total_sales DESC;

-- Profit by Category
GROUP BY Category
ROUND(SUM(Profit) 2) AS total_Profit
FROM sales
GROUP BY Category
ORDER BY total_profit DESC;

-- Average Order Value
SELECT ROUND(AVG(Sales), 2) AS avg_order_value
FROM sales;