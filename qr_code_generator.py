"""
QR Code Generator

This script generates a QR code from user-provided text or a URL and saves it as an image file.

Modules:
    - qrcode: A library for generating QR codes.

Functions:
    - generate_qr_code(data: str, filename: str): Generates and saves a QR code image.
"""

import qrcode


def generate_qr_code(data, filename):
    """
    Generates a QR code from the provided data and saves it as an image file.

    Args:
        data (str): The text or URL to encode in the QR code.
        filename (str): The name of the file to save the QR code image.

    Returns:
        None
    """
    # Create a QRCode object with specific settings
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)  # Add data to the QR code
    qr.make(fit=True)  # Optimize the QR code size to fit the data

    # Generate the QR code image
    image = qr.make_image(fill_color='black', back_color='white')

    # Save the image to the specified filename
    image.save(filename)
    print(f'QR code saved as {filename}')


def main():
    """
    Main function to prompt the user for input and generate the QR code.

    Returns:
        None
    """
    # Get user data and filename input
    data = input('Enter the text or URL to encode: ').strip()
    filename = input(
        'Enter the filename (with extension, e.g., image.png): ').strip()

    # Generate and save the QR code
    generate_qr_code(data, filename)


if __name__ == "__main__":
    main()
