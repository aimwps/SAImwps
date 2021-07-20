import cv2
import numpy as np
import matplotlib.pyplot as plt

# OPEN CV TRACKING API'S
# BOOSTING - (based on ADABOOST)
# Multiple Instance Learning(MIL)
# Kernelized corelation filters (KCF)
# Tracking, Learning, Detection (TLD)
# MEDIANFLOW
# GOTURN (DL Based )
# MOSSE
# CSRT
#background_subtractor = cv2.createBackgroundSubtractorMOG2(history=5, varThreshold=5, detectShadows=True)
# History = number of frames to calculate it on

background_subtractor = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=10, detectShadows=True)
background_image = cv2.imread("/media/aimwps/F/PyCode/SAI/SAImwps/Datasets/Img/mountains.jpg")
bg_resized = cv2.resize(background_image, (640,480))
webcam = cv2.VideoCapture(0)

while webcam.isOpened():
    ret,  frame = webcam.read()
    if ret == False:
        print("No webcam read")
        break

    foreground_mask = background_subtractor.apply(frame)


    vid_in_object = cv2.bitwise_and(frame,frame, mask=foreground_mask)#<---- THIS ONE
    vid_in_object[foreground_mask ==0] = [0,0,0]
    masked_image = bg_resized.copy()
    masked_image[foreground_mask != 0] = [0, 0, 0]
    final_image = masked_image + vid_in_object
    cv2.imshow('cam', final_image)
    cv2.imshow('foreground_mask', foreground_mask)
    cv2.imshow('masked image', masked_image)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
webcam.release()


mil_tracker = cv2.TrackerMIL_create()
#selectROI()
