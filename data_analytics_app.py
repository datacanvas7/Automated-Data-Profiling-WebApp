# Import Libraries
import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Streamlit App
st.set_page_config(page_title="Automated Data Profiling App", layout="wide")
st.title("📊 Automated Data Profiling App")

# Sidebar - select dataset
dataset_option = st.sidebar.selectbox(
    "Select a sample dataset",
    ["iris", "tips", "penguins"]
)

@st.cache_data
def load_dataset(name):
    if name == "iris":
        return sns.load_dataset("iris")
    elif name == "tips":
        return sns.load_dataset("tips")
    elif name == "penguins":
        return sns.load_dataset("penguins")
    else:
        return None

df = load_dataset(dataset_option)

# Show DataFrame Preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ------------------------------------
# 1️⃣ Pandas Profiling Report
# ------------------------------------
st.subheader("Pandas Profiling Report")
profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
st_profile_report(profile)

# -----------------------------------