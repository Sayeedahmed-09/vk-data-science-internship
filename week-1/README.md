
# Hotel Booking Demand — Exploratory Data Analysis (EDA)

## Project Overview

This project performs Exploratory Data Analysis (EDA) on the Hotel Booking Demand dataset to identify patterns in hotel bookings, cancellations, customer behavior, and pricing.

The analysis uses Python, Pandas, Matplotlib, Seaborn, and Jupyter Notebook.

## Dataset

- **Dataset:** Hotel Booking Demand
- **Source:** [Kaggle — Hotel Booking Demand](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)
- **Records:** 119,390 bookings
- **Columns:** 32

### Download Instructions

1. Download the dataset from the Kaggle link above.
2. Extract the downloaded files.
3. Place `hotel_bookings.csv` inside the `data/raw/` directory.

Expected file path: `data/raw/hotel_bookings.csv`

## Objectives

- Understand the dataset structure, dimensions, data types, and memory usage.
- Identify and analyze missing values.
- Calculate numerical summary statistics.
- Examine categorical variable frequencies.
- Visualize booking cancellations, hotel types, daily rates, seasonal patterns, lead times, and numerical correlations.
- Summarize key findings from the analysis.

## Tools and Libraries

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
week-1/
├── data/
│   └── raw/
│       └── hotel_bookings.csv
├── Hotel_Booking_Demand_EDA.ipynb
├── .gitignore
└── README.md
```

## Key Findings

1. Non-canceled bookings are more common than canceled bookings.
2. City Hotels received approximately twice as many bookings as Resort Hotels.
3. Average daily rates generally increased from January to August and then declined toward November.
4. Canceled bookings generally had longer lead times than non-canceled bookings.
5. The `company` column contained the highest proportion of missing values, at 94.31%.

## Conclusion

The analysis reveals useful patterns in booking cancellations, hotel preferences, seasonal pricing, and booking lead times. These findings provide a foundation for further analysis of hotel booking behavior and pricing strategies.

## How to Run

1. Clone or download this repository.
2. Install Python and Jupyter Notebook.
3. Install the required libraries:

   ```bash
   py -m pip install jupyter ipykernel pandas matplotlib seaborn
   ```

4. Download the dataset from Kaggle and place it at `data/raw/hotel_bookings.csv`.
5. Open `Hotel_Booking_Demand_EDA.ipynb` in VS Code or Jupyter Notebook.
6. Select the appropriate Python kernel and run all cells.

## Author

EDA project completed as part of an internship assignment.
