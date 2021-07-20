import cv2
import numpy as np
cam = cv2.VideoCapture(0)
face_clf = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
eye_clf = cv2.CascadeClassifier( 'Haarcascades/haarcascade_eye.xml')
window_name = "Callback Tester"
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
SETTINGS = {"grayscale_on": True,
            "eyes_on": False,
            "face_on": True,}



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
                    cv2.rectangle(face_img,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
            else:
                return cam_frame
        return cam_frame
    if setting == "eyes_on":
        return cam_frame

######################################
# CAMERA READ LOOP

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

    elif key == ord('f') or key == ord('F'):
        SETTINGS['face_on'] = np.abs(SETTINGS['face_on']-1)

    elif key == ord('e') or key == ord('E'):
        SETTINGS['eyes_on'] = np.abs(SETTINGS['eyes_on']-1)
    else:
        pass
cv2.destroyAllWindows()
cam.release()
