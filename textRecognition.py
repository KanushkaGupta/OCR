import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 1. Load the image
img=cv2.imread("img.jpg")

# 2. Resize the image
#img = cv2.resize(img, None, fx=0.5, fy=0.5)

# 3. Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Convert image to black and white (using adaptive threshold)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85,11)

# 5. Remove noise
#noise = cv2.medianBlur(adaptive_threshold, 1)

text = pytesseract.image_to_string(adaptive_threshold)
print(text)

cv2.imshow("Image",  adaptive_threshold)
cv2.waitKey(0)