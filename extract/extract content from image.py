import pytesseract
from PIL import Image

# Open image using PIL
img = Image.open(r'C:\Users\jayapradha\Desktop\extract\image.png')

# Apply OCR using Tesseract
text = pytesseract.image_to_string(img, lang='eng')

# Print extracted text
print(text)
