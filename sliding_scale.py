import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set up the Streamlit interface
st.title("Interactive Sliding Scale: Yearly Meat Spending with Inflation")

# Instructions
st.write("Use the slider below to adjust your weekly meat spending and see how inflation impacts yearly costs.")

# User input: Weekly meat spending using a slider
weekly_spending = st.slider("Select your weekly spending on meat ($):", min_value=30, max_value=250, step=1, value=100)

# Define inflation rate (8% per year)
inflation_rate = 0.08
weeks_per_year = 52

# Compute yearly spending for each year
year_1_spending = weekly_spending * weeks_per_year
year_2_spending = year_1_spending * (1 + inflation_rate)
year_3_spending = year_2_spending * (1 + inflation_rate)

# Display results
st.subheader("Projected Yearly Spending:")
st.metric(label="Year 1 (No Inflation)", value=f"${year_1_spending:,.2f}")
st.metric(label="Year 2 (8% Inflation)", value=f"${year_2_spending:,.2f}")
st.metric(label="Year 3 (8% Inflation)", value=f"${year_3_spending:,.2f}")

# Create a DataFrame for visualization
data = pd.DataFrame({
    "Year": [2025, 2026, 2027],
    "Total Spending ($)": [year_1_spending, year_2_spending, year_3_spending]
})

# Plot the spending trend
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(data["Year"], data["Total Spending ($)"], marker="o", linestyle="-", color="blue", label="Yearly Spending")
ax.set_xlabel("Year")
ax.set_ylabel("Total Spending ($)")
ax.set_title("Projected Yearly Meat Spending Over 3 Years")
ax.legend()
plt.grid(True, linestyle="--", alpha=0.5)

# Display the graph
st.pyplot(fig)

# Add footer
st.write("This tool helps visualize how inflation affects meat spending. Adjust your budget accordingly!")
