import cv2
import numpy as np
from skimage import measure

img = cv2.imread("task1.png", 0)

bin_img = (img != 51).astype(np.uint8)
_, connected_objs = cv2.connectedComponents(bin_img)
objs = measure.regionprops(connected_objs)

object_internal_areas = []
for i in range(len(objs)):
    internal_area = objs[i].area - objs[i].perimeter
    print(f"Object{i}'s\n   area:{objs[i].area},\n   perimeter: {objs[i].perimeter},\n   internal area: {internal_area}")
    object_internal_areas.append(internal_area)

print(f"\nThe biggest internal area: {max(object_internal_areas)}")
