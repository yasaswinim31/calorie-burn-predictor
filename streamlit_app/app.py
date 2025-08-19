import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('src/calorie_model.joblib')

st.title("🔥 Calorie Burn Predictor")
...