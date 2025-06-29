import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Insurance Premium Predictor", layout="centered")

st.title("🧮 Health Insurance Premium Predictor")

st.markdown("Enter the required information below to estimate your premium cost:")

# --- Row 1 ---
import streamlit as st

# --- Row 1 ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    age = st.number_input("Age", min_value=0, max_value=100, step=1)
with col2:
    gender = st.selectbox("Gender", ['Male', 'Female'])
with col3:
    region = st.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
with col4:
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])

# --- Row 2 ---
col5, col6, col7, col8 = st.columns(4)
with col5:
    bmi_category = st.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
with col6:
    smoking_status = st.selectbox("Smoking Status", ['No Smoking', 'Regular', 'Occasional'])
with col7:
    employment_status = st.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])
with col8:
    income_lakhs = st.number_input("Income (in Lakhs)", min_value=0.0)

# --- Row 3 ---
col9, col10, col11, col12 = st.columns(4)
with col9:
    medical_history = st.selectbox("Medical History", [
        'No Disease', 'Diabetes', 'High blood pressure', 'Thyroid', 'Heart disease',
        'Diabetes & High blood pressure', 'High blood pressure & Heart disease',
        'Diabetes & Thyroid', 'Diabetes & Heart disease'
    ])
with col10:
    insurance_plan = st.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])
with col11:
    genetical_risk = st.number_input("Genetical Risk (0–5)", min_value=0, max_value=5, step=1)
with col12:
    number_of_dependants = st.number_input("Number of Dependants", min_value=0, step=1)




# --- Predict Button ---
st.markdown("---")
if st.button("Predict"):
    input_dict = {
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }

    prediction = predict(input_dict)
    st.success(f"💰 Estimated Premium Cost: ₹{prediction}")
