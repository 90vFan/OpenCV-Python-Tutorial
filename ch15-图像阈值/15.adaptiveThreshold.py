# -*- coding: utf-8 -*-

'''
自适应阈值

Adaptive Method- 指定 算阈值的方法。
– cv2.ADPTIVE_THRESH_MEAN_C  值取自相邻区域的平均值
– cv2.ADPTIVE_THRESH_GAUSSIAN_C  值取值相邻区域 的加权和 ，权重为一个高斯窗口
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('dave.jpg', 0)
img = cv2.imread('../data/sudoku.jpg', 0)
img_copy = img.copy()
# 中值滤波
img = cv2.medianBlur(img, 5)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

img_gaus = cv2.GaussianBlur(img_copy, (5, 5), 0)
ret_OTSU, th_OTSU = cv2.threshold(img_gaus, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)


# 11 为 Block size 邻域大小 用来计算阈值的区域大小 ,
# 2 为 C值，常数， 阈值就等于的平均值或者加权平均值减去这个常数。
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

th5 = cv2.adaptiveThreshold(img_gaus, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ['Original Image', 'Global Thresholding (v = 127)', 'OTSU threshoding',
          'Adaptive Mean Thresh', 'Adaptive Gaussian Thresh', 'Adaptive Gaussian gaus']
images = [img, th1, th_OTSU, th2, th3, th5]

plt.subplots(3, 2)
for i in range(6):
    plt.subplot(3, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
