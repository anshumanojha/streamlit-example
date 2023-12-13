import streamlit as st
from reportlab.pdfgen import canvas
from io import BytesIO
import pandas as pd

# Function to generate PDF
def generate_pdf():
    buffer = BytesIO()

    # Create a PDF object
    pdf = canvas.Canvas(buffer)

    # Set up the PDF content
    pdf.setFont("Helvetica", 14)
    pdf.drawString(100, 800, "Anshuman Ojha's Resume")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(100, 780, "Personal Information:")
    pdf.drawString(120, 760, f"Name: Anshuman")
    pdf.drawString(120, 740, f"Designation: Finops Analyst")
    pdf.drawString(120, 720, f"Contact: 877743144")
    pdf.drawString(120, 700, f"Email: anshumanojha94@gmail.com")

    # Work Experience
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(100, 670, "Work Experience:")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(120, 650, "- MIS")
    pdf.drawString(120, 635, "- Revenue automation")
    # Add other work experience details

    # ... Add the rest of the content

    # Save the PDF to the buffer
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

# Freo
st.subheader("Finops(Revenue&Recon Analyst) - Freo")
st.write("Duration: Dec 2020 - Present")
st.write("Description:")
st.write("- MIS")
st.write("- Revenue automation")
# Add other work experience details

# Previous Experience
st.subheader("Associate(Operations) - Freo")
st.write("Duration: Dec 2019 - Nov 2020")
st.write("Description:")
# Add relevant details about the role

# Skills
st.header("Skills")
st.write("- Python")
st.write("- SQL")
st.write("- Advanced Excel")
st.write("- Power BI")
st.write("- SuperSet")

# Education
st.header("Education")
st.write("BE - MVJ, Aug 2019")

# Data Science Certification
st.header("Data Science Certification")
st.write("Certified by IBM in association with Coursera")
st.write("Link: [IBM Data Science Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)")

# Projects
st.header("Projects")
st.subheader("Data Science Certification Lead - May 2020")
st.write("Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")

# Skills
st.header("Skills")
st.write("- Python")
st.write("- SQL")
st.write("- Advanced Excel")
st.write("- Power BI")
st.write("- SuperSet")

# Location Map
st.header("Location Map - Bangalore")
location_data = pd.DataFrame({
    "latitude": [12.9716],  # Bangalore latitude
    "longitude": [77.5946]  # Bangalore longitude
})
st.map(location_data)

# SQL Query Suggestor (retain the existing code)
