from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import streamlit as st

# Add Personal Information
st.title("Anshuman's Portfolio")
st.markdown(
    "<p style='font-size: 20px; color: #555555;'>Finops & Revenue Analyst | Experience: 3+ years</p>",
    unsafe_allow_html=True
)

# Create bar chart for tools data
tools_data = [10, 10, 8, 9, 7]
tools_labels = ['MYSQL', 'Python', 'Dashboard Development', 'Power Bi']
tools_chart = dict(zip(tools_labels, tools_data))

# Create line chart for technology data
technology_data = [9, 10, 10, 8, 7, 10]
technology_labels = ['Superset', 'SQL', 'Python', 'AWS', 'AI', 'ML']
technology_chart = dict(zip(technology_labels, technology_data))

# Create pie chart for skills data
skills_data = [30, 60, 25, 33]
skills_labels = ['MYSQL', 'Python', 'Dashboard Development', 'Power Bi']
skills_chart = dict(zip(skills_labels, skills_data))

# Tools Known section
st.header('Tools Known')
st.bar_chart(tools_chart)

# Technology Known section
st.header('Technology Known')
st.line_chart(technology_chart)

# Skills Proficiency section
st.header('Skills Proficiency')
st.bar_chart(skills_chart)

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
