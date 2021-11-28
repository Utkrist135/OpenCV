import cv2 as cv
import numpy as np

img=cv.imread('Images/face_3.jpg')
blank=np.zeros(img.shape,dtype='uint8')
#cv.imshow('blank',blank)



gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray) 

canny=cv.Canny(img,145,175)
#cv.imshow('canny',canny)

blur=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('BLUR',blur)


ret, thresh= cv.threshold(gray,125,125,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank,contours, -1,(0,0,255),1)
cv.imshow('contoursdrawn',blank)


cv.waitKey(0)