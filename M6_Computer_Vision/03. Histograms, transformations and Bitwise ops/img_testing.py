import numpy as np
import cv2
import matplotlib.pyplot as plt
def ip(img_print):
    if len(img_print.shape) == 2:
        plt.figure(figsize=(15,10))
        plt.imshow(img_print, cmap='gray')
        plt.show()
    else:
        plt.figure(figsize=(15,10))
        plt.imshow(img_print[:,:,::-1])
        plt.show()
    print(img_print.shape)

def hsvp(img_print):
    x =cv2.cvtColor(img_print, cv2.COLOR_HSV2RGB)
    plt.figure(figsize=(15,10))
    plt.imshow(x)


img_path = 'img/research/frame_200.jpg'
img_ori = cv2.imread(img_path)
#img_hsv = cv2.cvtColor(img_ori.copy(), cvt.COLOR_BGR2HSV)
img_edit = img_ori.copy()
img_crop = img_edit[300:400, 575:615,:]
img_crop_hsv = cv2.cvtColor(img_crop.copy(), cv2.COLOR_BGR2HSV)
H,S,V = cv2.split(img_crop_hsv)
for row in H:
    print(row)


cv2.rectangle(img_edit, (575,300), (615,400), (255,255,255), 2)

ip(img_edit)
ip(img_crop)
