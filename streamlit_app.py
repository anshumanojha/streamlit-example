import streamlit as st

# Anshuman's Resume
st.title("Anshuman's Resume")

# Personal Information
st.header("Personal Information")

# Location Input
location = st.text_input("Location:", "Your Location")

# Display other personal information
st.write("Name: Anshuman")
st.write(f"Location: {location}")
st.write("Email: your.email@example.com")

# Work Experience
st.header("Work Experience")
st.subheader("Software Developer - XYZ Company")
st.write("Duration: January 2020 - Present")
st.write("Description: Worked on various projects, including web development and database management.")

# Education
st.header("Education")
st.write("Bachelor of Science in Computer Science - ABC University")
st.write("Graduation Year: 2019")

# Skills
st.header("Skills")
st.write("- Python")
st.write("- Web Development")
st.write("- Database Management")
st.write("- Streamlit")
st.write("- SQL")

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
