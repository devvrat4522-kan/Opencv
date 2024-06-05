import cv2 as cv

# img = cv.imread('C:\\Users\\91983\\Desktop\\opencv\\pic1.jpg')
# cv.imshow('Image',img)
# cv.waitKey(0)

capture = cv.VideoCapture('C:\\Users\\91983\\Desktop\\opencv\\vid1.mp4') # integer parameter that represent the web cam
f=0
while f==0:
    isTrue, frame = capture.read()
    if not isTrue:
        print("end")
        break
    cv.imshow('Video',frame)
    if 0xFF==ord('f') or cv.waitKey(30):
        f=1
        break

capture.release()
cv.destroyAllWindows()