from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
tools_data = [10, 10, 8, 9, 7]
tools_labels = ['MYSQL', 'Python', 'Dashboard Development', 'Power Bi']

# Tools Known section (Bar Chart)
st.header('Tools Known')
fig_tools, ax_tools = plt.subplots()
ax_tools.bar(tools_labels, tools_data, color='#00aaff')
ax_tools.set_title('Tools Known')
ax_tools.set_xlabel('Tools')
ax_tools.set_ylabel('Knowledge Level')
st.pyplot(fig_tools)

# Create radar chart for technology data
technology_data = [9, 10, 10, 8, 7, 10]
technology_labels = ['Superset', 'SQL', 'Python', 'AWS', 'AI', 'ML']

# Create a DataFrame for the radar chart
technology_df = pd.DataFrame({'Technology': technology_labels, 'Knowledge Level': technology_data})

# Technology Known section (Radar Chart)
st.header('Technology Known')
st.write("Knowledge Level for each Technology:")
st.write(technology_df)

# Create a radar chart
fig_radar, ax_radar = plt.subplots(subplot_kw={'polar': True})
ax_radar.plot(technology_labels + [technology_labels[0]], technology_data + [technology_data[0]], marker='o', color='#00aaff')
ax_radar.fill(technology_labels + [technology_labels[0]], technology_data + [technology_data[0]], alpha=0.25, color='#00aaff')
ax_radar.set_title('Technology Known')
st.pyplot(fig_radar)

# Create pie chart for skills data
skills_data = [30, 60, 25, 33]
skills_labels = ['MYSQL', 'Python', 'Dashboard Development', 'Power Bi']

# Skills Proficiency section (Pie Chart)
st.header('Skills Proficiency')
fig_skills, ax_skills = plt.subplots()
ax_skills.pie(skills_data, labels=skills_labels, autopct='%1.1f%%', startangle=90, colors=['#00aaff', '#ffbb00', '#ff5500', '#ff00aa'])
ax_skills.axis('equal')
ax_skills.set_title('Skills Proficiency')
st.pyplot(fig_skills)

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























