import streamlit as st

st.title('My firrst streamlit app')

st.write('Welcome to my stramlit app')

st.button("Rese", type="primary")
if st.button("Say hello"):
  st.write("Hello there")
else:
  st.write("Goodbye")