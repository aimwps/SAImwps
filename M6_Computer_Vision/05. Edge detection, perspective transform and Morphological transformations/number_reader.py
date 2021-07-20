import cv2
import numpy as np
import datetime as dt
import time
import os
selecting_images = True
################################################################################
### PROJECT HELPERS
def image_scaler(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

def mnist_creator(img):
    imgGs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adaptive_mean_c = cv2.adaptiveThreshold(imgGs,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 10)
    kernel = np.ones((3,3),np.uint8)
    dilate = cv2.dilate(adaptive_mean_c, kernel, iterations=1)
    img28 = cv2.resize(dilate, (28,28), interpolation=cv2.INTER_AREA)
    #_, imgInv = cv2.threshold(imgGs,128, 255, cv2.THRESH_BINARY_INV)
    return img28# img28#adaptive_mean_c #imgInv


################################################################################
### BASE IMAGES & WINDOW
img_path = "img/full_page.jpg"
img_orig = cv2.imread(img_path)
img_base = image_scaler(img_orig.copy(),50)
window_name = "AIMwpS"
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

################################################################################
### MOUSE GLOBALS
x_start = 0
y_start = 0
x_end = 0
y_end = 0
cropping = False
def image_scaler(img, scale_percent):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

def image_cropper(event, x, y, flags, param):
    # MOUSE CO-ORDINATE GLOBALS
    global x_start, y_start, x_end, y_end, cropping
    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True
    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y
    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False # cropping is finished
        refPoint = [(x_start, y_start), (x_end, y_end)]
        if len(refPoint) == 2: #when two points were found
            roi = img_base[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)

            num = input("What number is it?")
            now_code = dt.datetime.now().strftime("%y%m%d%H%M%S")
            cv2.imwrite(f"img/numbers/{num}_{now_code}.jpg", roi)


################################################################################
### SET THE MOUSE CALLBACKS,
if selecting_images:
    cv2.setMouseCallback(window_name,image_cropper)

while True:
    if selecting_images:
        img_crop = img_base.copy()
        if not cropping:
            cv2.imshow(window_name, img_base)
        elif croping:
            cv2.rectangle(img_crop,(x_start, y_start), (x_end, y_end),(255,0,0), 2)
            cv2.imshow(window_name, img_crop)
        key = cv2.waitKey(0) & 0xFF
        if key == 27:
            break
    else:
        for file in os.listdir("img/numbers"):
            print(type(file))
            img = cv2.imread("img/numbers/"+file)
            mnist_img = mnist_creator(img)
            print(mnist_img.shape)
            cv2.imshow("MNIST NUMBER", mnist_img)
            key = cv2.waitKey(0) & 0xFF
            if key == 27:
                break
        key = cv2.waitKey(0) & 0xFF
        if key == 27:
            break
cv2.destroyAllWindows()
