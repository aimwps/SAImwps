import numpy as np
import matplotlib.pyplot as plt
import cv2
cam = cv2.VideoCapture(0)
window_name = "Magic!"
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
SETTINGS = {"hands_on": False,
            "left_on": False,
            "right_on": False}
img_lh = cv2.imread('img/lh2.jpg')
img_rh = cv2.imread('img/rh2.jpg')
lh_gray = cv2.cvtColor(img_lh, cv2.COLOR_BGR2GRAY)
rh_gray = cv2.cvtColor(img_rh, cv2.COLOR_BGR2GRAY)
lh_w, lh_h = lh_gray.shape[::-1]
rh_w, rh_h = rh_gray.shape[::-1]

cv2.imshow('lh gray', lh_gray)

cv2.imshow('rh gray', rh_gray)
method = eval('cv2.TM_CCOEFF_NORMED')
#'cv2.TM_CCOEFF_NORMED' - Pretty good

def setting_executor(setting, cam_frame):
    cam_frame_gray = cv2.cvtColor(cam_frame.copy(), cv2.COLOR_BGR2GRAY)
    if setting == "hands_on":
        match_lh = cv2.matchTemplate(cam_frame_gray, lh_gray, method)
        lh_min_val, lh_max_val, lh_min_loc, lh_max_loc = cv2.minMaxLoc(match_lh)
        lh_top_left = lh_max_loc
        lh_bottom_right = (lh_top_left[0]+lh_w, lh_top_left[1]+lh_h)

        match_rh = cv2.matchTemplate(cam_frame_gray, rh_gray, method)
        rh_min_val, rh_max_val, rh_min_loc, rh_max_loc = cv2.minMaxLoc(match_rh)
        rh_top_left = rh_max_loc
        rh_bottom_right = (rh_top_left[0]+rh_w, rh_top_left[1]+rh_h)

        cv2.rectangle(cam_frame, lh_top_left, lh_bottom_right, (255,255,0), 5)
        cv2.rectangle(cam_frame, rh_top_left, rh_bottom_right, (255,255,0), 5)
        return cam_frame



while True:
    cam_, cam_frame = cam.read()
    if cam_:
        og = cam_frame.copy()
        for setting, info in SETTINGS.items():
            if info == True:
                 cam_frame = setting_executor(setting, cam_frame)
        og_plus = np.concatenate((og, cam_frame), axis=1)
        cv2.imshow(window_name, og_plus)
    else:
        print("not recieving video")

    key = cv2.waitKey(5) & 0xFF
    if key == 27:
        break

    elif key == ord('g') or key == ord('G'):
        SETTINGS['grayscale_on'] = np.abs(SETTINGS['grayscale_on']-1)

    elif key == ord('h') or key == ord('H'):
        SETTINGS['hands_on'] = np.abs(SETTINGS['hands_on']-1)

    elif key == ord('e') or key == ord('E'):
        cv2.imwrite('img/left_hand.jpg', og)
    else:
        pass
cv2.destroyAllWindows()
cam.release()
