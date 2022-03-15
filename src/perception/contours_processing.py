#!/usr/bin/env python

import cv2
import numpy as np


def read_image(image_name):
    image = cv2.imread(image_name)
    cv2.imshow("Original", image)
    return image


def colour_to_gray(rgb_image):
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", gray_image)
    # if blur:
    #     gray_image = cv2.GaussianBlur(rgb_image, (5, 5), 0)
    return gray_image


def colour_filter(rgb_image):
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(rgb_image)
    mask1 = cv2.inRange(hsv_image, (0, 100, 15), (30, 255, 255))
    mask2 = cv2.inRange(hsv_image, (45, 100, 15), (60, 255, 255))
    mask = mask1+mask2
    cv2.imshow("Filetring", mask)
    return mask


def gray_to_binary(gray_image, adaptive):
    if adaptive:
        bin_image = cv2.adaptiveThreshold(
            gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 5.5)
    else:
        ret, bin_image = cv2.threshold(
            gray_image, 127, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Binary", bin_image)
    return bin_image


def getContours(binary_image):
    contours, heirarchy = cv2.findContours(
        binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def draw_contours(image, contours, image_name):
    index = -1  # all contours
    thickness = 1
    color = (255, 255, 255)
    #cv2.drawContours(image, contours, index, color, thickness)
    cv2.imshow(image_name, image)


def get_contour_center(contour):
    M = cv2.moments(contour)
    cx = -1
    cy = -1
    if(M['m00'] != 0):
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

    return cx, cy


def contours_processing(binary_image, rgb_image, contours):
    black_image = np.zeros([bin_image.shape[0], bin_image.shape[1], 3])

    for c in contours:
        area = cv2.contourArea(c)
        perimeter = cv2.arcLength(c, True)
        (x, y), radius = cv2.minEnclosingCircle(c)
        if area > 1500:
            #cv2.drawContours(rgb_image, [c], -1, (150, 250, 150), 1)
            cv2.drawContours(black_image, [c], -1, (150, 250, 150), 1)

            cx, cy = get_contour_center(c)

            cv2.circle(rgb_image, (cx, cy), (int)(radius), (0, 0, 255), 1)
            cv2.circle(black_image, (cx, cy), (int)(radius), (0, 0, 255), 1)
        print("Area {}, Perimeter {}".format(area, perimeter))

    print("number of Contours:{}".format(len(contours)))
    cv2.imshow("RGB Contours", rgb_image)
    #cv2.imshow("Black", black_image)


if __name__ == '__main__':
    image_name = "images/balls.jpeg"
    image = read_image(image_name)
    gray_image = colour_to_gray(image)
    bin_image = gray_to_binary(gray_image, True)
    bin_image1 = colour_filter(image)
    contours = getContours(bin_image1)
    draw_contours(image, contours, "RGB Contours")
    contours_processing(bin_image, image, contours)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
