import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# Print the image with color
blank[200:300, 300:400] = 0,255,0
cv.imshow('Green', blank)

# Drow a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)
cv.imshow('Rectangle',blank)

# Drow a Circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2),200,(0,0,255),thickness=2)
cv.imshow('Circle',blank)

# Drow a line
cv.line(blank, (100,250), (300,400),color=(255,255,255), thickness=3)
cv.imshow('Line', blank)

# Write text
cv.putText(blank, 'Hello', (255,255),cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),2)
cv.imshow('Text', blank)


cv.waitKey(0)

