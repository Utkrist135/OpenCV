import cv2 as cv

img=cv.imread('Images/img1.jpeg',)
cv.imshow('Image',img)

#Average Blur
average=cv.blur(img,(3,3))
cv.imshow('Blur',average)

#Gaussian Blur
gauss=cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
med=cv.medianBlur(img,3)
cv.imshow('Median Blur',med)

#Bilateral Blurring
bilateral=cv.bilateralFilter(img, 10, 15, 15)
cv.imshow('bilateral',bilateral)



cv.waitKey(0)