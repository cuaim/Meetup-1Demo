import numpy as np 
import cv2
from pytesseract import image_to_string

# GrayScales the image
img = cv2.imread('./images/calendar.png', cv2.IMREAD_GRAYSCALE)
# Applies threshold to the image to detect rectables
_, thresh= cv2.threshold(img, 225,255, cv2.THRESH_BINARY_INV)
# Finds all rectangles
contours, her = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for i, cnt in enumerate(contours):
	x, y, w, h = cv2.boundingRect(cnt)
	
	blob = img[y:y+h, x:x+w]
	filename = str(i) + '.png'
    cv2.imwrite('contours/'+filename, blob)
	output = image_to_string(blob)
	print output



