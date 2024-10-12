import streamlit as st
import pickle
from pathlib import Path

# Get the path to the PKL files relative to the current script
linear_svc_path = Path(__file__).parents[1] / 'notebooks/Stress_Detection_LinearSVC_App.pkl'
lstm_path = Path(__file__).parents[1] / 'notebooks/Stress_Detection_LSTM_App.pkl'

# Load the classifiers from the PKL files
with open(linear_svc_path, 'rb') as f:
    linear_svc_classifier = pickle.load(f)
with open(lstm_path, 'rb') as f:
    lstm_classifier = pickle.load(f)

# Define a function to make predictions based on the selected model
def predict(sentences, model_type):
    if model_type == 'LinearSVC':
        classifier = linear_svc_classifier
    elif model_type == 'LSTM':
        classifier = lstm_classifier
    else:
        raise ValueError("Invalid model type")

    y_pred = classifier.predict(sentences)
    return y_pred

# Add a header title
st.title("Harnessing NLP to Detect Stress in Social Media: Early Intervention for Mental Wellbeing")

# Create a dropdown menu to select the model type
model_type = st.selectbox("Select Model Type", ["LinearSVC", "LSTM"])

# Create a text input for the user to enter a sentence
sentence = st.text_input('Enter a sentence')

# Make a prediction when the user clicks a button
if st.button('Predict'):
    prediction = predict([sentence], model_type)[0]

    # Display the prediction result with appropriate messaging
    if prediction == 0:
        st.write("The text does not indicate high stress levels.")
    else:
        st.write("The text indicates high stress levels.")