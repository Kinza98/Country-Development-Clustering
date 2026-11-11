
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Country Development Clustering",
    layout="wide"
)

st.title("🌍 Country Development Clustering")
st.write("Explore countries grouped by their socioeconomic indicators.")

# Load dataset
df = pd.read_csv("Country-data-clustered.csv")

st.header("Dataset Overview")

st.write("Complete dataset:")
st.dataframe(df)

st.write("Dataset Shape:", df.shape)

st.header("Cluster Distribution")

cluster_counts = df["clusters"].value_counts()

st.bar_chart(cluster_counts)

st.header("Cluster Statistics")

cluster_summary = df.groupby("clusters")[[
    "child_mort",
    "income",
    "gdpp",
    "life_expec",
    "health",
    "inflation",
    "total_fer"
]].mean().round(2)

st.dataframe(cluster_summary)
# Select a country
country = st.selectbox(
    "Select a country",
    sorted(df["country"].unique())
)

# Display selected country
selected = df[df["country"] == country].iloc[0]

st.subheader(country)

col1, col2, col3 = st.columns(3)

col1.metric("Income", f"{selected['income']:,.0f}")
col2.metric("GDP per capita", f"{selected['gdpp']:,.0f}")
col3.metric("Life expectancy", f"{selected['life_expec']:.1f} years")

# World map
fig = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="clusters",
    hover_name="country",
    title="Countries by KMeans Cluster",
    color_discrete_sequence=px.colors.qualitative.Set2
)

st.plotly_chart(fig, use_container_width=True)
