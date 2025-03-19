import streamlit as st

# Διάβασε το script
with open("codeGenerator.py", "r") as f:
    code = f.read()

# Προβολή του κώδικα
st.code(code, language="python")

# Κουμπί για να τρέξει το script
if st.button("Run Script"):
    exec(code)  # Εκτελεί τον κώδικα του αρχείου