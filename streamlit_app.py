import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

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
    pdf.drawString(20, page_height - 175, '''
    Utilized SQL, Python, and Excel to analyze and interpret complex financial data, providing key insights into team performance and operational efficiency.
    Created and automated dashboards for MIS and revenue reporting, improving the accuracy and timeliness of information for cross-functional teams.

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
    ''')

    # Certifications
    pdf.drawString(20, page_height - 610, "Certifications:")
    pdf.drawString(20, page_height - 625, "- Data Science Certification")
    pdf.drawString(20, page_height - 640, "   - Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")
    pdf.drawString(20, page_height - 655, "   - Lead")

    pdf.drawString(20, page_height - 680, "- Python for Data Science and AI Development")
    pdf.drawString(20, page_height - 695, "   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)")
    pdf.drawString(20, page_height - 710, "   - Lead")

    pdf.drawString(20, page_height - 735, "- Databases and SQL with Python")
    pdf.drawString(20, page_height - 750, "   - Lead")

    pdf.drawString(20, page_height - 775, "- Data Visualization with Python")
    pdf.drawString(20, page_height - 790, "   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)")
    pdf.drawString(20, page_height - 805, "   - Lead")

    pdf.drawString(20, page_height - 830, "- Data Analysis with Python")
    pdf.drawString(20, page_height - 845, "   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)")
    pdf.drawString(20, page_height - 860, "   - Lead")

    pdf.drawString(20, page_height - 885, "- Applied Data Science Capstone")
    pdf.drawString(20, page_height - 900, "   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PFEW9WJEB9UL)")
    pdf.drawString(20, page_height - 915, "   - Lead")

    pdf.drawString(20, page_height - 940, "- IBM Data Science")
    pdf.drawString(20, page_height - 955, "   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)")
    pdf.drawString(20, page_height - 970, "   - Lead")

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
st.write("Name: Anshuman Ojha")
st.write("Designation: Finops Analyst")
st.write("Contact: 877743144")
st.write("Email: anshumanojha94@gmail.com")

# Summary
st.header("Summary")
st.write('''
    Utilized SQL, Python, and Excel to analyze and interpret complex financial data, providing key insights into team performance and operational efficiency.
    Created and automated dashboards for MIS and revenue reporting, improving the accuracy and timeliness of information for cross-functional teams.

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
''')

# Certifications
st.header("Certifications")

st.write("- Data Science Certification")
st.write("   - Link: [GitHub - Anshuman Ojha](https://github.com/anshumanojha)")
st.write("   - Lead")

st.write("- Python for Data Science and AI Development")
st.write("   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/EYQS7XR5JQGV)")
st.write("   - Lead")

st.write("- Databases and SQL with Python")
st.write("   - Lead")

st.write("- Data Visualization with Python")
st.write("   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/YWQBBWNA4CHX)")
st.write("   - Lead")

st.write("- Data Analysis with Python")
st.write("   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PHKLT6LDUU3V)")
st.write("   - Lead")

st.write("- Applied Data Science Capstone")
st.write("   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/certificate/PFEW9WJEB9UL)")
st.write("   - Lead")

st.write("- IBM Data Science")
st.write("   - Link: [Coursera Certification](https://www.coursera.org/account/accomplishments/specialization/certificate/YBQ7NCKANHJ9)")
st.write("   - Lead")
