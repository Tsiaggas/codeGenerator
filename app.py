import streamlit as st
import subprocess

st.title("Run My Python Script")

# Προβολή του κώδικα
with open("codeGenerator.py", "r") as f:
    code = f.read()

st.code(code, language="python")

# Κουμπί για εκτέλεση του script
if st.button("Run"):
    result = subprocess.run(["python", "codeGenerator.py"], capture_output=True, text=True)
    st.write("### Output:")
    st.code(result.stdout)
