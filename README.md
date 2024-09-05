# extract-text-from-image

This program extracts text from images using Optical Character Recognition (OCR) technology.

## Features

- Processes image files to extract text content
- Supports various image formats (PNG, JPG, JPEG, etc.)
- Outputs extracted text to a file or console

## Prerequisites

Before running the program, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/extract-text-from-image.git
   cd extract-text-from-image
   ```

2. Install the required packages:
   ```
   pip install pytesseract Pillow
   ```

3. Install Tesseract OCR:
   - On Windows: Download and install from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - On macOS: `brew install tesseract`
   - On Linux: `sudo apt-get install tesseract-ocr`

## Usage

Run the program with the following command:
```
python3 start.py 
```