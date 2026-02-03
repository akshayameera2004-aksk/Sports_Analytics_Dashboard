import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data/sports_data.csv")

st.title("Sports Analytics Dashboard")

st.subheader("Match Data")
st.dataframe(data)

year = st.selectbox("Select Year", data["Year"].unique())
filtered_data = data[data["Year"] == year]

st.subheader("Filtered Data")
st.table(filtered_data)

fig, ax = plt.subplots()
ax.bar(filtered_data["Team"], filtered_data["Score"])
ax.set_xlabel("Team")
ax.set_ylabel("Score")

st.pyplot(fig)
