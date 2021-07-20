import cv2
import numpy as np



# Source image, 'contourn retrieval mode' [RETR_LIST, RETR_EXTERNAL, RETR_CCOMP, RETR_TREE]
# Used for finding 'contours' (lines with intense changes in pixel colour)
cv2.findContours()
# Outputs modified image, contours and hierachy

# Used for drawing contours on an image that it detects
# Source image, the found contours (returned from find contours), index of contours to draw, ...
cv2.drawContours()

## Sorting contours
## can be sorted by orientation, Area ; can help with noisy images where additonal contours are detected.
### Many others available and custom libraries to handle how to sort contours

## Moments
### Centre of mass, area of an object.

# Cx = M10  & Cy = M01
#      M00         M00
# This will find the centre of the contour

cv2.contourArea() # Takes a contour as parameter,
# using moments 'M[m00]'

## Finds the perimeter of a contopur.
cv2.arcLength()# Takes a contour as parameter, and if shape is closed.


# Approximates contour shape to another shape with less vertices (dependent on precision applied)
cv2.approxPolyDp()# Contour, epsilon,

#Epsilon Value (small values give precise, large give generic)
# Rule of thumb < 5% of contour perimeter
# by running len() on the approximation it will return the amount of vertices.

################
### See others
# Convex Hull - the smallest shape that fits the entire boundary tightly
# Bounding rectangle - (will not consider rotation)
# cv2.boundingRect(contours) # returns x,y,w,h (starting point, width / height)
# cv2.minEnclosingCircle() # creates a circle around the contour
# cv2.fitEllipse(contours) # fits the minimum ellipse around the object
# cv2.matchShapes(), compares 2 shapes or contours (lower result=better match)
# cv.HoughLines() # Used to detect straight lines.
# cv2.HoughLinesP() #
# cv2.HoughCircles() #
# cv2.SimpleBlockDetector_create() # #a big bunch of pixels that are conntected to each other a blob :D
def sort_contours(cnts, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y-coordinate rather than
    # the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to
    # bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
                                        key=lambda b: b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)



### go to server
# 1. connect to vpn
#    sudo humachi join 'id'453-578-886'
#    with gui enter same code as network id
# 2. connect account
#    ssh {username}@ip.address
# 3. clone repo
#    git clone sshkey@github
# 4. run files
#    python3 mega_singularity.py
