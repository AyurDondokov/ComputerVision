import cv2
import numpy as np

image = cv2.imread("task2.png")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

saturation = hsv_image[:, :, 1]
max_saturation_idx = np.unravel_index(np.argmax(saturation), saturation.shape)
center_pos = (max_saturation_idx[1], max_saturation_idx[0])

radius = 10
mask = np.zeros_like(saturation)
cv2.circle(mask, center_pos, radius, 255, -1)
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
