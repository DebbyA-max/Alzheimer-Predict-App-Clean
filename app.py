
import streamlit as st
import numpy as np
import joblib

model=joblib.load("alzheimers_model.pkl")
st.title("Alzheimer's Disease Prediction App")
st.write("Enter the patient data below to predict Alzheimer's Diagnosis.")

FunctionalAssessment=st.number_input("Functional Assessment Score", min_value=0, key="fun_acc_input") 
ADL=st.number_input("Activities of Daily Living score", min_value=0, key="ADL_input")
MMSE=st.number_input("Mini-Mental State Examination score", min_value=0.0, key="MMSE_input")
MemoryComplaints=st.radio(" Presence of memory complaints", ["Yes", "No"], key="mce_input")
MemoryComplaints_encoded= 1 if MemoryComplaints=="Yes" else 0
BehavioralProblems=st.radio(" Presence of behavioral problems", ["Yes", "No"], key="bpe_input")
BehavioralProblems_encoded= 1 if BehavioralProblems=="Yes" else 0 

input_data=np.array([[FunctionalAssessment, ADL, MMSE, MemoryComplaints_encoded, BehavioralProblems_encoded]])

if st.button("Predict"):
    prediction=model.predict(input_data)[0]
    st.success(f"Prediction:{prediction}")
