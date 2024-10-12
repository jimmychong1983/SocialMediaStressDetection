import streamlit as st
import pickle
from pathlib import Path
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json

# Load tokenizer from a saved JSON file
with open('notebooks/tokenizer.json', 'r') as f:
    tokenizer_data = json.load(f)
    
# Serialize the dictionary to a JSON string before passing it to tokenizer_from_json
tokenizer_json = json.dumps(tokenizer_data)  # Convert dict to JSON string
tokenizer = tokenizer_from_json(tokenizer_json)
    
# Get the path to the PKL files relative to the current script
linear_svc_path = Path(__file__).parents[1] / 'notebooks/Stress_Detection_LinearSVC_App.pkl'
lstm_path = Path(__file__).parents[1] / 'notebooks/Stress_Detection_LSTM_App.pkl'

# Load the classifiers from the PKL files
with open(linear_svc_path, 'rb') as f:
    linear_svc_classifier = pickle.load(f)

with open(lstm_path, 'rb') as f:
    lstm_classifier = pickle.load(f)

# Define a function to make predictions
def predict(sentence, model_type):
    if model_type == 'LinearSVC':
        classifier = linear_svc_classifier
        y_pred = classifier.predict([sentence])  
        return y_pred[0]

    elif model_type == 'LSTM':
        if type(sentence) == np.ndarray:
            sentence = sentence.astype(str)            
            sentence = sentence.lower()
        # Tokenize and pad the sentence
        sequence = tokenizer.texts_to_sequences([sentence])  
        padded_sequence = pad_sequences(sequence, maxlen=100)

        # Make prediction using the LSTM model
        prediction = lstm_classifier.predict(padded_sequence)

        # Convert prediction to a binary outcome (0 or 1)
        stress_level = (prediction > 0.5).astype(int)[0][0]
        return stress_level
    else:
        raise ValueError("Invalid model type")
    
# Create a dropdown menu to select the model type
model_type = st.selectbox("Select Model Type", ["LinearSVC", "LSTM"])

# Add a header title
st.title("Harnessing NLP to Detect Stress in Social Media: Early Intervention for Mental Wellbeing")

# Create a text input for the user to enter a sentence
sentence = st.text_input('Enter a sentence')

# Make a prediction when the user clicks a button
if st.button('Predict'):
    if sentence:  # Ensure the sentence is not empty
        prediction = predict(sentence, model_type)
        
        # Display the prediction result with appropriate messaging
        if prediction == 0:
            st.write("The text does not indicate high stress levels.")
        else:
            st.write("The text indicates high stress levels.")
    else:
        st.write("Please enter a sentence.")