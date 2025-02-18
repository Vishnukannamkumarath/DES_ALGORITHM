import streamlit as st
from des_api import des_output

st.title("DES Encryption/Decryption")


user_input = st.text_input("Enter Message for Encryption or Decryption")


choice = ["hex", "string"]
inp_type = st.selectbox("Select Type of Input", choice)


key = st.text_input("Enter key")


key_type = st.selectbox("Select Type of Key", choice)


operations = ["encrypt", "decrypt"]
opr = st.selectbox("Enter Type of Operation", operations)


if st.button('Submit'):
    if user_input and key:
        result = des_output(user_input, inp_type, key, key_type, opr)
        st.write("Result:", result)
    else:
        st.warning("Please enter both a message and a key before submitting.")
