import streamlit as st
import pandas as pd

st.set_page_config(page_title="Car Dekho Dataset Viewer", layout="wide")

st.title("🚗 Car Dekho Dataset Viewer")

# Upload CSV
uploaded_file = st.file_uploader(
    "Upload your car_dekho.csv file",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        # Read CSV safely
        df = pd.read_csv(uploaded_file, encoding="utf-8")

        st.success("✅ File uploaded successfully!")

        # Preview
        st.subheader("📊 Dataset Preview")
        st.dataframe(df, use_container_width=True)

        # Info
        st.subheader("ℹ️ Dataset Information")
        col1, col2 = st.columns(2)
        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])

        # Column names
        st.subheader("🧾 Column Names")
        st.write(list(df.columns))

    except Exception as e:
        st.error("❌ Error reading the file")
        st.write(e)

else:
    st.warning("⚠️ Please upload a CSV file to continue.")


