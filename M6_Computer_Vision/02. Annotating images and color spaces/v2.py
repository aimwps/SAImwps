import numpy as np
import cv2
import matplotlib as plt



vid = cv2.VideoCapture(0)

while(1):
    _, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0,50,50])
    upper_red1 = np.array([8,255,255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    lower_red2 = np.array([160,20,0])
    upper_red2 = np.array([180,255,255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    total_red = mask1 + mask2
    res = cv2.bitwise_and(frame,frame, mask= total_red)
    w = cv2.addWeighted(frame, 0.5, res, 1,0)

    cv2.imshow('frame',frame)
    cv2.imshow('mask1',mask1)
    cv2.imshow('mask2',mask2)
    cv2.imshow('total masks',total_red)
    #cv2.imshow('res',res)
    cv2.imshow("W", w)
    #cv2.imshow('test  res', test_res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
vid.release()
