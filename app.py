import streamlit as st
import pickle
import numpy as np

# Load the trained model
model_path = 'model.pkl'  # Ensure this path is correct
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Lung Cancer Prediction and Treatment Recommendation")

# Inputs from user
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=0)
smoking = st.selectbox("Smoking", [0, 1])
yellow_fingers = st.selectbox("Yellow Fingers", [0, 1])
anxiety = st.selectbox("Anxiety", [0, 1])
peer_pressure = st.selectbox("Peer Pressure", [0, 1])
chronic_disease = st.selectbox("Chronic Disease", [0, 1])
fatigue = st.selectbox("Fatigue", [0, 1])
allergy = st.selectbox("Allergy", [0, 1])
wheezing = st.selectbox("Wheezing", [0, 1])
alcohol_consuming = st.selectbox("Alcohol Consuming", [0, 1])
coughing = st.selectbox("Coughing", [0, 1])
shortness_of_breath = st.selectbox("Shortness of Breath", [0, 1])
swallowing_difficulty = st.selectbox("Swallowing Difficulty", [0, 1])
chest_pain = st.selectbox("Chest Pain", [0, 1])

# Map gender to numeric values
gender_mapping = {'Male': 0, 'Female': 1}
gender_num = gender_mapping.get(gender, -1)

# Prepare features array
features = np.array([[gender_num, age, smoking, yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcohol_consuming, coughing, shortness_of_breath, swallowing_difficulty, chest_pain]])

# Function to provide treatment recommendation
def treatment_recommendation(prediction, features):
    if prediction == 1:
        treatment = "Recommendation: Consult with an oncologist for further diagnosis and potential treatments such as chemotherapy, radiation therapy, or surgery."
        if smoking == 1:
            treatment += "\n- Smoking cessation is highly recommended."
        if chronic_disease == 1:
            treatment += "\n- Manage underlying chronic conditions to improve overall health."
        if chest_pain == 1 or shortness_of_breath == 1:
            treatment += "\n- Immediate medical attention for symptoms like chest pain and shortness of breath is advised."
    else:
        treatment = "No lung cancer detected. However, maintaining a healthy lifestyle, avoiding smoking, and regular check-ups are advised."

    return treatment

# Predict button
if st.button('Predict'):
    if gender_num == -1:
        st.error("Invalid gender input.")
    else:
        prediction = model.predict(features)
        result = "YES" if prediction[0] == 1 else "NO"
        st.write(f"Prediction: Lung Cancer {'Detected' if result == 'YES' else 'Not Detected'}")
        
        # Get treatment recommendation based on prediction
        recommendation = treatment_recommendation(prediction[0], features)
        st.write(recommendation)
