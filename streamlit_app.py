import streamlit as st
import pandas as pd
import random

# Anshuman's Resume
st.title("Anshuman's Resume")

# Personal Information
st.header("Personal Information")

# Location Input
location = st.write("Location:", "Bangalore")

# Display other personal information
st.write("Name: Anshuman")
st.write("Email: anshumanojha94@gmail.com")

# Work Experience
st.header("Work Experience")
st.subheader("Operations Analyst - Freo")
st.write("Duration: 3+ years")
st.write("Description: Worked as an Operations Analyst at Freo, focusing on various operational tasks.\n Made dashboard for various operational data.\n Dived into revenue data month on month")

# Skills
st.header("Skills")
st.write("- Python")
st.write("- Excel")
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
    "Write a query to select two unique items.",
    "Write a query to delete records older than a specific date.",
    "Write a query to find the average value of a numeric column.",
    "Write a query to join two tables based on a common column.",
    "Write a query to count the number of records in a table.",
    "Write a query to find the maximum value in a column.",
    "Write a query to list all tables in the database.",
    "Write a query to select records with a certain condition.",
    "Write a query to sort records in descending order.",
    "Write a query to filter records with a specific pattern.",
    "Write a query to group records based on a column.",
    "Write a query to find the minimum value in a column.",
    "Write a query to calculate the total sum of a numeric column.",
    "Write a query to perform an inner join between three tables.",
    "Write a query to retrieve the top N records from a table.",
    "Write a query to update multiple columns in a single query.",
    "Write a query to calculate the average value for each group.",
    "Write a query to find records where a column is not null.",
    "Write a query to count distinct values in a column.",
    "Write a query to select records with a date within a specific range.",
    "Write a query to concatenate two columns into a single column.",
    "Write a query to perform a left join between two tables.",
    "Write a query to select random records from a table.",
    "Write a query to find the second-highest value in a column.",
    "Write a query to calculate the median value of a numeric column.",
    "Write a query to update records based on a subquery.",
    "Write a query to select records with a case-insensitive search.",
    "Write a query to find the average value for each group.",
]
prompt = st.selectbox("Select a prompt:", prompt_options)

suggested_queries = {
    "Write a query to update the database.": "UPDATE table_name SET column1 = value1 WHERE condition;",
    "Write a query to select two unique items.": "SELECT DISTINCT column1, column2 FROM table_name;",
    "Write a query to delete records older than a specific date.": "DELETE FROM table_name WHERE date_column < '2022-01-01';",
    "Write a query to find the average value of a numeric column.": "SELECT AVG(numeric_column) FROM table_name;",
    "Write a query to join two tables based on a common column.": "SELECT * FROM table1 JOIN table2 ON table1.common_column = table2.common_column;",
    "Write a query to count the number of records in a table.": "SELECT COUNT(*) FROM table_name;",
    "Write a query to find the maximum value in a column.": "SELECT MAX(column_name) FROM table_name;",
    "Write a query to list all tables in the database.": "SHOW TABLES;",
    "Write a query to select records with a certain condition.": "SELECT * FROM table_name WHERE condition;",
    "Write a query to sort records in descending order.": "SELECT * FROM table_name ORDER BY column_name DESC;",
    "Write a query to filter records with a specific pattern.": "SELECT * FROM table_name WHERE column_name LIKE '%pattern%';",
    "Write a query to group records based on a column.": "SELECT column_name, COUNT(*) FROM table_name GROUP BY column_name;",
    "Write a query to find the minimum value in a column.": "SELECT MIN(column_name) FROM table_name;",
    "Write a query to calculate the total sum of a numeric column.": "SELECT SUM(numeric_column) FROM table_name;",
    "Write a query to perform an inner join between three tables.": "SELECT * FROM table1 JOIN table2 ON table1.common_column = table2.common_column JOIN table3 ON table2.common_column = table3.common_column;",
    "Write a query to retrieve the top N records from a table.": "SELECT * FROM table_name LIMIT N;",
    "Write a query to update multiple columns in a single query.": "UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;",
    "Write a query to calculate the average value for each group.": "SELECT column_name, AVG(numeric_column) FROM table_name GROUP BY column_name;",
    "Write a query to find records where a column is not null.": "SELECT * FROM table_name WHERE column_name IS NOT NULL;",
    "Write a query to count distinct values in a column.": "SELECT COUNT(DISTINCT column_name) FROM table_name;",
    "Write a query to select records with a date within a specific range.": "SELECT * FROM table_name WHERE date_column BETWEEN 'start_date' AND 'end_date';",
    "Write a query to concatenate two columns into a single column.": "SELECT CONCAT(column1, ' ', column2) AS concatenated_column FROM table_name;",
    "Write a query to perform a left join between two tables.": "SELECT * FROM table1 LEFT JOIN table2 ON table1.common_column = table2.common_column;",
    "Write a query to select random records from a table.": "SELECT * FROM table_name ORDER BY RAND() LIMIT N;",
    "Write a query to find the second-highest value in a column.": "SELECT MAX(column_name) FROM table_name WHERE column_name < (SELECT MAX(column_name) FROM table_name);",
    "Write a query to calculate the median value of a numeric column.": "SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY numeric_column) FROM table_name;",
    "Write a query to update records based on a subquery.": "UPDATE table_name SET column1 = (SELECT column2 FROM another_table WHERE condition) WHERE condition;",
    "Write a query to select records with a case-insensitive search.": "SELECT * FROM table_name WHERE LOWER(column_name) = LOWER('search_value');",
    "Write a query to find the average value for each group.": "SELECT column_name, AVG(numeric_column) FROM table_name GROUP BY column_name;"
}

user_response = st.text_area("Write your SQL query here:")
if st.button("Check Query"):
    if user_response.strip().lower() in suggested_queries[prompt].lower():
        st.success("Correct! Well done! You can now view the portfolio.")
    else:
        st.error("Oops! That's not the correct query. Try again!")
        st.info(f"The correct answer is:\n{suggested_queries[prompt]}")
