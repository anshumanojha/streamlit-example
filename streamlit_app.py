import streamlit as st
import pandas as pd

# Anshuman's Resume
st.title("Anshuman's Resume")

# Personal Information
st.header("Personal Information")

# Location Input
location = st.text_input("Location:", "Bangalore")

# Display other personal information
st.write("Name: Anshuman")
st.write(f"Location: {location}")
st.write("Email: your.email@example.com")

# Work Experience
st.header("Work Experience")
st.subheader("Operations Analyst - Freo")
st.write("Duration: 3+ years")
st.write("Description: Worked as an Operations Analyst at Freo, focusing on various operational tasks.")

# Skills
st.header("Skills")
st.write("- Python")
st.write("- Web Development")
st.write("- Database Management")
st.write("- Streamlit")
st.write("- SQL")

# Show map for Bangalore
st.header("Location Map - Bangalore")
location_data = pd.DataFrame({
    "latitude": [12.9716],  # Bangalore latitude
    "longitude": [77.5946]  # Bangalore longitude
})
st.map(location_data)

# SQL Query Suggestor
st.header('SQL Query Suggestor')
prompt_options = [
    "Write a query to update the database.",
    "Write a query to select two unique items."
]
prompt = st.selectbox("Select a prompt:", prompt_options)

suggested_query = ""
if prompt == "Write a query to update the database.":
    suggested_query = "UPDATE table_name SET column1 = value1 WHERE condition;"
elif prompt == "Write a query to select two unique items.":
    suggested_query = "SELECT DISTINCT column1, column2 FROM table_name;"

user_response = st.text_area("Write your SQL query here:")
if st.button("Check Query"):
    if user_response.strip().lower() == suggested_query.lower():
        st.success("Correct! Well done! You can now view the portfolio.")
    else:
        st.error("Oops! That's not the correct query. Try again!")
