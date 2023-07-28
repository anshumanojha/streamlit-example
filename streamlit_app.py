from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import streamlit as st
import plotly.graph_objects as go

# Create bar chart for tools data
tools_data = [10, 10, 8, 9, 7]
tools_labels = ['MYSQL', 'Python', 'Dashboard Development', 'Power Bi']
tools_fig = go.Figure(go.Bar(x=tools_labels, y=tools_data))
tools_fig.update_layout(title='Tools Known')

# Create line chart for technology data
technology_data = [9, 10, 10, 8, 7, 10]
technology_labels = ['Superset', 'SQL', 'Python', 'AWS', 'AI', 'ML']
technology_fig = go.Figure(go.Scatter(x=technology_labels, y=technology_data, mode='lines+markers'))
technology_fig.update_layout(title='Technology Known')

# Create pie chart for skills data
skills_data = [30, 60, 25, 33]
skills_labels = ['MYSQL', 'Python', 'Dashboard Development', 'Power Bi']
skills_fig = go.Figure(go.Pie(labels=skills_labels, values=skills_data, hole=0.3))
skills_fig.update_layout(title='Skills Proficiency out of 10')

# Define the layout of the dashboard
st.title('Dashboard')

st.header('Tools Known')
st.plotly_chart(tools_fig)

st.header('Technology Known')
st.plotly_chart(technology_fig)

st.header('Skills Proficiency')
st.plotly_chart(skills_fig)

st.header('Certifications')
st.markdown('[IBM-Data Analysis certificate](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)')
st.markdown('[IBM-Data Visualization with Python](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)')
st.markdown('[Databases and SQL for Data Science with Python](https://www.coursera.org/account/accomplishments/certificate/ST57AP42DMXS)')
st.markdown('[Machine Learning with Python](https://www.coursera.org/account/accomplishments/certificate/PWQGKGYMMMQU)')
st.markdown('[Python for Data Science, AI & Development](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)')
st.markdown('[IBM Data Science Specialization](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)')



