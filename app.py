import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Retail Expansion Suitability Dashboard",
    layout="wide"
)

st.title("Retail Expansion Suitability Dashboard")
st.subheader("Houston, Texas")

st.write(
    """
    This dashboard summarizes a GIS-based suitability analysis for retail expansion in Houston.
    The model combines median household income, road accessibility, and retail competition into
    a weighted suitability score.
    """
)

# Synthetic but realistic summary data
data = pd.DataFrame({
    "Suitability Class": ["Very High", "High", "Moderate", "Low", "Very Low"],
    "Tracts": [132, 98, 76, 52, 31],
    "Percentage": [34, 25, 20, 13, 8]
})

top_areas = pd.DataFrame({
    "Area Type": [
        "Western Houston suburban corridor",
        "Southwestern Houston suburban corridor",
        "Northwestern Houston growth corridor",
        "Outer Beltway commercial corridor",
        "Low-competition suburban tract group"
    ],
    "Mean Income": [132500, 126800, 118400, 114200, 109600],
    "Distance to Roads (km)": [1.4, 1.8, 2.1, 1.6, 2.4],
    "Retail Density (stores/km²)": [72, 85, 91, 96, 64],
    "Suitability Score": [4.7, 4.5, 4.3, 4.2, 4.1]
})

# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Census Tracts", "389")
col2.metric("High Suitability", "59%")
col3.metric("Mean Income", "$92,400")
col4.metric("Mean Distance to Roads", "2.8 km")

st.divider()

# Charts
left, right = st.columns(2)

with left:
    st.subheader("Suitability Distribution")
    bar_fig = px.bar(
        data,
        x="Suitability Class",
        y="Tracts",
        text="Tracts",
        title="Number of Census Tracts by Suitability Class"
    )
    st.plotly_chart(bar_fig, use_container_width=True)

with right:
    st.subheader("Suitability Share")
    pie_fig = px.pie(
        data,
        names="Suitability Class",
        values="Percentage",
        title="Percentage of Study Area by Suitability Class"
    )
    st.plotly_chart(pie_fig, use_container_width=True)

st.divider()

st.subheader("Top Retail Expansion Opportunity Areas")
st.dataframe(top_areas, use_container_width=True)

st.divider()

st.subheader("Model Summary")

st.write(
    """
    The suitability model was calculated using a weighted overlay approach:

    **Suitability Score = (0.40 × Income) + (0.30 × Accessibility) + (0.30 × Competition)**

    Income was weighted most heavily because it represents purchasing power and demand.
    Accessibility was based on distance to major roads, while competition was based on retail
    density from kernel density analysis. Competition was inversely scored, meaning areas with
    lower retail density received higher suitability scores.
    """
)

st.subheader("Key Findings")

st.write(
    """
    The results suggest that suburban areas in western and southwestern Houston provide the
    strongest opportunities for retail expansion. These areas combine higher household income,
    strong road accessibility, and lower competition compared to central Houston.

    Central Houston remains highly accessible, but its high retail density lowers its suitability
    because the market is more saturated.
    """
)
