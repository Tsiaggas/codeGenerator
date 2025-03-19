import streamlit as st
import subprocess

st.title("🔑 PyPassword Generator")

# Προβολή του αρχικού κώδικα
with open("codeGenerator.py", "r") as f:
    code = f.read()
st.code(code, language="python")

# Κουμπί για εκτέλεση του αρχικού script
if st.button("Run Script"):
    with st.form(key="password_form"):
        nr_letters = st.number_input("How many letters?", min_value=1, max_value=50, value=8)
        nr_symbols = st.number_input("How many symbols?", min_value=0, max_value=10, value=2)
        nr_numbers = st.number_input("How many numbers?", min_value=0, max_value=10, value=2)
        submit_button = st.form_submit_button(label="Generate Password")

    if submit_button:
        try:
            result = subprocess.run(
                ["python", "codeGenerator.py"],
                input=f"{nr_letters}\n{nr_symbols}\n{nr_numbers}\n",  # Στέλνει τα inputs στο script
                capture_output=True, text=True, check=True
            )
            st.success(f"Generated Password: **{result.stdout.strip()}**")
        except subprocess.CalledProcessError as e:
            st.error(f"Error running script: {e.stderr}")
