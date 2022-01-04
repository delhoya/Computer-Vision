

import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

test_image = np.array([
     [[255], [0], [255], [255], [0],[255]],
     [[255], [0], [255], [255], [0],[255]],
     [[255], [0], [255], [255], [0],[255]],
     [[255], [0], [255], [255], [0],[255]],
     [[255], [0], [255], [255], [0],[255]],
     [[255], [0], [255], [255], [0],[255]]
])

x_test = np.array([test_image])
x_test = x_test.astype(dtype=np.float32)
plt.imshow(test_image.reshape(6, 6), cmap='gray')
plt.show()

