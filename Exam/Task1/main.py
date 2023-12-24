import cv2

image = cv2.imread('task1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 3, 1)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
max_area = -1
max_contour = None
max_obj_i = -1
for i, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    print(f"Object{i}'s area: {area}")
    if area > max_area:
        max_obj_i = i
        max_area = area
        max_contour = contour

image_with_contour = cv2.drawContours(image, [max_contour], -1, (0, 255, 0), 2)
print(f"The biggest Object{max_obj_i}'s area:", max_area)
cv2.imshow(f"There is Object{max_obj_i}", image_with_contour)
cv2.waitKey(0)
cv2.destroyAllWindows()
