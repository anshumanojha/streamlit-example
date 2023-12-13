import streamlit as st
from reportlab.pdfgen import canvas
from io import BytesIO
import pandas as pd

# Function to generate PDF
def generate_pdf():
    buffer = BytesIO()

    # Create a PDF object
    pdf = canvas.Canvas(buffer)

    # Set up the PDF content (you may need to adjust the coordinates and styles)
    pdf.drawString(100, 800, "Anshuman Ojha's Resume")
    pdf.drawString(100, 780, "Personal Information:")
    pdf.drawString(120, 760, f"Name: Anshuman")
    pdf.drawString(120, 740, f"Designation: Finops Analyst")
    pdf.drawString(120, 720, f"Contact: 877743144")
    pdf.drawString(120, 700, f"Email: anshumanojha94@gmail.com")

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

# Anshuman's Resume
st.title("Anshuman Ojha's Resume")

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
st.write("- Partner onboarding")
st.write("- Made dashboards to check repayment")
st.write("- Day-to-day repayment reconciliation")
st.write("- Solving payments disputes")
st.write("- Development and verification of monthly partner invoices")
st.write("- Handling data required for partners and vendors")
st.write("- Data verification and analysis")
st.write("- Data correction")

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

# Generate PDF button at the top right corner
if st.button("Generate PDF"):
    generate_pdf()
