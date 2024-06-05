
import cv2 as cv
import numpy as np


def scaller(frame,scale=0.50):
    # used for image, video and live
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimenstions = (width, height)
    return cv.resize(frame,dimenstions,interpolation=cv.INTER_AREA)

img = cv.imread('C:\\Users\\91983\\Desktop\\opencv\\pic1.jpg')
img = scaller(img)
cv.imshow('img',img)

blank = np.zeros(img.shape,dtype='uint8')
print('blank',blank)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)

cv.imshow('thresh',thresh)
# RETR_LIST return the list of all the contours edges and CHAIN_APPROX_SIMPLE is used for each point of bwteen starting and end points of a line.
contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cblank = cv.drawContours(blank,contours,-1,(255,255,0),1)
cv.imshow('C_blank',cblank)

cv.waitKey(0)
