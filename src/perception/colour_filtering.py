#!/usr/bin/env python
import cv2


image_name = "images/balls.jpeg"

image = cv2.imread(image_name, cv2.IMREAD_COLOR)
cv2.imshow("Original", image)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv", image_hsv)
h, s, v = cv2.split(image_hsv)

# find the upper and Lower bounds of the yellow colour(tennis ball)
# (60/2 because hue is from 0-180 while 60 is when 0-360)
yellow_lower = (30, 100, 60)
yellow_upper = (60, 255, 255)  # (120/2)


# define a mask using lower and upper bounds
mask = cv2.inRange(image_hsv, yellow_lower, yellow_upper)
cv2.imshow("Mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
