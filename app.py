
import streamlit as st
import numpy as np
import joblib

model=joblib.load("alzheimers_model.pkl")
st.title("Alzheimer's Disease Prediction App")
st.write("Enter the patient data below to predict Alzheimer's Diagnosis.")

FunctionalAssessment=st.number_input("FunctionalAssessment", min_value=0) 
ADL=st.number_input("Activities of Daily Living score", min_value=0)
MMSE=st.number_input("Mini-Mental State Examination score", min_value=0.0)
MemoryComplaints=st.radio(" Presence of memory complaints", ["Yes", "No"])
MemoryComplaints_encoded= 1 if MemoryComplaints=="Yes" else 0
BehavioralProblems=st.radio(" Presence of behavioral problems", ["Yes", "No"])
BehavioralProblems_encoded= 1 if BehavioralProblems=="Yes" else 0 

input_data=np.array([[FunctionalAssessment, ADL, MMSE, MemoryComplaints_encoded, BehavioralProblems_encoded]])

if st.button("Predict"):
    prediction=model.predict(input_data)[0]
    st.success(f"Prediction:{prediction}")


import streamlit as st
import numpy as np
import joblib

model=joblib.load("alzheimers_model.pkl")
st.title("Alzheimer's Disease Prediction App")
st.write("Enter the patient data below to predict Alzheimer's Diagnosis.")

FunctionalAssessment=st.number_input("FunctionalAssessment", min_value=0) 
ADL=st.number_input("Activities of Daily Living score", min_value=0)
MMSE=st.number_input("Mini-Mental State Examination score", min_value=0.0)
MemoryComplaints=st.radio(" Presence of memory complaints", ["Yes", "No"])
MemoryComplaints_encoded= 1 if MemoryComplaints=="Yes" else 0
BehavioralProblems=st.radio(" Presence of behavioral problems", ["Yes", "No"])
BehavioralProblems_encoded= 1 if BehavioralProblems=="Yes" else 0 

input_data=np.array([[FunctionalAssessment, ADL, MMSE, MemoryComplaints_encoded, BehavioralProblems_encoded]])

if st.button("Predict"):
    prediction=model.predict(input_data)[0]
    st.success(f"Prediction:{prediction}")
dd32992ff335284256ed2752f58921b4a80837a0
