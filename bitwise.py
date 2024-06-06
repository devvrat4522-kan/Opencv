import cv2 as cv
import numpy as np

blank = np.zeros([400,400],dtype='uint8')
cv.imshow('blank',blank)

rect = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('rect',rect)
cv.imshow('circle',circle)

band = cv.bitwise_and(rect,circle)
cv.imshow('band',band)

bor = cv.bitwise_or(rect,circle)
cv.imshow('bor',bor)

bxor = cv.bitwise_xor(rect,circle)
cv.imshow('xbor',bxor)

cv.waitKey(0)