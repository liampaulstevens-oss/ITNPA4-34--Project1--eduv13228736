import streamlit as st
import joblib
from preprocessing import clean_text

#loading the saved model then keeping in memory
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

#readable names for labels
label_names = {"ai": "artificial intelligence", "classical": "classical research"}

#page content
st.title("Researchly Research Abstract Classifier")
st.write("This app classifies research abstracts as either AI-related or classical research.")

abstract = st.text_area("Enter research abstract:", height=200)

if st.button("Classify Abstract"):
    if not abstract.strip():
        #warning if the text box is empty
        st.warning("Please enter an abstract to classify.")
    else:
        #cleaning the text the same as training
        cleaned = clean_text(abstract)
        prediction = model.predict([cleaned])[0]

        st.subheader("Prediction")
        st.success(f"The abstract is classified as: {label_names[prediction]}")