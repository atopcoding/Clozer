try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cloze

def 

print(pytesseract.image_to_string(Image.open('test.png')))
