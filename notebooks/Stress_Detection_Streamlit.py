import streamlit as st
import pickle
from pathlib import Path

# Get the path to the PKL file relative to the current script
pkl_path = Path(__file__).parents[1] / 'notebooks/Stress_Detection_App.pkl'

# Load the classifier from the PKL file
with open(pkl_path, 'rb') as f:
    stress_classifier = pickle.load(f)

# Define a function to make predictions
def predict(sentences):
    y_pred = stress_classifier.predict(sentences)
    return y_pred
    
# Add a header title
st.title("Harnessing NLP to Detect Stress in Social Media: Early Intervention for Mental Wellbeing")

# Create a text input for the user to enter a sentence
sentence = st.text_input('Enter a sentence')

# Add a clear button beside the predict button
if st.button('Clear'):
    sentence = ''

# Make a prediction when the user clicks a button
if st.button('Predict'):
    prediction = predict([sentence])[0]

    # Display the prediction result with appropriate messaging
    if prediction == 0:
        st.write("The text does not indicate high stress levels.")
    else:
        st.write("The text indicates high stress levels.")

# Set the focus to the text input by default
st.markdown("<script>document.querySelector('input[type=text]').focus();</script>", unsafe_allow_html=True)