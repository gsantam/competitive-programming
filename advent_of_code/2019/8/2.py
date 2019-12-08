n = 25
m = 6 
photo = open("input.txt","r").read().strip()
layers = int(len(photo)/(n*m))

image = []
for j in range(m):
    for i in range(n):
        first_non_transparent = -1
        for layer in range(layers):
            pixel = int(photo[layer*m*n+j*n + i])
            if pixel!=2 and first_non_transparent==-1:
                first_non_transparent = pixel
        image.append(first_non_transparent)

import matplotlib.pyplot as plt
import numpy as np
imgplot = plt.imshow(np.asarray(image).reshape([6,25]))
