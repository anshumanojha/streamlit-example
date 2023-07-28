from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests  # Import the requests module

# Page 1: Anshuman's Portfolio

# Add Personal Information
st.title("Anshuman's Portfolio")
st.markdown(
    "<p style='font-size: 20px; color: #555555;'>Finops & Revenue Analyst | Experience: 3+ years</p>",
    unsafe_allow_html=True
)

# Add links to LinkedIn and GitHub profiles
st.markdown("[LinkedIn Profile](https://www.linkedin.com/in/anshuman-ojha-34093885/)")
st.markdown("[GitHub - Python Projects Automated Google Search](https://github.com/anshumanojha/pythonprojects/blob/master/Googlewebsearchauto.ipynb)")
st.markdown("[GitHub - Python Projects Automated Location Automate](https://github.com/anshumanojha/pythonprojects/blob/master/browser.py)")

# Create bar chart for tools data
tools_data = [10, 10, 8, 9, 7]
tools_labels = ['MYSQL', 'Python', 'Dashboard Development', 'Power Bi']
tools_chart = dict(zip(tools_labels, tools_data))

# Create line chart for technology data
technology_data = [9, 10, 10, 8, 7, 10]
technology_labels = ['Superset', 'SQL', 'Python', 'AWS', 'AI', 'ML']
technology_chart = dict(zip(technology_labels, technology_data))

# Create pie chart for skills data
skills_data = [30, 60, 60, 33, 50]
skills_labels = ['Data Scraping', 'Python Automation', 'Cohort Analysis', 'Trend Analysis', 'Repayment Automation']
skills_chart = dict(zip(skills_labels, skills_data))

# Tools Known section
st.header('Tools Known')
st.bar_chart(tools_chart, use_container_width=True)

# Technology Known section
st.header('Technology Known')
st.line_chart(technology_chart, use_container_width=True)

# Skills Proficiency section
st.header('Skills Proficiency')
st.bar_chart(skills_chart, use_container_width=True)

# Map section
st.header('Location - Bengaluru')
# Create a DataFrame with your location data
location_df = pd.DataFrame({'LATITUDE': [12.9716], 'LONGITUDE': [77.5946]})
st.map(location_df, zoom=10)

# Certifications section
st.header('Certifications')
st.markdown(
    "<ul style='font-size: 18px; color: #333333; list-style-type: square;'>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V' target='_blank'>IBM-Data Analysis certificate</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX' target='_blank'>IBM-Data Visualization with Python</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/ST57AP42DMXS' target='_blank'>Databases and SQL for Data Science with Python</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/PWQGKGYMMMQU' target='_blank'>Machine Learning with Python</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV' target='_blank'>Python for Data Science, AI & Development</a></li>"
    "<li><a href='https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9' target='_blank'>IBM Data Science Specialization</a></li>"
    "</ul>",
    unsafe_allow_html=True
)

# Page 2: Projects and Codes
st.title('Projects and Codes')

# Project 1: Data Scraping
st.subheader('Project 1: Data Scraping')
st.write("Description: A Python script to scrape data from a website.")

code_project1 = '''
def get_smaller_urls(search_query):
    url = "https://google.com/search?q=" + search_query
    request_result = requests.get(url)
    search_results = request_result.text
    start_index = search_results.find("https://www.zomato.com/")
    end_index = search_results.find("&", start_index)
    smaller_url = search_results[start_index:end_index]
    return smaller_url

search_query = "biryani in bangalore"
result = get_smaller_urls(search_query)

df = pd.DataFrame({"Search Query": [search_query],
                   "Smaller URL": [result]})
df
'''

if 'selected_project' not in st.session_state:
    st.session_state.selected_project = None

if st.button('Project 1: Data Scraping'):
    st.session_state.selected_project = 'Project 1: Data Scraping'

if st.session_state.selected_project == 'Project 1: Data Scraping':
    st.code(code_project1, language='python')
    st.subheader('Output:')
    exec(code_project1)

# Rest of the code for other projects (Project 2 to Project 5) remains unchanged.

# Show the content based on the selected project
if st.session_state.selected_project == 'Project 1: Data Scraping':
    st.subheader('Project 1: Data Scraping')
    st.write("Description: A Python script to scrape data from a website.")
