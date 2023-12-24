import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops


def filling_factor(reg):
    return reg.image.mean()


def recognize(reg):
    euler = reg.euler_number
    if euler == 0:
        if 1 in reg.image.mean(1):
            return "R"
        else:
            return "D"
    else:
        if 1 not in reg.image.mean(1):
            return "K"
        else:
            if reg.image[0][0] == 1:
                return "L"
            else:
                return "J"


img = plt.imread('task3.png')
binary = img.mean(2) > 0.25

labeled = label(binary)
print(f"Number of symbols: {np.max(labeled)}")

regions = regionprops(labeled)
counts = {}
for region in regions:
    symbol = recognize(region)
    if symbol not in counts:
        counts[symbol] = 0
    counts[symbol] += 1

print(f"All symbols:\n{counts}")
