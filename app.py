import streamlit as st
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
import joblib

try:
    model = joblib.load('model.pkl')
except FileNotFoundError:
    st.error("Error: catboost_model.pkl not found. Please ensure the model file is in the same directory.")
    st.stop()

st.title('Bitcoin Price Prediction')

st.write("Enter the current day's closing price to get a prediction for the next day.")

current_price = st.slider('Current Closing Price:', min_value=0.0, max_value=100000.0, value=30000.0, format="%.2f")

if st.button('Predict'):
    if current_price:
        input_data = np.array([[current_price]])
        predicted_price = model.predict(input_data)
        st.write(f'The predicted price for the next day is: {predicted_price[0]:.2f}')
    else:

        st.warning('Please enter a current closing price.')
