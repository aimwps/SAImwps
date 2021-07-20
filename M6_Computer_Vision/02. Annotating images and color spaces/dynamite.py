import numpy as np
import cv2
import matplotlib as plt
# img = cv2.imread('img/m.jpg')
# img_hsv = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2HSV)
# H, S, V = cv2.split(img_hsv)
# lower_blue = np.array([30,150,50])
# upper_blue = np.array([255,255,180])
#
# mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
# res = cv2.bitwise_and(img,img, mask= mask)
#
# cv2.imshow('frame',img)
# cv2.imshow('mask',mask)
# cv2.imshow('res',res)
#
# k =cv2.waitKey
#
# cv2.destroyAllWindows()
while(1):
    # _, frame = cap.read()
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #dtype="uint8"
    img = cv2.imread('img/m.jpg')
    img_hsv = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2HSV)
    H, S, V = cv2.split(img_hsv)

    lower_blue = np.array([90,40,20])
    upper_blue = np.array([140,255,255])
    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
    res_blue = cv2.bitwise_and(img,img, mask=mask_blue)
    cv2.imshow('frame',img)
    #cv2.imshow('mask',mask)
    cv2.imshow('Blue res',res_blue)

############################################
    lower_green = np.array([40,10,100])
    upper_green = np.array([70,255,255])
    mask_green = cv2.inRange(img_hsv, lower_green, upper_green)
    res_green = cv2.bitwise_and(img,img, mask= mask_green)
    #cv2.imshow('frame',img)
    #cv2.imshow('mask',mask)
    cv2.imshow('Green res',res_green)
############################################
    lower_red = np.array([0,10,100])
    upper_red = np.array([15,255,255])
    mask_red = cv2.inRange(img_hsv, lower_red, upper_red)
    res_red = cv2.bitwise_and(img,img, mask= mask_red)
    #cv2.imshow('frame',img)
    #cv2.imshow('mask',mask)
    #cv2.imshow('Red res',res_red)
##############################################
    green_blue = cv2.bitwise_or(res_green, res_blue)
    cv2.imshow('green blue', green_blue)
    weighted = cv2.addWeighted(img, 0.5, green_blue, 1, 0)
    # w2 = cv2.addWeighted(weighted, 0)
    cv2.imshow('weighted', weighted)




    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
