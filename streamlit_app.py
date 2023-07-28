from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

# Import the required libraries
import streamlit as st

# Page 1: Anshuman's Portfolio

# Add Personal Information
st.title("Anshuman's Portfolio")
st.markdown(
    "<p style='font-size: 20px; color: #555555;'>Finops & Revenue Analyst | Experience: 3+ years</p>",
    unsafe_allow_html=True
)

# Add links to LinkedIn and GitHub profiles
st.markdown("LinkedIn Profile: [Anshuman Ojha](https://www.linkedin.com/in/anshuman-ojha-34093885/)", unsafe_allow_html=True)
st.markdown("GitHub - Python Projects Automated Google Search: [Automated Google Search](https://github.com/anshumanojha/pythonprojects/blob/master/Googlewebsearchauto.ipynb)", unsafe_allow_html=True)
st.markdown("GitHub - Python Projects Automated Location Automate: [Automated Location Automate](https://github.com/anshumanojha/pythonprojects/blob/master/browser.py)", unsafe_allow_html=True)

# Create bar chart for tools data
# ... (your existing code for charts)

# Map section
# ... (your existing code for the map)

# Certifications section
# ... (your existing code for certifications)

# Page 2: Projects and Codes

st.title('Projects and Codes')
st.subheader('Project 1: Data Scraping')
st.write("Description: A Python script to scrape data from a website.")
st.code('''
# Your code for Data Scraping project goes here
''', language='python')

st.subheader('Project 2: Python Automation')
st.write("Description: A Python script for automating a repetitive task.")
st.code('''
# Your code for Python Automation project goes here
''', language='python')

st.subheader('Project 3: Cohort Analysis')
st.write("Description: Python code for performing cohort analysis on customer data.")
st.code('''
# Your code for Cohort Analysis project goes here
''', language='python')

st.subheader('Project 4: Trend Analysis')
st.write("Description: Python code for analyzing trends in financial data.")
st.code('''
# Your code for Trend Analysis project goes here
''', language='python')

st.subheader('Project 5: Repayment Automation')
st.write("Description: Python script for automating repayment calculations.")
st.code('''
# Your code for Repayment Automation project goes here
''', language='python')





