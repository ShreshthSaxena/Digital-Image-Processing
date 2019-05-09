import numpy as np
from PIL import Image,ImageFilter

img=Image.open("unsharp_g.jpg")
img.show()

img_ar=np.array(img,dtype=np.float32)

blur = img.filter(ImageFilter.BLUR)

average = np.array(blur,dtype=np.float32)

blur.show()

mask = img_ar - average

mask[mask<0]=0
mask[mask>255]=0

maskm = mask.astype(np.uint8)
inm=Image.fromarray(maskm)
inm.show()

original = img_ar + (2*mask)
original[original<0]=0
original[original>255]=255
original = original.astype(np.uint8)
inm=Image.fromarray(original)
inm.save('unsharp_g1.jpg')
inm.show()
