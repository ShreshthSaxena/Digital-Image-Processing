import cv2
import numpy as np
 
image = cv2.imread('guassian_noise.jpg')

#np_img=np.array(image,dtype=np.float32)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
#np_img=np.array(gray,dtype=np.float32)

#cv2.imshow('Original image',image)
#cv2.imshow('Gray image', gray)
cv2.imwrite('guassian.jpg',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
