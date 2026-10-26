# Week 2: Interactive Hotel Booking Analytics Dashboard

## Project Overview

This project develops an interactive dashboard to explore hotel booking patterns, cancellations, booking lead times, and room pricing. It uses the Hotel Booking Demand dataset and presents insights through interactive charts that are easy for non-technical stakeholders to understand.

## Objectives

- Analyze hotel booking patterns and cancellation behavior.
- Compare City Hotel and Resort Hotel bookings.
- Explore monthly changes in average daily rates.
- Understand booking lead-time distributions.
- Investigate the relationship between lead time, daily rate, and cancellation status.
- Present findings through an interactive dashboard.

## Dataset

**Hotel Booking Demand Dataset**

Source: https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand

The dataset contains 119,390 booking records and 32 columns.

Download the dataset from Kaggle and place `hotel_bookings.csv` in the location specified in the project setup instructions.

## Tools and Technologies

- Python
- Pandas
- Plotly
- Streamlit

## Dashboard Visualizations

The dashboard includes five different chart types:

1. **Bar Chart:** Compares bookings by hotel type.
2. **Pie Chart:** Displays canceled versus non-canceled bookings.
3. **Line Chart:** Shows average daily rate by arrival month.
4. **Histogram:** Displays the distribution of booking lead times.
5. **Scatter Plot:** Explores the relationship between booking lead time and daily rate, with cancellation status represented by color.

The dashboard also includes a hotel-type filter and summary metrics for total bookings, cancellation rate, and average daily rate. Plotly charts support interactive hover details and zooming.

## Installation and Usage

1. Install Python.
2. Clone or download this repository.
3. Open a terminal in the `week-2` directory.
4. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

5. Download the dataset from Kaggle and place it at the configured data path.
6. Run the dashboard:

   ```bash
   streamlit run app.py
   ```

## Key Questions Explored

- Which hotel type receives more bookings?
- What proportion of bookings are canceled?
- How do average daily rates vary by month?
- How far in advance do customers make reservations?
- Is booking lead time associated with daily rates or cancellations?

## Conclusion

This project transforms exploratory data analysis into an interactive dashboard. It enables users to explore booking patterns, compare hotel types, and investigate cancellation and pricing trends using interactive visualizations.

## Project Structure

```text
week-2/
├── app.py
├── README.md
├── requirements.txt
└── data/
    └── raw/
        └── hotel_bookings.csv
```

The dataset and virtual environment should not be committed to GitHub. Users should download the dataset from its original source and install dependencies locally.