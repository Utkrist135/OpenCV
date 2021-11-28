import cv2 as cv


img=cv.imread('Images/img1.jpeg')
cv.imshow('Image',img)
b,g,r=cv.split(img)

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merge=cv.merge([b,g,r])
cv.imshow('merged',merge)




cv.waitKey(0)