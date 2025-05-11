import streamlit as st
from model import predict_churn

st.title("Customer Churn Prediction")

# Example input features (simplified)
tenure = st.slider("Tenure (months)", 0, 72, 24)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0, 1500.0)

if st.button("Predict"):
    input_data = [tenure, monthly_charges, total_charges]
    result = predict_churn(input_data)
    st.success(f"Churn Probability: {result:.2f}")
    st.write("Customer is likely to churn!" if result > 0.5 else "Customer is likely to stay.")
