import numpy as np
from PIL import Image

img=Image.open("salt_and_pepper_noise.jpg")

img_ar=np.array(img,dtype=np.float32)

padded = np.zeros((img_ar.shape[0]+2,img_ar.shape[1]+2))
print(img_ar.shape)
print(padded.shape)

for i in range(img_ar.shape[0]):
	for j in range(img_ar.shape[1]):
		padded[i+1,j+1] = img_ar[i,j]

for i in range(1,padded.shape[0]-1):
	lists = []
	for j in range(1,padded.shape[1]-1):
		lists = [padded[i,j],padded[i+1,j],padded[i-1,j],padded[i,j-1],padded[i,j+1],padded[i-1,j-1],padded[i+1,j+1],padded[i+1,j-1],padded[i-1,j+1]]
		lists = sorted(lists)
		padded[i,j] = lists[4]

print(padded.shape)
padded = padded.astype(np.uint8)
inm=Image.fromarray(padded)
inm.save('sa.jpg')
inm.show()
