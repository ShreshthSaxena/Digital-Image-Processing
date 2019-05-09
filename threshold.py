import numpy as np
from PIL import Image

img=Image.open("boat.jpg")

img_ar=np.array(img,dtype=np.float32)

print(img_ar.shape)

img_ar[img_ar<132]=0

img_ar[img_ar>132]=255

img_ar = img_ar.astype(np.uint8)

inm=Image.fromarray(img_ar)
#inm.show()
