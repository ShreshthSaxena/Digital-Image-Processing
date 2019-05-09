import numpy as np
from PIL import Image

img=Image.open("boat.jpg")

img_ar=np.array(img,dtype=np.float32)

for i in range(img_ar.shape[0]):
	for j in range(img_ar.shape[1]):
		if i>50 and j>50 and i<200 and j<200:#img_ar[i,j] > 123 and img_ar[i,j]<200:
			img_ar[i,j] +=50
		#else:
		#	img_ar[i,j]=0

img_ar = img_ar.astype(np.uint8)

inm=Image.fromarray(img_ar)
inm.show()
