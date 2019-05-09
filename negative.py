import numpy as np
from PIL import Image

img = Image.open("boat.jpg")

img_array=np.array(img,dtype=np.float32)

img_array[:,:] =255-img_array[:,:]

img_array = img_array.astype(np.uint8)

img=Image.fromarray(img_array)

img.save('boat1.jpg')
