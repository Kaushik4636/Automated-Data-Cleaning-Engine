# Automated Data Cleaning Engine 

A robust Python-based tool designed to transform "dirty" raw data into model-ready datasets. 

## Key Features
- **Automated Imputation:** Handles missing numerical values using Median filling.
- **Categorical Encoding:** Automatically maps text features (like Gender/Port) to numerical values.
- **Noise Reduction:** Drops statistically insignificant columns and handles "Unknown" strings as NaN.
- **Outlier Detection:** (Optional) Z-score filtering for statistical cleaning.

## How to Use
1. Clone the repo.
2. Run `python main.py` to process the Titanic dataset.
3. Check `titanic_ready.csv` for the output.

## Tech Stack
- Python 3.x
- Pandas & NumPy
