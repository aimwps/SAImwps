
import cv2
import numpy as np
import matplotlib.pyplot as plt
def ip(img_print):
    if len(img_print.shape) == 2:
        plt.figure(figsize=(15,10))
        plt.imshow(img_print, cmap='gray')
    else:
        plt.figure(figsize=(15,10))
        plt.imshow(img_print[:,:,::-1])
    print(img_print.shape)

def hsvp(img_print):
    x =cv2.cvtColor(img_print, cv2.COLOR_2RGB)
    plt.figure(figsize=(15,10))
    plt.imshow(x)


ret, template_th = cv2.threshold(star_template, 127,255,cv2.THRESH_BINARY_INV)
img_th = cv2.threshold(star_gray, 127,255,cv2.THRESH_BINARY_INV)

template_contours, h = cv2.findContours(template_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) ## try CHAIN_APPROX_SIMPLE
image_contours, img_g = cv2.findContours(image_th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.matchShapes()
