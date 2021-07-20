import cv2
import numpy as np
import matplotlib.pyplot as plt
index = 0
arr = []
while True:
    cap = cv2.VideoCapture(index)
    if not cap.read()[0]:
        continue
    else:
        arr.append(index)
        print(arr)
        x = input("jij")
    cap.release()
    index += 1
print(arr)
# applies a threshold to an image - changes pixels into the typce desired. e.g. binary pixels above 128 are white below are black

# create named window,
# def change_threshold_value(val):
#     threshold_value = val
#     ret, thresh = cv2.threshold(gray_img, threshold_value, 255, threshold_type)
#     cv2.imshow(window_name, thresh)
#
# # cv2.createTrackBar(trackbar name, # be displayed on the trackbar
# #                     windowName, #Trackbar must go in a window
# #                     value,#integer on the trackbar
# #                     count,#max position of the trackbar
# #                     onChange# function that happens when trackbar is changed)
# # cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
# # source image, )
# # cv2.Canny()### FINDS EDGES
# # cv2.waitKey(0)#integer of how many milliseconds to delay. 0 means wait forever, returns the ascii value
# # #user ord('key') to get the key.
# # window_name ='threshold'
#
# window_name ='threshold'
# threshold_value = 128
# threshold_type = cv2.THRESH_BINARY
# threshold_types  = [cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV]
#
# img_path = 'img/4.png'
# img_ori = cv2.imread(img_path)
# gray_img = cv2.cvtColor(img_ori.copy(), cv2.COLOR_BGR2GRAY)
#
# cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
#
# cv2.createTrackbar('Threshold Value', window_name, threshold_value, 255, change_threshold_value)
# cv2.imshow(window_name, gray_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.waitKey(1)
