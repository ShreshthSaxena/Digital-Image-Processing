from PIL import Image
from matplotlib import pyplot as plt
import numpy as np


img = Image.open('pix2.jpg') 
img_array = np.array(img,dtype=np.float32)
print(img_array.shape)

flat_array= img_array.reshape(1,-1)
print(flat_array.shape)

freq = {}

no_of_pixels = img_array.size

for i in range(256):
	freq[i]=0
	
for i in range(no_of_pixels):
	if flat_array[0,i] in freq:
		freq[flat_array[0,i]]=freq[flat_array[0,i]]+1
		
#print("frequency:",freq)

pdf = {}
L = 255
value = 0
for key in freq:
	
	pdf[key] = (freq[key])/no_of_pixels

#print("PROBABILITY DISTRUBUTION FUNCTION:",pdf)
cdf = {}
for key in pdf:
	
	cdf[key] = round(L*(pdf[key]+value))
	value = value+pdf[key]

#print("cUMULATIVE DISTRUBUTION FUNCTION:",cdf)

f1=plt.figure(1)
plt.bar(pdf.keys(), pdf.values(), width=.5, color='b')
#plt.show()

new_freq = {}
for i in freq:
	new_freq[i]=0
	
for i in freq:
	new_freq[cdf[i]] += freq[i]

new_pdf = {}
for key in freq:
	new_pdf[key] = new_freq[key]/no_of_pixels
	
f2 = plt.figure(2)
plt.bar(new_pdf.keys(), new_pdf.values(), width=.5, color='g')
plt.show()

for i in range(flat_array.size):	
	flat_array[0,i]= cdf[flat_array[0,i]]
	
image= flat_array.reshape(600,900,3)

image = image.astype(np.uint8)
inm=Image.fromarray(image)

inm.save('pix_hist.jpg')

