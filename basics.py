import cv2 as cv

img=cv.imread('Images/face_0.jpg',)
#cv.imshow('Image',img)

#converting to greyscale
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Greyscaled',gray)

#Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('BLUR',blur)

#Edge Cascade
canny= cv.Canny(img,125,175)
#cv.imshow('Edges',canny)

#Dilating the image
dilate=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('dilated',dilate)

#Eroding
erode=cv.erode(dilate,(3,3),iterations=1)
cv.imshow('eroded',erode)
cv.waitKey(0) 




