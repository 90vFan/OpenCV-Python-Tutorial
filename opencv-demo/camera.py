import numpy as np
import cv2
import sys

output = None
if len(sys.argv) > 1:
    output = sys.argv[1]


cap = cv2.VideoCapture(0)


# scale video
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 4
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)    # 3


# width = 640
# ret = cap.set(3, width)
# height = 480
# ret = cap.set(4, height)


height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(f'Frame width: {width}, Frame height: {height}')


if output:
    # 编码模式　DIVX, XVID, MJPG, X264, WMV1, WMV2, ...
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output, fourcc, 20.0, (int(width), int(height)))


while cap.isOpened():
    # capture frame-by-frame
    ret, frame = cap.read()

    if ret is True:
        frame = cv2.flip(frame, flipCode=1)
        # flipCode：翻转方向：1：水平翻转；0：垂直翻转；-1：水平垂直翻转

        cv2.imshow('Camera', frame)
        # cv2.setWindowTitle('frame', 'COLOR_BGR2GRAY')

        if output:
            out.write(frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

if output:
    out.release()
