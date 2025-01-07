import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Summary Page",
    page_icon="👋",
)

st.title("Summary Page")

st.subheader("Summary of the data")

expander_bar = st.expander("Click to expand")
expander_bar.write("This is a test")


def display_metrics():
    # Create three columns for the metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="World EV Sales",
            value=f"{current_year_sales:,}",  # Format with commas for thousands
            delta=f"{sales_delta:,}",
            delta_color="normal"  # "normal" for green-red, "inverse" for red-green
        )

    with col2:
        st.metric(
            label="EV Sales Growth",
            value=f"{growth_rate:.1f}%",  # Format as percentage with 1 decimal
            delta=f"{growth_delta:.1f}%",
            delta_color="normal"
        )

    with col3:
        st.metric(
            label="Charging Points",
            value=f"{current_charging_points:,}",
            delta=f"{charging_points_delta:,}",
            delta_color="normal"
        )

