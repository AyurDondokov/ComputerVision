import cv2
import matplotlib.pyplot as plt

img = cv2.imread("task2.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

max_saturation = 0
for row in range(hsv_img.shape[0]):
    for column in range(hsv_img.shape[1]):
        if hsv_img[row, column][1] > max_saturation:
            max_saturation = hsv_img[row, column][1]

for row in range(hsv_img.shape[0]):
    for column in range(hsv_img.shape[1]):
        if hsv_img[row, column][1] != max_saturation:
            hsv_img[row, column] = [0, 0, 0]

rgb_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
plt.imshow(rgb_img)
plt.show()
