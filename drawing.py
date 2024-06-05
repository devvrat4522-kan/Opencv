import cv2 as cv
import numpy as np


#blank image
blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

# blank[100:200,200:400] = 0,255,0
# cv.imshow('green',blank)


# rectangle drawe
# ict = cv.rectangle(blank,(100,100),(250,250),(0,255,0),thickness=5)
# cv.imshow('recblank',ict)


# thickness=-1 or cv.FILLED for fully filling 
# circle = cv.circle(blank,(255,255),40,(0,0,255),thickness=-1)
# cv.imshow('circle',circle)

# Writing a text
txt = cv.putText(blank,'Hello! World',(150,250),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow("text",txt)

cv.waitKey(0)