import cv2
import numpy as np
#“options v4l2loopback devices=1 video_nr=13 card_label=’OBS Virtual Camera’ exclusive_caps=1”
cam = cv2.VideoCapture(0)
img_path = 'img/janoski.jpg'
img_ori = cv2.imread(img_path)
img_use = img_ori.copy()
threshold_value = 128
threshold_type = cv2.THRESH_BINARY

mask1 = {
        "hu":255,
        "hl":0,
        "su":180,
        "sl":0,
        "vu":255,
        "vl":0,}
SETTINGS = {"grayscale_on": True,
            "threshold_on": False,
            "mask1_on": False,
            "mask2_on": False,
            "mask3_on": False,
            "blur_on": False,
            "sharp_on": False,
            "line_detection_on": False,
}

def change_threshold_value(val):
    global threshold_value
    threshold_value = val

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

def change_blur(val):
    global blur_kernel_size
    blur_kernel_size =val

def change_sharpen(val):
    global sharpen_kernel_size
    sharpen_kernel_size =val


cv2.createTrackbar("'t' activates threshold: slide this to change value", window_name, threshold_value, 255, change_threshold_value)

cv2.createTrackbar("'1' activates mask 1: slide this to change Hue lower ", window_name, mask1['hl'], 255, change_mask1_hl)
cv2.createTrackbar("'1' activates mask 1: slide this to change Hue upper ", window_name, mask1['hu'], 255, change_mask1_hu)

cv2.createTrackbar("'1' activates mask 1: slide this to change Saturation lower ", window_name, mask1['sl'], 180, change_mask1_sl)
cv2.createTrackbar("'1' activates mask 1: slide this to change Saturation upper ", window_name, mask1['su'], 180, change_mask1_su)

cv2.createTrackbar("'1' activates mask 1: slide this to change Value lower ", window_name, mask1['vl'], 255, change_mask1_vl)
cv2.createTrackbar("'1' activates mask 1: slide this to change Value upper ", window_name, mask1['vu'], 255, change_mask1_vu)

cv2.createTrackbar("'b' activates blur: slide this to change kernel size ", window_name, blur_kernel_size, 21, change_blur)
cv2.createTrackbar("'s' activates sharpen: slide this to change kernel size ", window_name, sharpen_kernel_size, 9, change_sharpen)

def setting_executor(setting, cam_frame):
    new_frame = cam_frame.copy()
    if setting == "grayscale_on":
        grayscale = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2GRAY)
        stack_gray = np.stack((grayscale,)*3, axis=-1)
        return stack_gray

    if setting == "threshold_on":
        _, thresh = cv2.threshold(cam_frame, threshold_value, 255, threshold_type)
        #print(f"threshol value {threshold_value}")
        return thresh

    if setting == "blur_on":
        cam_frame = cv2.medianBlur(cam_frame,15)
        return cam_frame

    if setting == "sharp_on":
        kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        cam_frame = cv2.filter2D(cam_frame, -1, kernel)
        return cam_frame
    if setting == "line_detection_on":
        cam_frame = cv2.Canny(cam_frame, 100, 200)
        stack_lines = np.stack((cam_frame,)*3, axis=-1)
        return stack_lines

    if setting == "mask1_on":
        global mask1
        cam_hsv = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2HSV)
        lower_range = np.array([mask1['hl'], mask1['sl'], mask1['vl']])
        upper_range = np.array([mask1['hu'], mask1['su'], mask1['vu']])
        mask = cv2.inRange(cam_hsv, lower_range, upper_range)
        res = cv2.bitwise_and(cam_frame, cam_frame, mask=mask)
        return res


while True:
    cam_, cam_frame = cam.read()
    og = cam_frame.copy()
    if cam_:
        for setting, info in SETTINGS.items():
            if info == True:
                 cam_frame = setting_executor(setting, cam_frame)
        og_plus = np.concatenate((og, cam_frame), axis=1)
        #quick_plus = np.concatenate((np.stack((cv2.flip(og.copy(), 1),)*3, axis=-1), cv2.cvtColor(og.copy(),cv2.COLOR_BGR2GRAY)), axis=1)
        #print(quick_plus.shape)
        og_plus_plus = np.concatenate((og_plus))
        cv2.imshow(window_name, og_plus)
    else:
        print("not recieving video")

    key = cv2.waitKey(5) & 0xFF
    print(f"KEY::::::::::::::::::{key}")
    if key == 27:
        break
    elif key == ord('g') or key == ord('G'):
        SETTINGS['grayscale_on'] = np.abs(SETTINGS['grayscale_on']-1)
    elif key == ord('b') or key == ord('B'):
        SETTINGS['blur_on'] = np.abs(SETTINGS['blur_on']-1)
    elif key == ord('t') or key == ord('T'):
        SETTINGS['threshold_on'] = np.abs(SETTINGS['threshold_on']-1)
    elif key == ord('s') or key == ord('S'):
        SETTINGS['sharp_on'] = np.abs(SETTINGS['sharp_on']-1)
    elif key == ord('l') or key == ord('L'):
        SETTINGS['line_detection_on'] = np.abs(SETTINGS['line_detection_on']-1)
    elif key == ord('1'):
        SETTINGS['mask1_on'] = np.abs(SETTINGS['mask1_on']-1)
        print(SETTINGS)
    else:
        pass
cv2.destroyAllWindows()
cam.release()
