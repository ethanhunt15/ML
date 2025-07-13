import fitz 
import pytesseract
from PIL import Image

def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")  # mode 'text' for raw text extraction
        print(f"Page {page_num} text length:", len(text))
        if len(text) ==0:
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(img)
            print(f"Page {page_num} OCR text length:", len(text))
    return text