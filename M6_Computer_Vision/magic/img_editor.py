import numpy as np
import matplotlib.pyplot as plt
import cv2
cam = cv2.VideoCapture(0)
img = cv2.imread('img/gesture_right_hand.jpg')
img_crop = img[174:350,230:360,:]
window_name = "Magic!"
SETTINGS = {"hand_extract": False,
            "threshold_on": False,
            "mask1_on": False,
            "mask2_on": False,
            "mask3_on": False,
            "blur_on": False,
            "sharp_on": False,
            "line_detection_on": False,
}
mask1 = {
        "hl":0,
        "hu":66,
        "sl":0,
        "su":117,
        "vl":33,
        "vu":91,}
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
def change_mask1_hl(val):
    mask1['hl'] = val
def change_mask1_hu(val):
    mask1['hu'] = val
def change_mask1_sl(val):
    mask1['sl'] = val
def change_mask1_su(val):
    mask1['su'] = val
def change_mask1_vl(val):
    mask1['vl'] = val
def change_mask1_vu(val):
    mask1['vu'] = val
cv2.createTrackbar("'1' activates mask 1: slide this to change Hue lower ", window_name, mask1['hl'], 255, change_mask1_hl)
cv2.createTrackbar("'1' activates mask 1: slide this to change Hue upper ", window_name, mask1['hu'], 255, change_mask1_hu)

cv2.createTrackbar("'1' activates mask 1: slide this to change Saturation lower ", window_name, mask1['sl'], 180, change_mask1_sl)
cv2.createTrackbar("'1' activates mask 1: slide this to change Saturation upper ", window_name, mask1['su'], 180, change_mask1_su)

cv2.createTrackbar("'1' activates mask 1: slide this to change Value lower ", window_name, mask1['vl'], 255, change_mask1_vl)
cv2.createTrackbar("'1' activates mask 1: slide this to change Value upper ", window_name, mask1['vu'], 255, change_mask1_vu)

def setting_executor(setting, cam_frame):
    if setting == "mask1_on":
        global mask1
        cam_hsv = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2HSV)
        lower_range = np.array([mask1['hl'], mask1['sl'], mask1['vl']])
        upper_range = np.array([mask1['hu'], mask1['su'], mask1['vu']])
        mask = cv2.inRange(cam_hsv, lower_range, upper_range)
        res = cv2.bitwise_and(cam_frame, cam_frame, mask=mask)
        res = cv2.medianBlur(res,9)
        #final_image = cv2.cvtColor(final_image, cv2.COLOR_HSV2BGR)
        #res[mask ==0] = [0,0,0]
        # masked_image = cam_frame.copy()
        # masked_image[mask!= 0] = [0, 0, 0]
        # final_image = masked_image + res
        # )

        return res



while True:
    final = img_crop.copy()
    #cv2.imshow(window_name, final)
    key = cv2.waitKey(5) & 0xFF

    for setting, info in SETTINGS.items():
        if info == True:
             final = setting_executor(setting, final)
    cv2.imshow(window_name, final)

        #og_plus = np.concatenate((og, cam_frame), axis=1)
    if key == 27:
        break
    elif key == ord('1'):
        SETTINGS['mask1_on'] = np.abs(SETTINGS['mask1_on']-1)
        print(SETTINGS['mask1_on'] )
    elif key == ord('2'):
        SETTINGS['hand_extract'] = np.abs(SETTINGS['hand_extract']-1)
    else:
        pass


# while True:
#     cam_, cam_frame = cam.read()
#     if cam_:
#         og = cam_frame.copy()
#         for setting, info in SETTINGS.items():
#             if info == True:
#                  cam_frame = setting_executor(setting, cam_frame)
#         og_plus = np.concatenate((og, cam_frame), axis=1)
#         cv2.imshow(window_name, og_plus)
#     else:
#         print("not recieving video")
#
#     key = cv2.waitKey(5) & 0xFF
#     if key == 27:
#         break
#     elif key == ord('e') or key == ord('E'):
#         pass
#     else:
#         pass
cv2.destroyAllWindows()
cam.release()
