# -*- coding: utf-8 -*-

import cv2
import numpy as np

# 按位运算

# Load two images
img1 = cv2.imread('../data/messi5.jpg')
img2 = cv2.imread('../data/opencv_logo.png')

img1_copy = img1.copy()

# I want to put logo on top-left corner, So I create a ROI
img2 = cv2.resize(img2, (300, 300))
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  # opencv 3.0

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
# logo in ROI -> image

cv2.imshow('img1_copy', img1_copy)
roi_add = img1_copy[0:rows, 0:cols]
# logo ROI overlap
roi_add = cv2.addWeighted(roi_add, 0.5, img2, 0.5, 0)
cv2.imshow('roi_add', roi_add)
# take only region of add log from log image
img2_fg_add = cv2.bitwise_and(roi_add, roi_add, mask=mask)
dst_add = cv2.add(img1_bg, img2_fg_add)
img1_copy[0:rows, 0:cols] = dst_add
cv2.imshow('dst_add', img1_copy)


cv2.waitKey(0)
cv2.destroyAllWindows()

# 左 的图像是我们创建的掩码。右 的是最终结果。
# 为了帮助大 家理解，我把上面程序的中间结果也显示了出来
# 特别是 img1_bg 和 img2_fg。
