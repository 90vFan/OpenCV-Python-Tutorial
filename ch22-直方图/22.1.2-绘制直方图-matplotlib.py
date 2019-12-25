# -*-coding:utf8-*-#
__author__ = 'play4fun'
"""
create time:15-10-24 下午5:17
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/home.jpg', 0)

plt.subplots(1, 2)
plt.subplot(121)
plt.imshow(img)

plt.subplot(122)
# img.ravel() 将图像转成一维数组   没有中括号
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

