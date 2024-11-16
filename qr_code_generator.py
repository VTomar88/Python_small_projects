import qrcode

# Get user data and filename input
data = input('Enter the text or URL: ').strip()
filename = input('Enter the filename: ').strip()

# Genrate the QR code for the data
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
# Embed the data generated QR in an image
image = qr.make_image(fill_color='black', back_color='white')
# Save the image
image.save(filename)

print(f'QR code saved as {filename}')