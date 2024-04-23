import streamlit as st
import pandas as pd

tab1, tab2 = st.tabs(["Data Scientist Technical Review", "Data Analyst Technical Review"]) 

with tab1:
    # Title of the application
    st.title("Data Scientist Technical Review")

    # Create empty dictionary to store the inputs
    data = {}

    # Loop to generate text input fields for questions
    for i in range(1, 13):
        question_key = f"Python Basic Q-{i}"
        # Streamlit input field, defaulting to 0
        data[question_key] = st.number_input(question_key, value=0, format="%d")

    # Button to create DataFrame
    if st.button("Total Score"):
        # Create DataFrame from the dictionary
        df = pd.DataFrame([data])
        df['Total'] = df.sum(axis=1)
        df['Average'] = df['Total'] / 66
        df['Average'] = df['Average'].apply(lambda x: "{:.2%}".format(x))
        df['Outcome'] = df['Average'].apply(lambda x: 'Pass' if float(x.strip('%')) > 60 else 'Fail')
        # Display the DataFrame
        st.write(df)


with tab2:
    # Title of the application
    st.title("Data Analyst Technical Review")

