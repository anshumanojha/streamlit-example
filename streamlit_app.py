import streamlit as st
import matplotlib.pyplot as plt
from io import BytesIO

# Text Variables
Header = '>>>This resume was generated entirely in Python. For the full source code, view my portfolio.'
Name = 'Anshuman Ojha'
Designation = 'Finops Analyst'
Contact = 'Location: Bangalore\nContact: 877743144\nEmail: anshumanojha94@gmail.com'
WorkExperienceHeader = 'Work Experience'
FinopsTitle = 'Finops(Revenue&Recon Analyst) - Freo'
FinopsDuration = 'Duration: Dec 2019 - Present'
FinopsDesc = '- MIS\n- Revenue automation\n- Partner onboarding\n- Made dashboards to check repayment\n- Day-to-day repayment recon\n- Solving payments disputes\n- Development and verification of monthly partner invoices\n- Handling Data required for partners and vendors\n- Data verification and analysis\n- Data correction'
AssociateTitle = 'Associate(Operations) - Freo'
AssociateDuration = 'Duration: Dec 2019 - Nov 2020'
AssociateDesc = 'Add relevant details about the role'
ProjectsHeader = 'Projects'
DataScienceProject = 'Data Science Certification Lead - May 2020\nLink: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)'
CertificationsHeader = 'Certifications'
DataScienceCertification = 'Data Science Certification\nCertified by IBM in association with Coursera\nLink: [IBM Data Science Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)'
PythonCertification = 'Python for Data Science and AI Development\nLead\nLink: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)'
SQLCertification = 'Databases and SQL with Python\nLead\nLink: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)'
DataVizCertification = 'Data Visualization with Python\nLead\nLink: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)'

# Set up the Streamlit app
st.set_page_config(
    page_title="Anshuman Ojha's Resume",
    page_icon=":clipboard:",
    layout="wide",
)

# Heading
st.title("Anshuman Ojha's Resume")

# Text beneath the heading
st.write("Click the button to get the resume in PDF")

# Personal Information
st.header("Personal Information")
st.write(f"Name: {Name}")
st.write(f"Designation: {Designation}")
st.write(Contact)

# Work Experience
st.header(WorkExperienceHeader)

# Finops(Revenue&Recon Analyst) - Freo
st.subheader(FinopsTitle)
st.write(FinopsDuration)
st.write("Description:")
st.write(FinopsDesc)

# Associate(Operations) - Freo
st.subheader(AssociateTitle)
st.write(AssociateDuration)
st.write("Description:")
st.write(AssociateDesc)

# Projects
st.header(ProjectsHeader)
st.subheader(DataScienceProject)

# Certifications
st.header(CertificationsHeader)
st.write(DataScienceCertification)
st.write(PythonCertification)
st.write(SQLCertification)
st.write(DataVizCertification)
