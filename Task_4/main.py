import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation, binary_erosion, binary_opening, binary_closing
from skimage.measure import label

img = np.load("ps.npy.txt")
plt.subplot(121)
plt.imshow(img)
struct1 = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1]]
struct2 = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [1, 1, 0, 0, 1, 1],
           [1, 1, 0, 0, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1]]

struct3 = [[1, 1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 1],
           [1, 1, 0, 0, 1, 1],
           [1, 1, 0, 0, 1, 1],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]

struct4 = [[1, 1, 1, 1, 0, 0],
           [1, 1, 1, 1, 0, 0],
           [1, 1, 0, 0, 0, 0],
           [1, 1, 0, 0, 0, 0],
           [1, 1, 1, 1, 0, 0],
           [1, 1, 1, 1, 0, 0]]

struct5 = [[0, 0, 1, 1, 1, 1],
           [0, 0, 1, 1, 1, 1],
           [0, 0, 0, 0, 1, 1],
           [0, 0, 0, 0, 1, 1],
           [0, 0, 1, 1, 1, 1],
           [0, 0, 1, 1, 1, 1]]


def main():
    print(f"Number of Objects: {np.max(label(img))}")

    for struct, name in zip((struct1, struct2, struct3, struct4, struct5),
                            ("Rectangle", "U", "∩", "⊂", "⊃")):
        if struct == struct2 or struct == struct3:
            print(f"{name}: {np.max(label(binary_erosion(img, struct))) - np.max(label(binary_erosion(img, struct1)))}")
        else:
            print(f"{name}: {np.max(label(binary_erosion(img, struct)))}")


if __name__ == '__main__':
    main()