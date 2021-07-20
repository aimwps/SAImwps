import cv2
import numpy as np

# Load an image and show it on screen with cv2.imshow
def change_threshold_value(val):
    threshold_value = val
    _, thresh = cv2.threshold(img_use, threshold_value, 255, threshold_type)
    cv2.imshow(window_name, thresh)


img_path = 'img/janoski.jpg'
img_ori = cv2.imread(img_path)
img_use = img_ori.copy()
threshold_value =25
threshold_type = cv2.THRESH_BINARY
cam = cv2.VideoCapture(0)
window_name = "Callback Tester"
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

cv2.createTrackbar('Threshold Value', window_name, threshold_value, 255, change_threshold_value)

while True:
    cv2.imshow(window_name,img_use)
    key = cv2.waitKey(0) & 0xFF

    if key == 27:
        break
    elif key == ord('g') or key == ord('G'):
        img_use = cv2.cvtColor(img_ori.copy(), cv2.COLOR_BGR2GRAY)
    elif key == ord('c') or key == ord('C'):
        img_use = img_ori.copy()
    elif key == ord('t') or key == ord('T'):
        _, img_use = cv2.threshold(img_use, threshold_value, 255, threshold_type)
    elif key == ord('r') or key == ord('R'):
        img_use = img_ori.copy()
    else:
        print("Not understood- refreshing")
cv2.destroyAllWindows()
cam.release()
