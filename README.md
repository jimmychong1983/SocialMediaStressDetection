# SocialMediaStressDetection

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project explores the use of machine learning to detect stress in social media text data. It leverages Streamlit to create a user-friendly web application for stress detection analysis.

Project Link:
```python
https://socialmediastressdetection.streamlit.app/
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Installation:

1) Python and pip:
 - Download and install Python from the official website: 
```python
https://www.python.org/downloads/
```
 - Verify pip installation using  
```python
python -m ensurepip --upgrade
```	
 
2) Dependencies:

 - Open a terminal and navigate to your project directory (example).
```python
cd C:\Users\jimmy\OneDrive\Desktop\My Project\SocialMediaStressDetection\notebooks
```	
 
 - Install the required libraries:
```python
pip install streamlit scikit-learn spacy
```	

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Setting Up and Running the Social Media Stress Detection App

1) Running the Streamlit App
```python
streamlit run "Stress_Detection_Streamlit.py"
```
 
2)Generating Requirements
```python
pip freeze > requirements.txt
```

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Setting Up the Python Environment for Natural Language Processing (NLP)

1) Download and Install Python (Optional):
```python
https://www.python.org/downloads/
```

2) Adding Python to System Path

 - Click on the "Start" button.
 - Search for "Control Panel" and open it.
 - Navigate to "System and Security" -> "System".
 - Click on "Advanced system settings".
 
 3) Edit Environment Variables:

 - In the "Environment Variables" window, look for the "System variables" section.
 - Find the "Path" variable and click "Edit".
 - Add the directory where Python is installed to the end of the existing path. eg: C:\Users\jimmy\AppData\Local\Programs\Python\Python312
 - Click "OK" to save the changes.
 
 4) Open Command Prompt:
```python
cd C:\Users\jimmy\AppData\Local\Programs\Python\Python312 
```

```python 
cd Scripts	 
```

```python
pip install spacy 
```

```python
phyton -m spacy download en_core_web_lg
```