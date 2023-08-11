import streamlit as st
import base64
import io
import fitz

def convert_pdf_to_text(pdf_content):
    doc = fitz.open(stream=pdf_content, filetype="pdf")
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    doc.close()
    return text

def main():
    st.title("PDF to Text Conversion")
    
    uploaded_file = st.file_uploader("Select a PDF File", type=["pdf"])
    
    if uploaded_file is not None:
        pdf_content = uploaded_file.read()
        
        extracted_text = convert_pdf_to_text(pdf_content)
        
        # Display extracted text
        st.subheader(f'Extracted Text from {uploaded_file.name}:')
        st.text_area("Extracted Text", extracted_text, height=300)
        
        # Create a downloadable text file
        txt_file_content = extracted_text.encode('utf-8')
        txt_data_uri = base64.b64encode(txt_file_content).decode('utf-8')
        st.download_button("Download as TXT", data=txt_data_uri, file_name='output.txt')

if __name__ == "__main__":
    main()

