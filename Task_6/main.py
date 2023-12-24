import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops


def filling_factor(reg):
    return reg.image.mean()


def recognize(reg):
    if filling_factor(reg) == 1:
        return "-"
    else:
        euler = reg.euler_number
        if euler == -1:
            if 1 in reg.image.mean(0)[:2]:
                return "B"
            else:
                return "8"
        elif euler == 0:
            tmp = reg.image.copy()
            if 1 in reg.image.mean(0)[:2]:
                tmp[len(tmp[:, 0]) // 2, :] = 1
                tmp_labeled = label(tmp)
                tmp_regions = regionprops(tmp_labeled)
                if tmp_regions[0].euler_number == -1:
                    return "D"
                elif tmp_regions[0].euler_number == 0:
                    return "P"
            tmp[-1, :] = 1
            tmp_labeled = label(tmp)
            tmp_regions = regionprops(tmp_labeled)
            if 1 in reg.image.mean(0) and reg.eccentricity < 0.5:
                return '*'
            elif tmp_regions[0].euler_number == -1:
                return "A"
            return "0"
        else:
            if 1 in reg.image.mean(0):
                return "1"
            tmp = reg.image.copy()
            tmp[[0, -1], :] = 1
            tmp_labeled = label(tmp)
            tmp_regions = regionprops(tmp_labeled)
            euler = tmp_regions[0].euler_number
            if euler == -1:
                return "X"
            elif euler == -2:
                return "W"
            if reg.eccentricity > 0.5:
                return "/"
            else:
                return "*"


img = plt.imread('symbols.png')
binary = img.mean(2)
binary[binary != 0] = 1

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
print(f'Percentage of character recognition: {(labeled.max() - counts.get("?", 0)) / labeled.max()}')
plt.show()
