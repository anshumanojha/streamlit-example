from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


import streamlit as st

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

# Define the layout of the dashboard
st.title('Dashboard')

st.header('Tools Known')
st.bar_chart(tools_chart)

st.header('Technology Known')
st.line_chart(technology_chart)

st.header('Skills Proficiency')
st.pyplot(skills_chart)

st.header('Certifications')
st.markdown('[IBM-Data Analysis certificate](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)')
st.markdown('[IBM-Data Visualization with Python](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)')
st.markdown('[Databases and SQL for Data Science with Python](https://www.coursera.org/account/accomplishments/certificate/ST57AP42DMXS)')
st.markdown('[Machine Learning with Python](https://www.coursera.org/account/accomplishments/certificate/PWQGKGYMMMQU)')
st.markdown('[Python for Data Science, AI & Development](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)')
st.markdown('[IBM Data Science Specialization](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)')




