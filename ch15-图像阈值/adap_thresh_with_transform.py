import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/sudoku.jpg', 0)
rows, cols = img.shape
print(rows)
print(cols)

plt.imshow(img)


pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
img_trans = cv2.warpPerspective(img, M, (300, 300))
plt.imshow(img_trans)

img_blur = cv2.medianBlur(img_trans, 5)
plt.imshow(img_blur)

img_gaus = cv2.GaussianBlur(img_trans, (5, 5), 0)
plt.imshow(img_gaus)


img_blur_th = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 23, 2)
img_gaus_th = cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 2)


img_li = [img, img_trans, img_blur, img_gaus, img_blur_th, img_gaus_th]
for i in range(6):
    plt.subplot(3, 2, i+1)
    plt.imshow(img_li[i], 'gray')

plt.show()
