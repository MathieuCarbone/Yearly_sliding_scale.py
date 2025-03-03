import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set up the Streamlit interface
st.title("Interactive Sliding Scale: Yearly Meat Spending with Inflation")

# Instructions
st.write("Use the slider below to adjust your weekly meat spending and see how inflation impacts yearly costs in real-time.")

# User input: Weekly meat spending using a slider
weekly_spending = st.slider("Select your weekly spending on meat ($):", min_value=30, max_value=250, step=1, value=100, key='slider')

# Define inflation rate (5% per year)
inflation_rate = 0.08
weeks_per_year = 52

# Compute yearly spending for each year
yearly_spending = [weekly_spending * weeks_per_year]
for i in range(2):  # Compute for year 2 and 3 with inflation
    yearly_spending.append(yearly_spending[-1] * (1 + inflation_rate))

# Display results dynamically with adaptive columns
st.subheader("Projected Yearly Spending:")
columns = st.columns(len(yearly_spending))
for i, col in enumerate(columns):
    col.metric(label=f"Year {i+1}", value=f"${yearly_spending[i]:,.2f}")

# Create a DataFrame for visualization
data = pd.DataFrame({
    "Year": [2025, 2026, 2027],
    "Total Spending ($)": yearly_spending
})

# Add footer
st.write("This tool helps visualize how inflation affects meat spending dynamically. Adjust your budget accordingly!")
