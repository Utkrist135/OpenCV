import cv2 as cv

img= cv.imread('Images/face_0.jpg')

capture=cv.VideoCapture('Videos/Adele.mp4')
while True:
    isTrue, frame=capture.read()

    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('e'):
        break
capture.release()
cv.destroyAllWindows()