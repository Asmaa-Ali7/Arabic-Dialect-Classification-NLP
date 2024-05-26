import streamlit as st
import joblib
import time

# st.title("Arabic Dialects Prediction")

html_temp = """
    <div style="background-color:#85002d;padding:10px;border-radius: 15px;">
    <h2 style="color:white;text-align:center;">Arabic Dialects Prediction</h2>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

# Load Model
pipeline = joblib.load('text_classification_pipeline.pkl')
label_encoder = joblib.load('label_encoder.pkl')

sentence = st.text_input("Enter your sentence: ")

submit = st.button("Predict")

# Dictionary mapping labels to dialect names and flags
dialect_names = {
    "SD": "Sudanese - سودانية",
    "LB": "Lebanese - لبنانية",
    "EG": "Egyptian - مصرية",
    "MA": "Moroccian - مغربية",
    "LY": "Libyan - ليبية"
}

if submit:
    start = time.time()
    prediction = pipeline.predict([sentence])
    prediction_label = label_encoder.inverse_transform(prediction)
    end = time.time()
    st.write("Prediction Time Taken: ", round(end - start), " Seconds")
    st.write("Predicted Dialect is: ", dialect_names[prediction_label[0]])