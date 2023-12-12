import streamlit as st
import requests
import pandas as pd
import random

# Odd One Out Game Logic
class OddOneOutGame:
    def __init__(self):
        self.sets = [
            ['Apple', 'Banana', 'Orange', 'Carrot'],
            ['Dog', 'Cat', 'Fish', 'Bird'],
            ['Red', 'Blue', 'Green', 'Chair']
        ]
        self.correct_answers = ['Carrot', 'Fish', 'Chair']
        self.current_set = None
        self.answer = None

    def new_round(self):
        self.current_set = random.choice(self.sets)
        self.answer = None

# SQL Query Suggestor Function
def suggest_sql_query(prompt):
    if prompt == "Write a query to update the database.":
        return "UPDATE table_name SET column1 = value1 WHERE condition;"
    elif prompt == "Write a query to select two unique items.":
        return "SELECT DISTINCT column1, column2 FROM table_name;"

# Streamlit App
def main():
    st.title("Anshuman's Portfolio with Odd One Out Game")

    # SQL Query Suggestor
    st.header('SQL Query Suggestor')
    prompt_options = [
        "Write a query to update the database.",
        "Write a query to select two unique items."
    ]
    prompt = st.selectbox("Select a prompt:", prompt_options)

    suggested_query = suggest_sql_query(prompt)

    user_response = st.text_area("Write your SQL query here:")
    if st.button("Check Query"):
        if user_response.strip().lower() == suggested_query.lower():
            st.success("Correct! Well done! You can now view the portfolio.")
        else:
            st.error("Oops! That's not the correct query. Try again!")

    # Odd One Out Game
    game = OddOneOutGame()

    # Button to start a new round
    if st.button("Start New Round - Odd One Out Game"):
        game.new_round()

    # Display the current set for Odd One Out Game
    if game.current_set:
        st.write("Which one is the odd one out?")
        selected_option = st.radio("Select one:", game.current_set)

        # Check user's answer for Odd One Out Game
        game.answer = selected_option

        if game.answer in game.correct_answers:
            st.success("Correct! Well done! You can now view the portfolio.")
        else:
            st.error("Oops! That's not the odd one out. Try again!")

    # Rest of your existing code for the portfolio display
    st.title("Anshuman's Portfolio")
    # ... (rest of the code remains the same)

if __name__ == "__main__":
    main()
