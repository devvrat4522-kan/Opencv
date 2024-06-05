import cv2 as cv

def scaller(frame,scale=0.75):
    # used for image, video and live
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimenstions = (width, height)
    return cv.resize(frame,dimenstions,interpolation=cv.INTER_AREA)


img = cv.imread('C:\\Users\\91983\\Desktop\\opencv\\pic1.jpg')
resized_img = scaller(img,0.5) 
cv.imshow('img',resized_img)

# BGR -> Gray image
gray = cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# Blur Image
blur = cv.GaussianBlur(resized_img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

# Edge Cascade
canny = cv.Canny(resized_img,125,175)
cv.imshow('canny',canny)

# Dialating the image
dilated = cv.dilate(canny,(1,1),iterations=1)
cv.imshow('dilated',dilated)

# cropping
cropped = resized_img[50:200,200:400]
cv.imshow('cropped',cropped)

cv.waitKey(0)