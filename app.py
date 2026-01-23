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

# Create two columns for a better layout
col1, col2 = st.columns(2)

with col1:
    year_old = st.number_input("Age of the Car (years)", min_value=0, max_value=30, value=5)
    km_driven = st.number_input("Kilometers Driven", min_value=0, value=50000)
    mileage = st.number_input("Mileage (kmpl)", min_value=0.0, value=20.0)
    engine = st.number_input("Engine CC", min_value=500, max_value=5000, value=1200)

with col2:
    max_power = st.number_input("Max Power (bhp)", min_value=20.0, value=80.0)
    seats = st.selectbox("Number of Seats", [4, 5, 7, 8, 10], index=1)
    owner = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])

# Prepare input for prediction
# Note: The order of features must match the order used during model training
if st.button("Predict Price"):
    # Encode the owner input
    owner_encoded = owner_encoder.transform([[owner]])[0]
    
    # Feature vector based on dataset columns
    features = np.array([[km_driven, owner_encoded, seats, year_old, mileage, engine, max_power]])
    
    prediction = model.predict(features)
    
    st.success(f"Estimated Selling Price: ₹{round(prediction[0], 2):,}")

# Display data statistics if requested
if st.checkbox("Show Data Sample"):
    df = pd.read_csv('car_dekho.csv')
    st.dataframe(df.head())