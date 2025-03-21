import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("calories_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit UI setup
st.set_page_config(layout="wide")
st.title("Personal Fitness Tracker")
st.write("Adjust the sliders to predict calories burned during exercise.")

# Create columns for layout
col1, col2 = st.columns([1, 1])

# Left Column - Input Sliders
with col1:
    st.header("Input Parameters")
    age = st.slider("Age", 10, 100, 30)
    bmi = st.slider("BMI", 15, 40, 24)
    duration = st.slider("Duration (minutes)", 0, 35, 15)
    heart_rate = st.slider("Heart Rate", 60, 130, 80)
    body_temp = st.slider("Body Temperature (°C)", 36, 42, 38)
    gender = st.radio("Gender", ("Male", "Female"))
    gender_value = 0 if gender == "Male" else 1  # Correcting gender encoding

# Prepare input data for prediction
input_data = np.array([[gender_value, age, duration, heart_rate, body_temp, bmi]])

prediction = model.predict(input_data)[0]

# Right Column - Show Parameters & Prediction
with col2:
    st.header("Selected Parameters")
    st.write(f"**Age:** {age} years")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Duration:** {duration} min")
    st.write(f"**Heart Rate:** {heart_rate} bpm")
    st.write(f"**Body Temperature:** {body_temp} °C")
    st.write(f"**Gender:** {gender}")
    
    # Display Prediction
    st.header("Calories Burned")
    st.success(f"{prediction:.2f} kcal")