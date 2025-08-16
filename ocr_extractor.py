import os
import pytesseract
from PIL import Image
import PyPDF2

INPUT_FOLDER = "input_files"
OUTPUT_FOLDER = "output_files"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Path to Tesseract (only if needed, adjust for your PC installation)
# Example for Windows: r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# --------------------------
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(pdf_path, output_path):
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"[PDF] Extracted text saved to {output_path}")

def extract_text_from_image(image_path, output_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"[IMG] Extracted text saved to {output_path}")

def main():
    for filename in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, filename)
        name, ext = os.path.splitext(filename)
        output_file = os.path.join(OUTPUT_FOLDER, f"{name}.txt")

        if ext.lower() == ".pdf":
            extract_text_from_pdf(file_path, output_file)
        elif ext.lower() in [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]:
            extract_text_from_image(file_path, output_file)
        else:
            print(f"Skipped: {filename} (unsupported format)")

if __name__ == "__main__":
    main()
