from PIL import Image
import pandas as pd
import numpy as np

im = Image.open('zatoichi.png') # Can be many different formats.
pix = im.load()
im.show()

from PIL import Image
import pandas as pd
import numpy as np

im = Image.open('zatoichi.png') # Can be many different formats.
pix = im.load()
im.show()
width, height = im.size
array = np.zeros([height,width,3], dtype=np.uint8)

for i in range(width):
    for j in range(height):
        array[j][i] = pix[i,j]
        
new_array = np.zeros([height,width,3], dtype=np.uint8)

new_array[:height//2,:width//3,:] = array[height//2:,width//3:2*width//3,:]
new_array[:height//2,width//3:2*width//3,:] = array[height//2:,:width//3,:]
new_array[:height//2,2*width//3:,:] = array[:height//2,:width//3,:]
new_array[height//2:,:width//3,:] = array[:height//2,2*width//3:,:]
new_array[height//2:,width//3:2*width//3,:] = array[height//2:,2*width//3:,:]
new_array[height//2:,2*width//3:,:] = array[:height//2,width//3:2*width//3:,:]

stream = ""
output = ""
 
# loop each pixel in the first row (y = 0)
for y in range(img.size[1]):
    for x in range(img.size[0]):
     # loop for every channel
     for channel in img.getpixel( (x, y) ):
      # mask all bit except LSB & concat to stream
      stream += str(channel & 1)

    # loop through every 8 bit
    for i in range(0, len(stream), 8):
     # convert binary to ascii char & concat to output stream
     output += chr( int(stream[i:i+8], 2) )

    #print(output)
