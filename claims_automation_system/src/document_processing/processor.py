import pytesseract
from PIL import Image
import io

def parse_document(file_bytes: bytes) -> dict:
    """
    Extract text from a simple image or document bytes.
    NOTE: This is very basic; extend for PDFs & DOCX.
    """
    try:
        image = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(image)
    except Exception:
        text = file_bytes.decode("utf-8", errors="ignore")  # fallback for text files

    return {
        "raw_text": text[:1000],  # limit for simplicity
    }
