import cv2
import numpy as np
import matplotlib.pyplot as plt

# 500 x 250
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')

add = img1+img2
add_cv = cv2.add(img1, img2)
# cv2.imshow('add',add)
print(img1[102, 110, 1])
print(img2[102, 110, 1])
print(add[102, 110, 1])
print(add_cv[102, 110, 1])

# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# cv2.imshow('weighted', weighted)

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)


ret, mask = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)


mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)


cv2.imshow('img3gray', img3gray)
cv2.imshow('mask', mask)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img3_fg', img3_fg)

dst = cv2.add(img1_bg, img3_fg)
cv2.imshow('dst', dst)


img1[0:rows, 0:cols] = dst
cv2.imshow('res', img1)


cv2.waitKey(0)
cv2.destroyAllWindows()
