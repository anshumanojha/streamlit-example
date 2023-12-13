import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

# Function to generate PDF
def generate_pdf():
    buffer = BytesIO()

    # Create a PDF object
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 14)

    # Add borders to the PDF
    page_width, page_height = letter
    pdf.line(0, page_height, page_width, page_height)  # Top border
    pdf.line(0, page_height, 0, 0)                     # Left border
    pdf.line(0, 0, page_width, 0)                      # Bottom border
    pdf.line(page_width, 0, page_width, page_height)

    # Set up the PDF content with center alignment
    pdf.drawString(20, page_height - 20, "Anshuman Ojha's Resume")
    pdf.line(0, page_height - 25, page_width, page_height - 25)  # Top border for header

    # Personal Information
    pdf.drawString(100, 750, "Personal Information:")
    pdf.drawString(100, 730, "Location: Bangalore")
    pdf.drawString(100, 710, "Name: Anshuman")
    pdf.drawString(100, 690, "Designation: Finops Analyst")
    pdf.drawString(100, 670, "Contact: 877743144")
    pdf.drawString(100, 650, "Email: anshumanojha94@gmail.com")

    # Work Experience
    pdf.drawString(100, 620, "Work Experience:")
    pdf.drawString(100, 600, "Finops(Revenue&Recon Analyst) - Freo")
    pdf.drawString(120, 580, "Duration: Dec 2020 - Present")
    pdf.drawString(120, 560, "Description:")
    pdf.drawString(140, 540, "- MIS")
    pdf.drawString(140, 520, "- Revenue automation")
    pdf.drawString(140, 500, "- Partner onboarding")
    pdf.drawString(140, 480, "- Made dashboards to check repayment")
    pdf.drawString(140, 460, "- Day-to-day repayment recon")
    pdf.drawString(140, 440, "- Solving payments disputes")
    pdf.drawString(140, 420, "- Development and verification of monthly partner invoices")
    pdf.drawString(140, 400, "- Handling Data required for partners and vendors")
    pdf.drawString(140, 380, "- Data verification and analysis")
    pdf.drawString(140, 360, "- Data correction")

    pdf.drawString(100, 320, "Associate(Operations) - Freo")
    pdf.drawString(120, 300, "Duration: Dec 2019 - Nov 2020")
    pdf.drawString(120, 280, "Description:")
    # Add relevant details about the role

    # Projects
    pdf.drawString(100, 240, "Projects:")
    pdf.drawString(120, 220, "Data Science Certification Lead - May 2020")
    pdf.drawString(140, 200, "Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")

    # Certifications
    pdf.drawString(100, 160, "Certifications:")
    pdf.drawString(120, 140, "Data Science Certification:")
    pdf.drawString(140, 120, "Certified by IBM in association with Coursera")
    pdf.drawString(140, 100, "Link: [IBM Data Science Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)")

    pdf.drawString(120, 80, "Additional Certifications:")
    pdf.drawString(140, 60, "Python for Data Science and AI Development:")
    pdf.drawString(140, 40, "Lead")
    pdf.drawString(140, 20, "Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)")

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

# Finops(Revenue&Recon Analyst) - Freo
st.subheader("Finops(Revenue&Recon Analyst) - Freo")
st.write("Duration: Dec 2020 - Present")
st.write("Description:")
st.write("- MIS")
st.write("- Revenue automation")
st.write("- Partner onboarding")
st.write("- Made dashboards to check repayment")
st.write("- Day-to-day repayment recon")
st.write("- Solving payments disputes")
st.write("- Development and verification of monthly partner invoices")
st.write("- Handling Data required for partners and vendors")
st.write("- Data verification and analysis")
st.write("- Data correction")

# Associate(operations) - Freo
st.subheader("Associate(Operations) - Freo")
st.write("Duration: Dec 2019 - Nov 2020")
st.write("Description:")
# Add relevant details about the role

# Projects
st.header("Projects")
st.subheader("Data Science Certification Lead - May 2020")
st.write("Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")

# Certifications
st.header("Certifications")
st.write("Data Science Certification:")
st.write("Certified by IBM in association with Coursera")
st.write("Link: [IBM Data Science Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)")

# Additional Certifications
st.write("Python for Data Science and AI Development:")
st.write("Lead")
st.write("Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)")

st.write("Databases and SQL with Python:")
st.write("Lead")
st.write("Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)")

st.write("Data Visualization with Python:")
st.write("Lead")
st.write("Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)")
