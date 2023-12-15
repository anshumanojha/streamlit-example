import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
import qrcode

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

    # Summary
    pdf.drawString(20, page_height - 160, "Summary:")
    summary_text = '''
    - Utilized SQL, Python, and Excel to analyze and interpret complex financial data, providing key insights into team performance and operational efficiency.
    - Created and automated dashboards for MIS and revenue reporting, improving the accuracy and timeliness of information for cross-functional teams.

    Operational Efficiency:
    - Automated routine operational tasks, streamlining processes and reducing manual effort, resulting in increased productivity.
    - Developed frameworks for data analysis on repayment and disbursal, contributing to the creation of efficient operational strategies for the upcoming months.

    Collaboration and Communication:
    - Facilitated the onboarding process for new partners, ensuring seamless integration into existing operations and fostering strong collaborative relationships.
    - Conducted presentations on EMI details to customers, enhancing their understanding and contributing to successful loan repayment outcomes.

    Problem Solving:
    - Identified and resolved operational bottlenecks by applying analytical skills, leading to improved overall workflow and reduced turnaround times.
    - Assisted in the development of frameworks for analyzing data on repayment and disbursal, contributing to more informed decision-making processes.

    Project Management:
    - Led initiatives to enhance operational efficiency, collaborating with cross-functional teams to implement process improvements and achieve organizational objectives.
    - Played a key role in ensuring the success of operational projects through effective planning, execution, and monitoring.

    Technical Proficiency:
    - Demonstrated high proficiency in SQL, Python, and Excel for data manipulation, analysis, and reporting purposes.
    - Actively stayed abreast of industry trends and best practices to incorporate the latest technologies and methodologies into daily operations.

    Metrics and KPIs:
    - Defined and monitored key performance indicators (KPIs) to measure and report on the success of operational initiatives, providing data-driven insights for strategic decision-making.
    '''
    summary_lines = [line.strip() for line in summary_text.split('\n') if line.strip()]
    for i, line in enumerate(summary_lines):
        pdf.drawString(20, page_height - 175 - (i * 15), line)

    # Certifications
    pdf.drawString(20, page_height - 480, "Certifications:")
    certifications = [
        ("- Data Science Certification", "[GitHub - Anshuman Ojha](https://github.com/anshumanojha)", "Lead"),
        ("- Python for Data Science and AI Development", "[Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)", "Lead"),
        ("- Databases and SQL with Python", "Lead"),
        ("- Data Visualization with Python", "[Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)", "Lead"),
        ("- Data Analysis with Python", "[Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)", "Lead"),
        ("- Applied Data Science Capstone", "[Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PFEW9WJEB9UL)", "Lead"),
        ("- IBM Data Science", "[Coursera Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)", "Lead"),
    ]
    for i, (cert, link, lead) in enumerate(certifications):
        pdf.drawString(20, page_height - 495 - (i * 25), cert)
        pdf.drawString(20, page_height - 510 - (i * 25), f"   - Link: {link}")
        pdf.drawString(20, page_height - 525 - (i * 25), f"   - {lead}")

    # QR Code
    qr_data = "https://anshumanojha-streamlit-porfolio-streamlit-app-jqouin.streamlit.app/"
    pdf.drawInlineImage(qrcode.make(qr_data).make_image(fill='black', back_color='white'), 20, page_height - 600)  # Adjust the position as needed

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

# Text beneath the heading
st.write("Click the button to get the resume in PDF")

# Generate PDF button at the top-right corner
if st.button("Generate PDF", key="generate-pdf-btn", help="Generate and download PDF"):
    generate_pdf()

# Personal Information
st.header("Personal Information")

# Display other personal information
st.write("Name: Anshuman Ojha")
st.write("Designation: Finops Analyst")
st.write("Contact: 877743144")
st.write("Email: anshumanojha94@gmail.com")

# Summary
st.header("Summary")
for line in summary_lines:
    st.write(line)

# Certifications
st.header("Certifications")

for cert, link, lead in certifications:
    st.write(cert)
    st.write(f"   - Link: {link}")
    st.write(f"   - {lead}")
