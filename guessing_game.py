import streamlit as st
import random
import math

# Portfolio Section
def show_portfolio():
    st.title("My Portfolio")
    st.write("This is a sample portfolio section.")
    

# Guessing Game Section
def guessing_game():
    st.title("Guessing Game")
    
    # Choose Mode
    mode = st.selectbox("Choose the mode:", ["User Guessing", "Machine Guessing"])
    
    # Display rules
    if mode == "User Guessing":
        st.write("Rules: Try to guess the number the machine has picked.")
        user_guessing_mode()
    elif mode == "Machine Guessing":
        st.write("Rules: Think of a number, and the machine will try to guess it.")
        machine_guessing_mode()

# User Guessing Mode
def user_guessing_mode():
    if 'target_number' not in st.session_state:
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    submit = st.button("Submit Guess")
    
    if submit:
        st.session_state.attempts += 1
        if guess < st.session_state.target_number:
            st.write("Try a higher number!")
        elif guess > st.session_state.target_number:
            st.write("Try a lower number!")
        else:
            st.write(f"Congratulations! You guessed it in {st.session_state.attempts} attempts.")
            st.session_state.target_number = random.randint(1, 100)  # Reset for a new game
            st.session_state.attempts = 0

# Machine Guessing Mode
def machine_guessing_mode():
    if 'low' not in st.session_state:
        st.session_state.low, st.session_state.high = 1, 100
        st.session_state.attempts = 0
    
    st.write(f"Think of a number between {st.session_state.low} and {st.session_state.high}.")
    guess = (st.session_state.low + st.session_state.high) // 2
    st.write(f"Machine's guess: {guess}")
    
    response = st.radio("Is the guess too low, too high, or correct?", ["Too low", "Too high", "Correct"])
    if response == "Too low":
        st.session_state.low = guess + 1
    elif response == "Too high":
        st.session_state.high = guess - 1
    elif response == "Correct":
        st.write(f"Machine guessed it in {st.session_state.attempts} attempts!")
        st.session_state.low, st.session_state.high = 1, 100  # Reset for a new game
        st.session_state.attempts = 0
        return
    
    st.session_state.attempts += 1

# Main app
def main():
    st.sidebar.title("Guessing Game & Portfolio")
    st.sidebar.write("Choose a section to view:")
    section = st.sidebar.selectbox("Section", ["Portfolio", "Guessing Game"])
    
    if section == "Portfolio":
        show_portfolio()
    elif section == "Guessing Game":
        guessing_game()

    main()