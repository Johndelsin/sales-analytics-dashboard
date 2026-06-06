# Sales Analytics Dashboard

## Overview

This project analyzes retail sales data using Python, SQL, SQLite, and Power BI.

## Tech Stack

- Python
- Pandas
- Kaggle API
- SQLite
- SQL
- Power BI

## Data Pipeline

Raw Data → Data Cleaning → SQLite Database → SQL Analysis → Power BI Dashboard

## Dashboard Preview

See `screenshots/dashboard.png`

## Key Insights
Key Insights
1. Revenue Growth

Sales increased steadily between 2014 and 2017, indicating consistent business growth. Revenue grew from approximately $0.48M in 2014 to $0.75M in 2017, demonstrating expanding customer demand and market reach.

2. Regional Performance

The West region generated the highest revenue and remains the company's strongest market. Conversely, the South region produced the lowest sales performance, suggesting opportunities for targeted growth initiatives.

3. Customer Segment Analysis

The Consumer segment generated approximately $1.16M in sales and $134K in profit, making it both the largest and most profitable customer group. This indicates that Consumer customers are the primary revenue drivers of the business.

4. Product Performance

The Canon imageCLASS 2200 Advanced Copier emerged as both the highest-selling and most profitable product, generating over $25K in profit. This product demonstrates strong demand while maintaining healthy profitability.

5. Category Profitability

Technology was the most profitable category, outperforming Furniture and Office Supplies. This suggests that technology products contribute significantly to overall business profitability.

6. Business Profitability

The business generated approximately $2.30M in sales and $286K in profit, resulting in an estimated profit margin of 12.5%, indicating healthy overall performance.

## Business Recommendations

### Recommendation 1

Increase investment in the West region by replicating successful sales strategies across other markets.

### Recommendation 2

Prioritize marketing and inventory planning for the Canon imageCLASS 2200 Advanced Copier due to its strong contribution to both revenue and profit.

### Recommendation 3

Continue focusing on Consumer customers through targeted promotions and retention strategies, as they represent the most valuable customer segment.

### Recommendation 4

Investigate the causes of lower sales performance in the South region and evaluate opportunities for localized campaigns or product adjustments.

### Sales by Segment

| Segment | Sales |
|----------|----------:|
| Consumer | $1,161,401 |
| Corporate | $706,146 |
| Home Office | $429,653 |

### Profit by Segment

| Segment | Profit |
|----------|----------:|
| Consumer | $134,119 |
| Corporate | $91,979 |
| Home Office | $60,299 |

### Top Profitable Product

Canon imageCLASS 2200 Advanced Copier generated approximately $25,200 profit.

## Folder Structure

```text
sales-analysis-project/
├── dashboard/
├── data/
├── screenshots/
├── scripts/
├── sql/
└── README.md
```

## How to Run

1. Download data using Kaggle API
2. Run `clean_data.py`
3. Run `run_queries.py`
4. Open Power BI dashboard

## Future Improvements

* Build automated ETL pipelines using Airflow.
* Migrate the project from SQLite to PostgreSQL.
* Implement Bronze, Silver, and Gold data layers.
* Introduce data quality monitoring and validation checks.
* Develop forecasting models for future sales prediction.
* Incorporate A/B testing analysis for marketing experiments.
* Deploy analytics APIs using FastAPI.
