from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

# Create the Dash app
app = dash.Dash(__name__)

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
app.layout = html.Div(children=[
    html.H1('Dashboard'),

    html.H2('Tools Known'),
    dcc.Graph(figure=tools_fig),

    html.H2('Technology Known'),
    dcc.Graph(figure=technology_fig),

    html.H2('Skills Proficiency'),
    dcc.Graph(figure=skills_fig),

    html.H2('Certifications'),
    html.Ul([
        html.Li(html.A('IBM-Data Analysis certificate', href='https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V', target='_blank')),
        html.Li(html.A('IBM-Data Visualization with Python', href='https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX', target='_blank')),
        html.Li(html.A('Databases and SQL for Data Science with Python', href='https://www.coursera.org/account/accomplishments/certificate/ST57AP42DMXS', target='_blank')),
        html.Li(html.A('Machine Learning with Python', href='https://www.coursera.org/account/accomplishments/certificate/PWQGKGYMMMQU', target='_blank')),
        html.Li(html.A('Python for Data Science, AI & Development', href='https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV', target='_blank')),
        html.Li(html.A('IBM Data Science Specialization', href='https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9', target='_blank')),
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
