import numpy as np
import cv2

pencils = 0
for i in range(0, 12):
    img = cv2.imread(f"images/img ({i + 1}).jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 128, 192, cv2.THRESH_OTSU)
    img = cv2.bitwise_not(binary)

    unique = np.unique(img)
    img[img != unique[1]] = 0
    img = img[:, :img.shape[1] - 50]

    edged = cv2.Canny(img, 0, 255)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (100, 100))
    edged = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cont in contours:
        p = cv2.arcLength(cont, True)
        approx = cv2.approxPolyDP(cont, 0.02 * p, True)
        for j in range(1, len(approx)):
            dx = (approx[j][0][0] - approx[j - 1][0][0]) ** 2
            dy = (approx[j][0][1] - approx[j - 1][0][1]) ** 2
            edge_length = (dx + dy) ** 0.5
            if edge_length >= 2500:
                pencils += 1

print(f"Number of pencils: {pencils}")
