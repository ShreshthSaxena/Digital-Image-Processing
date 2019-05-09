import cv2
import numpy as np

img = cv2.imread('j.png',0)

img_cc = cv2.imread('it.jpg',0)

kernel = np.ones((5,5),np.uint8) #structuring element 1

kernel1 = np.ones((15,15),np.uint8) #structuring element 2

erosion = cv2.erode(img,kernel,iterations = 1) #erosion

dilation = cv2.dilate(img,kernel,iterations = 1) #dilation

opening = cv2.morphologyEx(img_cc, cv2.MORPH_OPEN, kernel1) #opening

closing = cv2.morphologyEx(img_cc, cv2.MORPH_CLOSE, kernel1) #closing

gradient = cv2.morphologyEx(img_cc, cv2.MORPH_GRADIENT, kernel) #boundary

cv2.imshow('original',img)
cv2.imshow("erosion",erosion)
cv2.imshow("dilation",dilation)
cv2.imshow('opening',opening)
cv2.imshow("closing",closing)
cv2.imshow("boundary",gradient)

cv2.waitKey(0)
