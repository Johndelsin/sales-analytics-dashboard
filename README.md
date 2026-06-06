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