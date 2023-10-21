import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('face1.jpg', 0)
img_copy = cv.imread('face1.jpg')
gray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)
gray_invert = cv.bitwise_not(gray)
edges = cv.Canny(img, 100, 200)

contours, hierarchy = cv.findContours(gray_invert,  cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
print("Numar de conture: {}\n".format(len(contours)))
# img_copy = cv.imread("face1 (1).jpg.jpg")

cv.drawContours(img_copy, contours, -1, (0, 255, 0), 3)

cv.imshow('image', img_copy)
cv.waitKey(0)


