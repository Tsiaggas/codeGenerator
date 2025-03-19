import streamlit as st

with open("codeGenerator.py", "r") as f:
    code = f.read()

st.title("My Python Script")
st.code(code, language="python")