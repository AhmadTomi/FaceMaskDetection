import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread('jeremy.jpeg')
print('Type: ', type(img), 'Dimension: ', img.shape)

plt.imshow(img)