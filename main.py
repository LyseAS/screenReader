import numpy as np
from PIL import ImageGrab
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
from textblob import TextBlob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Grab some screen
screen = ImageGrab.grab(bbox=(1371, 322, 1513, 925))
# Make greyscale
w = screen.convert('L')

# Save so we can see what we grabbed
w.save('grabbed.png')

text = pytesseract.image_to_string(w)
correctedText = TextBlob(text).correct()

print(correctedText)

text_file = open("Counting.txt", "a")
text_file.write('\t' + str(correctedText))
text_file.close()
