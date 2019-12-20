# -*- coding: utf-8 -*-
# @Time    : 2017/8/2 10:46
# @Author  : play4fun
# @File    : test_video.py
# @Software: PyCharm

"""
test_video.py:
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

cap = cv2.VideoCapture('../../data/vtest.avi')#不支持读取视频
# cap = cv2.VideoCapture('output.avi')
# cap = cv2.VideoCapture('Minions_banana.mp4')


# 帧率
fps = cap.get(cv2.CAP_PROP_FPS)  # 25.0
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
# 总共有多少帧
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print('共有', num_frames, '帧')
#
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print('高：', frame_height, '宽：', frame_width)

FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 第0帧
print('当前帧数', FRAME_NOW)  # 当前帧数 0.0

# 读取指定帧,对视频文件才有效，对摄像头无效？？
# frame_no = 121
# cap.set(1, frame_no)  # Where frame_no is the frame you want
ret, frame = cap.read()  # Read the frame
print(ret, frame)
# cv2.imshow('frame_no'+str(frame_no), frame)

FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)
print('当前帧数', FRAME_NOW)  # 当前帧数 122.0

# if frame is not  None:#出错
#     plt.imshow(frame)
#     # plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#     plt.show()

from matplotlib.pyplot import figure, draw, pause

# plt.ion()
#
# im = plt.imshow(frame)
#
# for i in range(100):
#     ret, frame = cap.read()
#     im.set_array(frame)
#     draw()
#     plt.pause(0.1)
#
# plt.ioff()
# plt.show()


# from matplotlib.pyplot import figure, draw, pause


# fg = figure()
# ax = fg.gca()
#
# h = ax.imshow(frame)
# for i in range(20):
#     ret, frame = cap.read()
#     h.set_array(frame)
#     draw()
#     pause(1e-1)


# for i in range(10):
#     ret, frame = cap.read()
#     cv2.imshow('img', frame)
#     cv2.waitKey(0)
# cv2.destroyAllWindows()


plt.ion()
#
# im = plt.imshow(frame)
#
for i in range(100):
    ret, frame = cap.read()
    plt.imshow(frame)
    plt.pause(0.01)
#
plt.ioff()
plt.show()
