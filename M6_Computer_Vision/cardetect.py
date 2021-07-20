import cv2
import numpy as np
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
#ffmpeg_extract_subclip("../Datasets/Video/4k2min.mp4", 30, 60, targetname="../Datasets/Video/cut.mp4")
cam = cv2.VideoCapture("../Datasets/Video/cut.mp4")
length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)

face_clf = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
eye_clf = cv2.CascadeClassifier( 'Haarcascades/haarcascade_eye.xml')
car_clf = cv2.CascadeClassifier( 'Haarcascades/haarcascade_car.xml')
window_name = "Callback Tester"
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
SETTINGS = {"grayscale_on": True,
            "eyes_on": False,
            "face_on": False,
            "cars_on":True}



######################################
# FOR EXECUTING SETTINGS
def setting_executor(setting, cam_frame):
    #new_frame = cam_frame.copy()
    if setting == "grayscale_on":
        grayscale = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2GRAY)
        stack_gray = np.stack((grayscale,)*3, axis=-1)
        return stack_gray
    if setting == "face_on":
        faces = face_clf.detectMultiScale(cam_frame, 1.5, 5, minSize=(100, 100))
        for (x,y,w,h) in faces:
            face_img = cam_frame[y:y+h, x:x+w]
            face_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
            cv2.rectangle(cam_frame,(x,y),(x+w,y+h),(255,0,0),2)
            eyes = eye_clf.detectMultiScale(face_gray, 1.5, 10)
            if len(eyes) >= 1:
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(face_img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        return cam_frame
    if setting == "eyes_on":
        return cam_frame
    if setting == "cars_on":
        cam_gray = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2GRAY)
        cars = car_clf.detectMultiScale(cam_gray, 1.1, 2,minSize=(100, 100))
        if len(cars) > 0:
            for (x,y,w,h) in cars:
                ratio = w/float(h)
                #print(w,h)
                cv2.rectangle(cam_frame,(x,y),(x+w,y+h),(255,0,0),2)
                car_gray = cam_gray[y:y+h, x:x+w]
                car_lines = cv2.Canny(car_gray,100,200)
                contours, h = cv2.findContours(car_lines, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
                for i, contour in enumerate(contours):
                    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
                    M = cv2.moments(contour)
                    if M["m00"] != 0:
                        cX = int(M["m10"] / M["m00"])
                        cY = int(M["m01"] / M["m00"])
                                #x, y , w, h = cv2.boundingRect(approx)

                    if len(approx) ==4:
                        if ratio >= 0.9 and ratio <1.1:
                            cv2.drawContours(cam_frame, contours, i, (255,255,0))

        return cam_frame




######################################
# CAMERA READ LOOP

while cam.isOpened():
    cam_, cam_frame = cam.read()
    #print(cam_frame.shape)
    cam_frame = cv2.resize(cam_frame,(int(cam_frame.shape[1]*0.4), int(cam_frame.shape[0]*0.4)), interpolation=cv2.INTER_AREA)
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

    elif key == ord('f') or key == ord('F'):
        SETTINGS['face_on'] = np.abs(SETTINGS['face_on']-1)

    elif key == ord('e') or key == ord('E'):
        SETTINGS['eyes_on'] = np.abs(SETTINGS['eyes_on']-1)
    elif key == ord('c') or key == ord('C'):
        SETTINGS['cars_on'] = np.abs(SETTINGS['cars_on']-1)
    else:
        pass
cv2.destroyAllWindows()
cam.release()
