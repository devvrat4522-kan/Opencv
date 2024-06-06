import cv2 as cv
import matplotlib.pyplot as plt
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
b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('b',blue)
cv.imshow('r',red)
cv.imshow('g',green)

merge = cv.merge([b,g,r])
cv.imshow('merge',merge)
cv.waitKey(0)

