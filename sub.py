from PIL import Image
import numpy as np
import cv2

img1 = cv2.imread('s1.png')
img2 = cv2.imread('s2.png')

imag1 = np.array(img1,dtype= np.float32)
imag2 = np.array(img2,dtype= np.float32)

img=img2-img1

cv2.imwrite("s.jpg",img)

