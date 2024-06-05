import cv2 as cv


def scaller(frame,scale=0.75):
    # used for image, video and live
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimenstions = (width, height)
    return cv.resize(frame,dimenstions,interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # used only for live videos
    capture.set(3,width)
    capture.set(2,height)

capture = cv.VideoCapture('C:\\Users\\91983\\Desktop\\opencv\\vid1.mp4')

img = cv.imread('C:\\Users\\91983\\Desktop\\opencv\\pic1.jpg')
resized_img = scaller(img,0.2) 
cv.imshow('Image',resized_img)
cv.waitKey(0)

