try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import cloze

def ocr(filedir):
    print(pytesseract.image_to_string(Image.open(filedir)))
    return cloze.clozer(pytesseract.image_to_string(Image.open(filedir)))
