import qrcode

# Set the data and segmentation options
data = "https://www.example.com"
version = 40
num_segments = 4

# Create the QR code image
qr = qrcode.QRCode(
    version=version, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("qr-long.png")
