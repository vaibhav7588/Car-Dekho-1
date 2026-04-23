import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the saved model and encoder
@st.cache_resource
def load_assets():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("owner_encoder.pkl", "rb") as f:
        owner_encoder = pickle.load(f)
    return model, owner_encoder

model, owner_encoder = load_assets()

st.title("🚗 Car Price Predictor")
st.write("Enter the details below to estimate the selling price of the car.")

# Layout
col1, col2 = st.columns(2)

with col1:
    year_old = st.number_input("Age of the Car (years)", min_value=0, max_value=30, value=5)
    km_driven = st.number_input("Kilometers Driven", min_value=0, value=50000)
    mileage = st.number_input("Mileage (kmpl)", min_value=0.0, value=20.0)
    engine = st.number_input("Engine CC", min_value=500, max_value=5000, value=1200)

with col2:
    max_power = st.number_input("Max Power (bhp)", min_value=20.0, value=80.0)
    seats = st.selectbox("Number of Seats", [4, 5, 7, 8, 10], index=1)
    owner = st.selectbox("Owner Type", [
        "First Owner", "Second Owner", "Third Owner",
        "Fourth & Above Owner", "Test Drive Car"
    ])

# Prediction
if st.button("Predict Price"):
    try:
        # ✅ FIX 1: Correct encoding input shape
        owner_encoded = owner_encoder.transform([owner])[0]

        # ✅ FIX 2: Ensure correct datatype
        features = np.array([[ 
            int(km_driven),
            int(owner_encoded),
            int(seats),
            int(year_old),
            float(mileage),
            int(engine),
            float(max_power)
        ]])

        # ✅ Prediction
        prediction = model.predict(features)

        st.success(f"Estimated Selling Price: ₹{round(prediction[0], 2):,}")

        # Debug (optional)
        st.write("Feature Vector:", features)

    except Exception as e:
        st.error(f"Error occurred: {e}")

# Show sample data
if st.checkbox("Show Data Sample"):
    df = pd.read_csv('car_dekho.csv')
    st.dataframe(df.head())