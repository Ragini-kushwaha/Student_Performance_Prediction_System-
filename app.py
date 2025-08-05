import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load trained model
model = joblib.load("student_performance_model.pkl")

st.set_page_config(page_title="Student Performance Predictor", layout="centered")
st.title("🎓 Student Performance Predictor")

st.markdown("Predict whether a student will perform **High**, **Medium**, or **Low** based on several inputs.")

# --- Input Fields ---
gender = st.selectbox("Gender", ["Male", "Female"])
study_hours = st.slider("Study Hours per Week", 0, 50, 10)
attendance = st.slider("Attendance Rate (%)", 0, 100, 75)
past_score = st.slider("Previous Exam Score", 0, 100, 60)
parent_edu = st.selectbox("Parental Education Level", ["None", "High School", "Graduate", "Post Graduate"])
internet = st.selectbox("Internet Access at Home", ["No", "Yes"])
activities = st.selectbox("Extracurricular Activities", ["No", "Yes"])

# --- Convert to numeric ---
gender = 1 if gender == "Male" else 0
internet = 1 if internet == "Yes" else 0
activities = 1 if activities == "Yes" else 0
parent_edu_dict = {"None": 0, "High School": 1, "Graduate": 2, "Post Graduate": 3}
parent_edu = parent_edu_dict[parent_edu]

# --- Prediction ---
if st.button("Predict Performance"):
    input_data = np.array([[gender, attendance, study_hours, past_score, activities, parent_edu, internet]])
    prediction = model.predict(input_data)[0]

    # Map numerical prediction to label
    performance_map = {0: "Low", 1: "Medium", 2: "High"}
    performance_label = performance_map.get(prediction, "Unknown")

    st.success(f"🎯 Predicted Student Performance Level: **{performance_label}**")
