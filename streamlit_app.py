import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import pandas as pd

# Function to generate PDF
def generate_pdf():
    buffer = BytesIO()

    # Create a PDF object
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 14)

    # Add borders to the PDF
    pdf.line(100, 800, 500, 800)  # Top border
    pdf.line(100, 800, 100, 0)    # Left border
    pdf.line(100, 0, 500, 0)      # Bottom border
    pdf.line(500, 0, 500, 800)    # Right border

    # Set up the PDF content with center alignment
    pdf.drawString(300, 780, "Anshuman Ojha's Resume")
    pdf.line(100, 775, 500, 775)  # Top border for header

    # ... (rest of the content)

    pdf.save()

    # Set up download button
    st.download_button(
        "Download PDF",
        buffer.getvalue(),
        file_name="Anshuman_Ojha_Resume.pdf",
        key="pdf-download",
    )

# Set page layout
st.set_page_config(
    page_title="Anshuman Ojha's Resume",
    page_icon=":clipboard:",
    layout="wide",
)

# Anshuman's Resume
st.title("Anshuman Ojha's Resume")

# Generate PDF button at the top-right corner
if st.button("Generate PDF", key="generate-pdf-btn", help="Generate and download PDF"):
    generate_pdf()

# Personal Information
st.header("Personal Information")

# Location Input
location = st.write("Location:", "Bangalore")

# Display other personal information
st.write("Name: Anshuman")
st.write("Designation: Finops Analyst")
st.write("Contact: 877743144")
st.write("Email: anshumanojha94@gmail.com")

# Work Experience
st.header("Work Experience")

# Finops(Revenue&Recon Analyst) - Freo
st.subheader("Finops(Revenue&Recon Analyst) - Freo")
st.write("Duration: Dec 2020 - Present")
st.write("Description:")
st.write("- MIS")
st.write("- Revenue automation")
st.write("- Partner onboarding")
st.write("- Made dashboards to check repayment")
st.write("- Day-to-day repayment recon")
st.write("- Solving payments disputes")
st.write("- Development and verification of monthly partner invoices")
st.write("- Handling Data required for partners and vendors")
st.write("- Data verification and analysis")
st.write("- Data correction")

# Associate(operations) - Freo
st.subheader("Associate(Operations) - Freo")
st.write("Duration: Dec 2019 - Nov 2020")
st.write("Description:")
# Add relevant details about the role

# Projects
st.header("Projects")
st.subheader("Data Science Certification Lead - May 2020")
st.write("Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")

# Certifications
st.header("Certifications")
st.write("Data Science Certification:")
st.write("Certified by IBM in association with Coursera")
st.write("Link: [IBM Data Science Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)")

# Additional Certifications
st.write("Python for Data Science and AI Development:")
st.write("Lead")
st.write("Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)")

st.write("Databases and SQL with Python:")
st.write("Lead")
st.write("Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)")

st.write("Data Visualization with Python:")
st.write("Lead")
st.write("Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)")

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
