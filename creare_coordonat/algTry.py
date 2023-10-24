import cv2 as cv
import numpy as np

img_copy = cv.imread('face1.jpg')
gray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)

# cleaning img
ret, threshold = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print(threshold)
kernel = np.ones((5, 5), np.uint8)
opening = cv.morphologyEx(gray, cv.MORPH_CLOSE, kernel)

contours, hierarchy = cv.findContours(gray,  cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img_copy, contours, -1, (0, 255, 0), 3)

cv.imshow('image', img_copy)
cv.waitKey(0)

# img = cv.imread('face1.jpg', cv.IMREAD_GRAYSCALE)
# img_copy = cv.imread('face1.jpg')
# # gray = cv.cvtColor(img_copy, cv.COLOR_BGR2GRAY)
# # gray_invert = cv.bitwise_not(gray)
# # edges = cv.Canny(img, 100, 200)
#
# # cleaning img
# ret, threshold = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# print(threshold)
# kernel = np.ones((5, 5), np.uint8)
# opening = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
#
# # # img_copy = cv.imread("face1 (1).jpg.jpg")
#
# contours, hierarchy = cv.findContours(img,  cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
# # print("Numar de conture: {}\n".format(len(contours)))
#
# cv.drawContours(img, contours, -1, (0, 255, 0), 3)
#
# cv.imshow('image', img + threshold)
# cv.waitKey(0)
#
#
