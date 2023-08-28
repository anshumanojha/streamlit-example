import streamlit as st
import qrcode

# Streamlit app title
st.title("QR Code Generator")

# Input field for the user to enter the URL
user_url = st.text_input("Enter the URL:")

# Function to generate and display the QR code
def generate_qr_code(url):
    if url:
        # Create the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Display the QR code
        st.image(qr_img, use_column_width=True, caption="QR Code")

# Button to trigger QR code generation
if st.button("Generate QR Code"):
    generate_qr_code(user_url)
