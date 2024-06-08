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

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

threhold , thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('threhold',thresh)

threhold , thresh_inv = cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('threhold',thresh_inv)

ad_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,100)
cv.imshow('ad_thresh',ad_thresh)

cv.waitKey(0)