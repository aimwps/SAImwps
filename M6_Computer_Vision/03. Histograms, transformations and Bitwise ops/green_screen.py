import numpy as np
import cv2
import matplotlib as plt
window_name= 'Multi window viewer'
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
vid = cv2.VideoCapture(0)
screen = cv2.VideoCapture("/media/aimwps/F/PyCode/SAI/SAImwps/Datasets/Video/cut.mp4")
counter = 0
while(1):

    ret1, cam_frame = vid.read()
    ret2, vid_frame = screen.read()
    vid_frame = cv2.resize(vid_frame, (640,480))
    if ret1==False:
        print("could not read from webcam !")
        continue
    if ret2==False:
        print("could not read from screen !")
        continue
    hsv = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2HSV)
############################################################################
#### FOR TAKING SNAP SHOTS EVERY 100 FRAMES
    # if counter%100 == 0:
    #     cv2.imwrite(f'img/research/frame_{counter}.jpg', cam_frame)


################################################################################
#### MASK FOR LOW END RED SPECTRUM
    # lower_red1 = np.array([0,100,0])
    # upper_red1 = np.array([10,255,77])
    # mask1 = cv2.inRange(hsv, lower_red1, upper_red1)

################################################################################
#### MASK FOR LOW HIGH RED SPECTRUM
    lower_red2 = np.array([110,70,77])
    upper_red2 = np.array([180,230,255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask2 = cv2.medianBlur(mask2,15)

    #print(type(mask2))
    # total_red = mask1 + mask2

################################################################################
#### FOR DISPLAYING JUST THE CAPTURED OBJECT
    res = cv2.bitwise_and(cam_frame,cam_frame, mask=mask2)

################################################################################
#### FOR BLURRING
    # res_with_bg = cv2.addWeighted(cam_frame, 0.5, res, 1,0)
    # kernel = np.ones((15,15), np.float32)/225
    # smoothed = cv2.filter2D(res, -1, kernel)
    # blur = cv2.GaussianBlur(res, (15,15),0)
    #med_blur = cv2.medianBlur(res,15)


################################################################################
#### FOR ADDING IMAGE TO OBJECT AREA **(480,640,3)


    vid_in_object = cv2.bitwise_and(vid_frame,vid_frame, mask=mask2)#<---- THIS ONE
    #med_blur_vid = cv2.medianBlur(vid_in_object, 15)
    vid_in_object[mask2 ==0] = [0,0,0]

    masked_image = cam_frame.copy()
    masked_image[mask2 != 0] = [0, 0, 0]

    final_image = masked_image + vid_in_object
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print(masked_image.shape)
    print(vid_in_object.shape)








################################################################################
#### FOR SHOWING VIDEOS
    # cv2.imshow('cam_frame',cam_frame)
    # cv2.imshow('Video Frame',vid_frame)
    # cv2.imshow('Vid in mask',vid_in_object)
    # cv2.imshow('Blurred vid in mask ',med_blur_vid)
    #final = cv2.vconcat([mask2, final_image])
    #cv2.imshow('mask1',mask1)
    #cv2.imshow(window_name,final)
    cv2.imshow(window_name,final_image)
    #cv2.imshow('total masks',total_red)
    #cv2.imshow('res',res)
    #cv2.imshow("With background 0.5 alpha", w)
    #cv2.imshow("Smoothed", smoothed)
    #cv2.imshow('blur',blur)
    #cv2.imshow('med blur',med_blur)
    #cv2.imshow('test  res', test_res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    counter += 1

cv2.destroyAllWindows()
vid.release()
