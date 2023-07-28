from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import bs4
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

code = '''
import requests
import bs4
import pandas as pd

def get_smaller_urls(search_queries):
    smaller_urls = []

    for query in search_queries:
        url = "https://google.com/search?q=" + query
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, "html.parser")
        search_results = soup.find_all("a")
        result_links = []

        for result in search_results:
            link = result.get("href")
            if link.startswith("/url?q="):
                smaller_url = link[7:].split("&sa")[0]
                result_links.append(smaller_url)

        smaller_urls.extend(result_links)

    return smaller_urls

search_queries = ["biryani in bangalore"]
results = get_smaller_urls(search_queries)

df = pd.DataFrame({"Search Query": [query for query in search_queries for _ in range(len(results))],
                   "Smaller URL": results})

df
'''

st.code(code, language='python')

st.subheader('Output:')
st.write(pd.DataFrame({"Search Query": ["biryani in bangalore"], "Smaller URL": ["https://www.zomato.com/bangalore/biryani"]}))

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
