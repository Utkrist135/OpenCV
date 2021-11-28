import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype= 'uint8')

#cv.imshow('Blank',blank)

#painting a certain color
#blank[200:300, 300:400]=0,0,255
#cv.imshow('Green',blank)

#Drawing a rectangle
#cv.rectangle(blank,(0,0),(499,250),(0,255,0),thickness=-1)
#cv.imshow('Rectangle',blank)

#Drawing a circle
#cv.circle(blank,(250,250),250,(0,255,0),thickness=-1)
#cv.imshow('Circle',blank)

#Draw a line
cv.line(blank,(0,0),(250,150),(0,255,0),thickness=1)
cv.imshow('Line',blank)

#Inserting text
cv.putText(blank, 'Hello My name is ut',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('text',blank)



cv.waitKey(0)

