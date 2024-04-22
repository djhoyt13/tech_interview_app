import streamlit as st
import pandas as pd

# Title of the application
st.title("Input Integers for Python Basics Questions")

# Create empty dictionary to store the inputs
data = {}

# Loop to generate text input fields for questions
for i in range(1, 13):
    question_key = f"Python Basic Q-{i}"
    # Streamlit input field, defaulting to 0
    data[question_key] = st.number_input(question_key, value=0, format="%d")

# Button to create DataFrame
if st.button("Create DataFrame"):
    # Create DataFrame from the dictionary
    df = pd.DataFrame([data])
    # Display the DataFrame
    st.write(df)
