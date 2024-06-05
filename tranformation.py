import cv2 as cv
import numpy as np

img = cv.imread('C:\\Users\\91983\\Desktop\\opencv\\pic1.jpg')
cv.imshow('img',img)

# Translation

def transform(img,x,y):
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimansions = (img.shape[1],img.shape[0])

    return cv.warpAffine(img,transmat,dimansions)

# -x -> left
# -y -> up
# x  -> right
#  y -> down

translated = transform(img,100,-100)
cv.imshow('transformed',translated)


# Rotation

def rotation(img,angle,rotpoint=None):
    (height,width) = img.shape[:2]
    if rotpoint is None:
        rotpoint =(width//2,height//2)
    
    rotmat = cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotmat,dimensions)

# +angle for anticlockwise and -ive for clockwise

rot_img = rotation(img,30)
cv.imshow('rot_img',rot_img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow('canny',canny)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)

cv.imshow('thresh',thresh)
# RETR_LIST return the list of all the contours edges and CHAIN_APPROX_SIMPLE is used for each point of bwteen starting and end points of a line.
contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

cv.waitKey(0)


