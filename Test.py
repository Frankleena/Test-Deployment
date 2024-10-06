import streamlit as st

st.title('Model Deployment: Logistic Regression')

text = st.text_input("Enter the text")
if st.button("Predict"):
    st.write("Thanks for sharing with us, your input was: ", text)
