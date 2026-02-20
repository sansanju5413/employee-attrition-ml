import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("attrition_model.pkl","rb"))
columns = pickle.load(open("columns.pkl","rb"))
st.title("Employee Attrition Predictor")

age = st.number_input("Age", 18, 60)
income = st.number_input("Monthly Income")
distance = st.number_input("Distance From Home")
years = st.number_input("Years at Company")

overtime = st.selectbox("Overtime", ["No","Yes"])
overtime = 1 if overtime == "Yes" else 0

if st.button("Predict"):
    data = np.array([[age, income, distance, years, overtime]])
    result = model.predict(data)

    if result[0] == 1:
        st.error("Employee Likely to Leave")
    else:
        st.success("Employee Likely to Stay")