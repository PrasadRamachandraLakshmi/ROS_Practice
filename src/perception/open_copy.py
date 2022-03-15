#!/usr/bin/env/python

import numpy as np
import cv2


image_name = "rgb"

img = cv2.imread("images/"+image_name+".jpeg")
cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Image", img)
print(img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray_img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#cv2.namedWindow("Image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Image1", img)
cv2.imshow("Gray Image", gray_img)
red, green, blue = cv2.split(img)
cv2.imshow("Blue", blue)
cv2.imshow("Red", red)
cv2.imshow("Green", green)

cv2.waitKey(0)

# cv2.imwrite("images/copy/"+image_name+"_copy.jpeg", img)
