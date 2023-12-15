import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

st.write("Click the button to generate PDF Resume")
def generate_pdf():
    buffer = BytesIO()

    # Create a PDF object
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.setFont("Helvetica", 8)  # Change the font and size as needed

    # Add borders to the PDF
    page_width, page_height = letter
    pdf.line(0, page_height, page_width, page_height)  # Top border
    pdf.line(0, page_height, 0, 0)                     # Left border
    pdf.line(0, 0, page_width, 0)                      # Bottom border
    pdf.line(page_width, 0, page_width, page_height)   # Right border

    # Set up the PDF content with left alignment
    pdf.drawString(20, page_height - 20, ">>>This resume was generated entirely in Python. For the full source code, view my portfolio.")
    pdf.drawString(20, page_height - 40, "Anshuman Ojha's Resume")
    pdf.line(0, page_height - 45, page_width, page_height - 45)  # Top border for header

    # Personal Information
    pdf.drawString(20, page_height - 60, "Personal Information:")
    pdf.drawString(20, page_height - 75, "- Location: Bangalore")
    pdf.drawString(20, page_height - 90, "- Name: Anshuman Ojha")
    pdf.drawString(20, page_height - 105, "- Designation: Finops Analyst")
    pdf.drawString(20, page_height - 120, "- Contact: 877743144")
    pdf.drawString(20, page_height - 135, "- Email: anshumanojha94@gmail.com")

    # Work Experience
    pdf.drawString(20, page_height - 160, "Work Experience:")
    
    # Finops(Revenue&Recon Analyst) - Freo
    pdf.drawString(20, page_height - 175, "- Finops(Revenue&Recon Analyst) - Freo")
    pdf.drawString(20, page_height - 190, "   - Duration: Dec 2019 - Present")
    pdf.drawString(20, page_height - 205, "   - Description:")
    pdf.drawString(40, page_height - 220, "     - MIS")
    pdf.drawString(40, page_height - 235, "     - Revenue automation")
    pdf.drawString(40, page_height - 250, "     - Partner onboarding")
    # Add more content as needed

    # Associate(operations) - Freo
    pdf.drawString(20, page_height - 275, "- Associate(Operations) - Freo")
    pdf.drawString(20, page_height - 290, "   - Duration: Dec 2019 - Nov 2020")
    pdf.drawString(20, page_height - 305, "   - Description:")
    # Add relevant details about the role

    # Projects
    pdf.drawString(20, page_height - 330, "Projects:")
    pdf.drawString(20, page_height - 345, "- Data Science Certification Lead - May 2020")
    pdf.drawString(20, page_height - 360, "   - Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")

    # Certifications
    pdf.drawString(20, page_height - 385, "Certifications:")
    pdf.drawString(20, page_height - 400, "- Data Science Certification:")
    pdf.drawString(20, page_height - 415, "   - Certified by IBM in association with Coursera")
    pdf.drawString(20, page_height - 430, "   - Link: [IBM Data Science Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)")

    # Additional Certifications
    pdf.drawString(20, page_height - 455, "- Python for Data Science and AI Development:")
    pdf.drawString(20, page_height - 470, "   - Lead")
    pdf.drawString(20, page_height - 485, "   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)")

    pdf.drawString(20, page_height - 510, "- Databases and SQL with Python:")
    pdf.drawString(20, page_height - 525, "   - Lead")
    pdf.drawString(20, page_height - 540, "   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)")

    pdf.drawString(20, page_height - 565, "- Data Visualization with Python:")
    pdf.drawString(20, page_height - 580, "   - Lead")
    pdf.drawString(20, page_height - 595, "   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)")

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

# Text beneath the heading
st.write("Bangalore")

# Personal Information
st.header("Personal Information")

# Display other personal information
st.write("Name: Anshuman Ojha")
st.write("Designation: Finops Analyst")
st.write("Contact: 877743144")
st.write("Email: anshumanojha94@gmail.com")

# Work Experience
st.header("Work Experience")

# Finops(Revenue&Recon Analyst) - Freo
st.subheader("Finops(Revenue&Recon Analyst) - Freo")
st.write("Duration: Dec 2019 - Present")
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
