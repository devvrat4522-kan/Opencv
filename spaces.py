import cv2 as cv
import matplotlib.pyplot as plt

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

lab = cv.cvtColor(img,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)

plt.imshow(img)
plt.show()

rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)


hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)
cv.waitKey(0)