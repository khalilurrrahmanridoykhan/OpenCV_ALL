import cv2 as cv
import numpy as np
# .\myvenv\scripts\activate

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Cats', blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Greay',gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh Image', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0,0,255), 2)
cv.imshow('Contous Draw', blank)

cv.waitKey(0)
