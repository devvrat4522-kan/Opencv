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

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)
# 
# rect = cv.rectangle(blank,(img.shape[0]//2,img.shape[1]//2),(0,50),355,-1)
circ = cv.circle(blank,(img.shape[0]//4,img.shape[1]//4),100,255,-1)
# cv.imshow('rect',rect)

# masked = cv.bitwise_and(img,img,mask=rect)
masked1 = cv.bitwise_and(img,img,mask=circ)
# cv.imshow('masked', masked)
cv.imshow('masked', masked1)
cv.waitKey(0)