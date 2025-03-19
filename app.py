import streamlit as st
import subprocess

st.title("🔑 PyPassword Generator")

# Προβολή του αρχικού κώδικα
with open("codeGenerator.py", "r") as f:
    code = f.read()
st.code(code, language="python")

# Επιλογή αριθμού χαρακτήρων
nr_letters = st.number_input("How many letters?", min_value=1, max_value=50, value=8)
nr_symbols = st.number_input("How many symbols?", min_value=0, max_value=10, value=2)
nr_numbers = st.number_input("How many numbers?", min_value=0, max_value=10, value=2)

# Κουμπί για εκτέλεση του script
if st.button("Generate Password"):
    try:
        # Εκτελεί το codeGenerator.py και του στέλνει τα inputs
        result = subprocess.run(
            ["python", "codeGenerator.py"],
            input=f"{nr_letters}\n{nr_symbols}\n{nr_numbers}\n",  # Στέλνει τα inputs ως text
            capture_output=True, text=True
        )

        # Αν υπάρχει output, εμφάνισέ το
        if result.stdout:
            st.success(f"Generated Password: **{result.stdout.strip()}**")
        if result.stderr:
            st.error(f"Error: {result.stderr}")

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
