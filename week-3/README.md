# Week 3: Data Cleaning and Preprocessing

## Overview
This project focuses on cleaning and preprocessing the Adult Census Income dataset from the UCI Machine Learning Repository. The objective is to improve data quality and prepare the dataset for further exploratory data analysis and machine learning.

## Dataset
- **Source:** [UCI Adult Dataset](https://archive.ics.uci.edu/dataset/2/adult)
- **Original rows:** 32,561
- **Columns:** 15
- **Target variable:** `income`

The raw dataset is stored locally and is not included in this repository.

## Tasks Completed
1. Loaded and inspected the dataset using Pandas and NumPy.
2. Identified missing values and duplicate records.
3. Removed 24 duplicate rows.
4. Handled missing categorical values by replacing them with `Unknown`.
5. Standardized categorical text values.
6. Detected potential outliers using the Interquartile Range (IQR) method.
7. Applied one-hot encoding to categorical features.
8. Converted the income target into binary labels (`0` for `<=50K` and `1` for `>50K`).
9. Validated the processed dataset and compared data quality before and after cleaning.

## Results

| Metric | Original | Cleaned | Encoded |
|---|---:|---:|---:|
| Rows | 32,561 | 32,537 | 32,537 |
| Columns | 15 | 15 | 93 |
| Missing values | 4,262 | 0 | 0 |
| Duplicate rows | 24 | 0 | 0 |

## Project Structure

```text
week-3/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── data_cleaning.ipynb
├── outputs/
└── README.md
```

## Output Files
The following files are generated locally and excluded from Git:
- `data/processed/adult_cleaned.csv`
- `data/processed/adult_encoded.csv`

## Tools and Libraries
- Python
- Pandas
- NumPy
- Jupyter Notebook

## How to Run
1. Download the dataset from the UCI repository.
2. Place `adult.data` in `data/raw/`.
3. Open `notebooks/data_cleaning.ipynb` in Jupyter Notebook or VS Code.
4. Select a compatible Python kernel with Pandas and NumPy installed.
5. Run the notebook cells in order.
