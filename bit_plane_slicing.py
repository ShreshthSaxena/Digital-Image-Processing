import numpy as np
from PIL import Image

img = Image.open("boat.jpg")

img_array=np.array(img,dtype=np.float32)

def toImage(layer):
	img_array = layer.astype(np.uint8)
	img=Image.fromarray(img_array)
	return img

print("original array",img_array)

layer0 = (img_array[:,:]%2)
print("layer0",layer0)
img=toImage(layer0[:,:]*255)
img.save('boat_layer0.jpg')

img_array[:,:] = np.floor(img_array[:,:]/2)

print("array after layer0:",img_array)
layer1 = (img_array[:,:]%2)
img=toImage(layer1[:,:]*255)
img.save('boat_layer1.jpg')

img_array[:,:] = np.floor(img_array[:,:]/2)

print("array after layer1:",img_array)
layer2 = (img_array[:,:]%2)
img=toImage(layer2[:,:]*255)
img.save('boat_layer2.jpg')

img_array[:,:] = np.floor(img_array[:,:]/2)

print("array after layer2:",img_array)
layer3 = (img_array[:,:]%2)
img=toImage(layer3[:,:]*255)
img.save('boat_layer3.jpg')

img_array[:,:] = np.floor(img_array[:,:]/2)

print("array after layer3:",img_array)
layer4 = (img_array[:,:]%2)
img=toImage(layer4[:,:]*255)
img.save('boat_layer4.jpg')

img_array[:,:] = np.floor(img_array[:,:]/2)

print("array after layer4:",img_array)
layer5 = (img_array[:,:]%2)
img=toImage(layer5[:,:]*255)
img.save('boat_layer5.jpg')

img_array[:,:] = np.floor(img_array[:,:]/2)

print("array after layer5:",img_array)
layer6 = (img_array[:,:]%2)
img=toImage(layer6[:,:]*255)
img.save('boat_layer6.jpg')

img_array[:,:] = np.floor(img_array[:,:]/2)

print("array after layer6:",img_array)
layer7 = (img_array[:,:]%2)
img=toImage(layer7[:,:]*255)
img.save('boat_layer7.jpg')

final= layer0+2*layer1+4*layer2+8*layer3+16*layer4+32*layer5+64*layer6+128*layer7
img=toImage(final)
img.save('boat_layer 9.jpg')

