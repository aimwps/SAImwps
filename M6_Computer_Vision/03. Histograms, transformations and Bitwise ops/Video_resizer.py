import cv2
import numpy as np


player = cv2.VideoCapture("vid/bg1.mp4")
writer = cv2.VideoWriter('bg1_480x640.mp4', )
fourcc = cv2.VideoWriter_fourcc('M',)

while True:
    ret, frame = player.read()
    if ret == True:
        b = cv2.resize(frame,(480,640),fx=0,fy=0, interpolation = cv2.INTER_CUBIC)
        writer.write(b)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()



o
