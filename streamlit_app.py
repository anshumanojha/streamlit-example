# QR Code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5,
)
qr.add_data("https://anshumanojha-streamlit-porfolio-streamlit-app-jqouin.streamlit.app/")
qr.make(fit=True)

# Convert QR code image to RGB format
img = qr.make_image(fill='black', back_color='white').convert("RGB")

# Save the image to buffer
img_path = "/tmp/qrcode.png"
img.save(img_path)

# Insert QR code into the PDF
pdf.drawInlineImage(buffer, 20, current_height + 30, width=60, height=60)  
img_path.close()
# Adjust the position and size as needed
