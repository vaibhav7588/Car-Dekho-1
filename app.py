import streamlit as st
import pandas as pd

st.title("Car Dekho Dataset Viewer")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload your car_dekho.csv file",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    st.subheader("Dataset Preview")
    st.dataframe(df)

    st.subheader("Dataset Information")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    st.subheader("Column Names")
    st.write(df.columns.tolist())

else:
    st.warning("Please upload a CSV file to continue.")

