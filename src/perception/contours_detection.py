#!/usr/bin/env python

import cv2


def read_image(image_name):
    image = cv2.imread(image_name)
    cv2.imshow("Original", image)
    return image


def colour_to_gray(rgb_image):
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", gray_image)
    return gray_image


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
    cv2.drawContours(image, contours, index, color, thickness)
    cv2.imshow(image_name, image)


if __name__ == '__main__':
    image_name = "images/fruit.jpeg"
    image = read_image(image_name)
    gray_image = colour_to_gray(image)
    bin_image = gray_to_binary(gray_image, True)
    contours = getContours(bin_image)
    draw_contours(image, contours, "RGB Contours")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
