
import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Hotel Booking Analytics",
    page_icon="🏨",
    layout="wide"
)

# Dashboard title

# Professional dashboard styling
st.markdown("""

<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    h1 {
        color: #2DD4BF;
        font-weight: 700;
    }

    [data-testid="stMetric"] {
        background-color: #111827;
        border: 1px solid #374151;
        padding: 16px;
        border-radius: 12px;
    }

    [data-testid="stMetricLabel"] {
        color: #D1D5DB !important;
    }

    [data-testid="stMetricValue"] {
        color: #F9FAFB !important;
    }
</style>

""", unsafe_allow_html=True)

st.title("Hotel Booking Analytics Dashboard")
st.caption(
    "An interactive exploration of booking behavior, "
    "cancellations, and hotel pricing."
)
st.markdown(
    "Use the filters in the sidebar to explore hotel performance "
    "and discover patterns in the booking data."
)


# Load dataset using the working Week 1 environment
DATA_PATH = "data/raw/hotel_bookings.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)
    df["arrival_date"] = pd.to_datetime(
        df["arrival_date_year"].astype(str) + "-" +
        df["arrival_date_month"] + "-01",
        format="%Y-%B-%d",
        errors="coerce"
    )
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

hotel_types = st.sidebar.multiselect(
    "Select hotel type",
    options=sorted(df["hotel"].dropna().unique()),
    default=sorted(df["hotel"].dropna().unique())
)

filtered_df = df[df["hotel"].isin(hotel_types)]

# Summary metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Bookings", f"{len(filtered_df):,}")
col2.metric(
    "Cancellation Rate",
    f"{filtered_df['is_canceled'].mean() * 100:.1f}%"
)
col3.metric(
    "Average Daily Rate",
    f"{filtered_df['adr'].mean():.2f}"
)

st.success(f"Loaded {len(filtered_df):,} bookings successfully.")


st.divider()
st.header("1. Booking Analysis")

# Chart 1: Interactive bar chart
st.subheader("Bookings by Hotel Type")

hotel_counts = (
    filtered_df["hotel"]
    .value_counts()
    .rename_axis("Hotel Type")
    .reset_index(name="Bookings")
)

fig_bar = px.bar(
    hotel_counts,
    x="Hotel Type",
    y="Bookings",
    color="Hotel Type",
    title="Number of Bookings by Hotel Type",
    template="plotly_white",
    hover_data={"Bookings": ":,"}
)

st.plotly_chart(fig_bar, use_container_width=True)

# Chart 2: Interactive pie chart
st.subheader("Booking Cancellation Status")

cancellation_counts = (
    filtered_df["is_canceled"]
    .map({0: "Not Canceled", 1: "Canceled"})
    .value_counts()
    .rename_axis("Status")
    .reset_index(name="Bookings")
)

fig_pie = px.pie(
    cancellation_counts,
    names="Status",
    values="Bookings",
    title="Canceled vs. Non-Canceled Bookings",
    color="Status",
    color_discrete_map={
        "Not Canceled": "#0D9488",
        "Canceled": "#F97316"
    },
    template="plotly_white"
)

st.plotly_chart(fig_pie, use_container_width=True)

st.divider()
st.header("2. Pricing and Booking Trends")

# Chart 3: Line chart - Average daily rate by month
monthly_adr = (
    filtered_df.groupby("arrival_date_month", observed=False)["adr"]
    .mean()
    .reindex([
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ])
    .reset_index()
)

monthly_adr.columns = ["Month", "Average Daily Rate"]

fig_line = px.line(
    monthly_adr,
    x="Month",
    y="Average Daily Rate",
    markers=True,
    title="Average Daily Rate by Arrival Month",
    template="plotly_white"
)
st.plotly_chart(fig_line, use_container_width=True)

# Chart 4: Histogram - Booking lead time
fig_hist = px.histogram(
    filtered_df,
    x="lead_time",
    nbins=40,
    title="Distribution of Booking Lead Time",
    labels={
        "lead_time": "Lead Time (days)",
        "count": "Number of Bookings"
    },
    template="plotly_white"
)
st.plotly_chart(fig_hist, use_container_width=True)

# Chart 5: Scatter plot - Lead time vs daily rate
fig_scatter = px.scatter(
    filtered_df.sample(
        n=min(5000, len(filtered_df)),
        random_state=42
    ),
    x="lead_time",
    y="adr",
    color="is_canceled",
    color_discrete_map={
        0: "#0D9488",
        1: "#F97316"
    },
    labels={
        "lead_time": "Lead Time (days)",
        "adr": "Average Daily Rate",
        "is_canceled": "Cancellation Status"
    },
    title="Booking Lead Time vs. Daily Rate",
    hover_data=["hotel", "arrival_date_month"],
    template="plotly_white"
)
st.plotly_chart(fig_scatter, use_container_width=True)
