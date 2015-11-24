#!/usr/bin/python
__author__ = 'mandeep'
import cv2
import numpy as np
#from PyQt4 import QtGui
fname='sample/1.jpg'
img = cv2.imread(fname)
rimg =cv2.imread(fname)
'''
ORANGE_MIN = np.array([5, 50, 50],np.uint8)
ORANGE_MAX = np.array([15, 255, 255],np.uint8)

hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

frame_threshed = cv2.inRange(hsv_img, ORANGE_MIN, ORANGE_MAX)
cv2.imwrite('output2.jpg', frame_threshed)
'''
def nothing(x):
    pass

cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('hl','image',0,255,nothing)
cv2.createTrackbar('sl','image',0,255,nothing)
cv2.createTrackbar('vl','image',0,255,nothing)
cv2.createTrackbar('hu','image',0,255,nothing)
cv2.createTrackbar('su','image',0,255,nothing)
cv2.createTrackbar('vu','image',0,255,nothing)

while(1):
    cv2.imshow('image',rimg)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    hcl = cv2.getTrackbarPos('hl','image')
    scl = cv2.getTrackbarPos('sl','image')
    vcl = cv2.getTrackbarPos('vl','image')
    hcu = cv2.getTrackbarPos('hu','image')
    scu = cv2.getTrackbarPos('su','image')
    vcu = cv2.getTrackbarPos('vu','image')
    I_MIN = np.array([hcl, scl, vcl],np.uint8)
    I_MAX = np.array([hcu, scu, vcu],np.uint8)
    hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    rimg=cv2.inRange(hsv_img, I_MIN, I_MAX)

cv2.destroyAllWindows()
