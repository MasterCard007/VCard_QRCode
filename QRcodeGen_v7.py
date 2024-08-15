import qrcode
from PIL import Image
import json
import os


def create_qr_code(data, file_path, error_correction, logo_path=None, logo_size_ratio=0.2):
    
    # Generate the QR code
    qr = qrcode.QRCode(
        version=None,  # Automatically determine the best version
        error_correction=error_correction,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # If a logo path is provided, overlay the logo onto the QR code
    if logo_path:
        logo = Image.open(logo_path)

        # Calculate the logo size based on the QR code size and the specified ratio
        qr_width, qr_height = img.size
        logo_size = int(logo_size_ratio * qr_width)
        logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

        # Calculate the position to place the logo
        logo_position = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

        # Paste the logo onto the QR code
        img.paste(logo, logo_position, mask=logo)

    # Save the final image
    img.save(file_path)

def generate_vcard(name, phone, email, nickname, website, linkedin):
    vcard = "BEGIN:VCARD\nVERSION:3.0\n"
    if name:
        vcard += f"N:{name}\n"
    if phone:
        vcard += f"TEL:{phone}\n"
    if email:
        vcard += f"EMAIL:{email}\n"
    if nickname:
        vcard += f"NICKNAME:{nickname}\n"
    if website:
        vcard += f"URL:{website}\n"
    if linkedin:
        vcard += f"NOTE:LinkedIn Profile - {linkedin}\n"
    vcard += "END:VCARD"
    return vcard

def process_json_file(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    filename = os.path.basename(json_file)
    file_type = filename.split('_')[0]

    if file_type.lower() == 'url':
        url = data.get('url', '')
        if url:
            create_qr_code(url, os.path.splitext(json_file)[0] + ".png")
            print(f"QR code for URL has been saved as {os.path.splitext(json_file)[0]}.png")
        else:
            print("URL cannot be empty.")
    elif file_type.lower() == 'vcard':
        name = data.get('name', '')
        phone = data.get('phone', '')
        email = data.get('email', '')
        nickname = data.get('nickname', '')
        website = data.get('website', '')
        linkedin = data.get('linkedin', '')
        logo_path = data.get('logo_path', '')  # New entry for logo path

        vcard_data = generate_vcard(name, phone, email, nickname, website, linkedin)
        
    # Loop through all error correction levels and create a QR code for each
    error_corrections = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }

    for level, correction in error_corrections.items():
        file_path = os.path.splitext(json_file)[0] + f"_{level}.png"
        create_qr_code(vcard_data, file_path, correction, logo_path=logo_path)
    
        print(f"QR code for V card has been saved as {os.path.splitext(json_file)[0]}.png")
    else:
        print("Unsupported file type.")

def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))

    json_files = [f for f in os.listdir(script_dir) if f.endswith('.json')]

    if not json_files:
        print("No JSON files found in the directory.")
        return

    for json_file in json_files:
        process_json_file(os.path.join(script_dir, json_file))

if __name__ == "__main__":
    main()

def generate_qr_codes_for_all_levels(data, base_file_path, logo_path=None):
    error_corrections = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H,
    }

    for level, correction in error_corrections.items():
        file_path = f"{base_file_path}_{level}.png"
        create_qr_code(data, file_path, correction, logo_path)
        print(f"QR code generated and saved as {file_path}")

# Example usage
if __name__ == "__main__":
    data = "https://example.com"
    base_file_path = "QRCode"
    logo_path = None  # Optional: provide the path to the logo image if needed
    generate_qr_codes_for_all_levels(data, base_file_path, logo_path)
