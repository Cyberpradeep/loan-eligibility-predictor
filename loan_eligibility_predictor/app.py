import streamlit as st
import numpy as np
import joblib
model = joblib.load("loan_model.pkl")
st.set_page_config(page_title="Loan Eligibility Predictor 💰", page_icon="📋")
st.title(" Loan Eligibility Predictor")
st.write("Fill the form below to check if you're eligible for a loan.")
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Monthly Income (₹)", min_value=0)
loan_amount = st.number_input("Loan Amount (in ₹1000)", min_value=0)
property_area = st.selectbox("Property Area", ["Rural", "Semiurban", "Urban"])
gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0
property_area = {"Rural": 0, "Semiurban": 1, "Urban": 2}[property_area]
if st.button("Check Eligibility"):
    input_data = np.array([[gender, married, education, self_employed, applicant_income, loan_amount, property_area]])
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.success("You are eligible for a loan!")
    else:
        st.error("Sorry, you are not eligible for a loan.")
