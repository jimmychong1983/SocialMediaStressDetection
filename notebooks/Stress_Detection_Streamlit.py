import streamlit as st
import pickle

# Load the classifier from the pickle file
with open('Stress_Detection_App.pkl', 'rb') as f:
    stress_classifier = pickle.load(f)

# Define a function to make predictions
def predict(sentences):
    y_pred = stress_classifier.predict(sentences)
    return y_pred

# Create a text input for the user to enter a sentence
sentence = st.text_input('Enter a sentence')

# Make a prediction when the user clicks a button
if st.button('Predict'):
    prediction = predict([sentence])[0]

    # Display the prediction result with appropriate messaging
    if prediction == 0:
        st.write("The text does not indicate high stress levels.")
    else:
        st.write("The text indicates high stress levels.")
