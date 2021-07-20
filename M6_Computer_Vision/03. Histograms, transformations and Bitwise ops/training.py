import numpy as np
import cv2
import matplotlib.pyplot as plt

while True:
    img_ori = cv2.imread('img/day4.jpg')
    cv2.imshow("original",img_ori)

    # hist_blue = cv2.calcHist([img_ori],[0],None, [255],[0,255])
    # plt.plot(hist_blue,color='g')
    #
    # colors = ['b','g','r']
    # for i, color in enumerate(colors):
    #     histogram= cv2.calcHist([img_ori],[i],None, [255],[0,255])
    #     plt.plot(histogram, color=color)
    #     plt.xlim(0,256)
    # plt.show()
    ####################################################################
    ### Translation_matrix
    # Moves the image in different direcions
    translation_matrix = np.float32([
                [1,0,50],
                [0,1,100]
    ])
    moved_img = cv2.warpAffine(img_ori.copy(), translation_matrix)
    # ^^^ the above moves it down and right, doing negative for 50/100 will move it up and left
    ####################################################################
    ### Rotation_matrix
    rotation_matrix = cv2.getRotationMatrix2D((0,0), 45, 1)
    rotated_img = cv2.warpAffine(img_ori.copy(),)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
