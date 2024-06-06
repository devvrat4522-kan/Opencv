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

#1. method := Averaging method  (more blur (Average sum))

avg = cv.blur(img,(5,5))
cv.imshow('avg',avg)

# 2. method := Gaussian Blur Method (more natural less blur (Average product))

gauss = cv.GaussianBlur(img,(5,5),0)
cv.imshow('gauss',gauss)

# 3. method := Median blurring method

med = cv.medianBlur(img,5)
cv.imshow('median',med)

# 4. Bilateral Blurring


bilter = cv.bilateralFilter(img,40,45,45)
cv.imshow('bilateral',bilter)

cv.waitKey(0)