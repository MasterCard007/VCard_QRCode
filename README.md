
# QRcodeGen

## Overview

`QRcodeGen` is a Python script designed to generate QR codes from user-provided text or URLs. This tool is useful for quickly creating QR codes that can be scanned by mobile devices to access websites, text, or other encoded information.

## Features

- **Generate QR Codes**: Convert any text or URL into a QR code.
- **Save QR Codes**: The generated QR codes can be saved as image files.
- **Customizable Output**: You can specify the output file name and directory for saving the QR codes.

## Requirements

- Python 3.x
- Required Python packages:
  - `qrcode`
  - `PIL` (Pillow)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/MasterCard007/VCard_QRCode.git
    cd QRcodeGen
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```bash
    python QRcodeGen.py
    ```

2. Follow the prompts to enter the text or URL you wish to convert into a QR code.

3. Specify the output file name and directory where you want to save the QR code image.

## Example

Here’s an example of generating a QR code for a URL:

```bash
python QRcodeGen.py
```

- Input: `https://github.com/MasterCard007/VCard_QRCode`
- Output: A QR code image saved in the specified directory.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss the changes you would like to make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please reach out via the [issues page](https://github.com/MasterCard007/VCard_QRCode/issues) on GitHub.
