import streamlit as st
import pandas as pd
import joblib
import numpy as np

model = joblib.load('fare_predictor.pkl')

st.title("Fair Price Predictor")
st.write("Estimate a fair fare for your trip before you book.")

distance_km = st.number_input("Trip Distance (km)", min_value=0.1, value=5.0)
passenger_count = st.slider("Number of Passengers", 1, 6, 1)
hour = st.slider("Hour of Day (0-23)", 0, 23, 12)
is_weekend = st.selectbox("Is it a weekend?", ["No", "Yes"])
is_weekend_val = 1 if is_weekend == "Yes" else 0

input_data = pd.DataFrame({
    'distance_km': [distance_km],
    'passenger_count': [passenger_count],
    'hour': [hour],
    'is_weekend': [is_weekend_val]
})

if st.button("Predict Fair Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Fair Price: ${prediction:.2f}")