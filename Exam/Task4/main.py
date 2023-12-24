import cv2
import numpy as np
from skimage import filters, measure


def find_circle(imr):
    max_area = imr[0].area
    result = [0, imr[0].axis_major_length, imr[0].axis_minor_length]
    for i in range(1, len(imr)):
        if imr[i].area > max_area:
            max_area = imr[i].area
            result = [i, imr[i].axis_major_length, imr[i].axis_minor_length]
    return result


def circle(img_path):
    image = cv2.imread(img_path, 0)
    binary_image = (image < filters.threshold_otsu(image)).astype(np.uint8)
    _, labeled_regions = cv2.connectedComponents(binary_image)
    result = measure.regionprops(labeled_regions)
    return result


image_path = "task4.jpg"
mr = circle(image_path)
arr = find_circle(mr)
nominal_resolution = 1.05714
length = (arr[1] + arr[2]) / 2 * nominal_resolution
print(f"The real diameter of the ball: {length}")
