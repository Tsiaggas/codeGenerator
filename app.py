import random
import streamlit as st

def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'
    
    password_chars = (
        [random.choice(letters) for _ in range(nr_letters)] +
        [random.choice(symbols) for _ in range(nr_symbols)] +
        [random.choice(numbers) for _ in range(nr_numbers)]
    )
    
    random.shuffle(password_chars)
    return ''.join(password_chars)

st.title("PyPassword Generator")

nr_letters = st.number_input("How many letters would you like in your password?", min_value=0, value=8, step=1)
nr_symbols = st.number_input("How many symbols would you like?", min_value=0, value=2, step=1)
nr_numbers = st.number_input("How many numbers would you like?", min_value=0, value=2, step=1)

if st.button("Generate Password"):
    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    st.text_input("Your Generated Password:", password, type="default")
