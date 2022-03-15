#!/usr/bin/env python
import cv2


def read_image(image_name, as_gray):
    if as_gray:
        image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    else:
        image = cv2.imread(image_name, cv2.IMREAD_COLOR)
    cv2.imshow("Original", image)
    return image


def basic_threshold(image, threshold_value):
    ret, img = cv2.threshold(image, threshold_value,
                             255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Basic", img)


def adaptive_threshold(image, threshold_value):
    img = cv2.adaptiveThreshold(
        image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, threshold_value, 2)
    cv2.imshow("Adaptive", img)


if __name__ == '__main__':
    image_name = "images/fruit.jpeg"
    as_gray = True
    threshold_value = 115
    gray_img = read_image(image_name, as_gray)
    basic_threshold(gray_img, threshold_value)
    adaptive_threshold(gray_img, threshold_value)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
