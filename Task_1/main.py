import numpy as np
import matplotlib.pyplot as plt

for i in range(1, 7):
    file = open(f"figure{i}.txt")
    lines = file.readlines()
    size = float(lines[0].split()[0])
    file.close()
    s = []
    lines = lines[2:]
    for line in lines:
        arr = list(map(int, line.split()))
        s.append(sum(arr))
    if max(s) == 0:
        print(f"No image detected")
    else:
        print(f"The nominal resolution of the image in the figure{i}.txt: {size / max(s)}")

file1 = np.loadtxt(f"img1.txt", skiprows=2)
file2 = np.loadtxt(f"img2.txt", skiprows=2)
# plt.subplot(121)
# plt.imshow(file1)
# plt.subplot(122)
# plt.imshow(file2)
# plt.show()


def get_cent(img):
    rows, cols = img.shape
    x_sum = 0
    y_sum = 0
    count = 0

    for i in range(rows):
        for j in range(cols):
            if img[i, j] == 1:
                x_sum += j
                y_sum += i
                count += 1

    if count == 0:
        return None, None
    return x_sum / count, y_sum / count


centroid1 = get_cent(file1)
centroid2 = get_cent(file2)

if centroid1[0] is not None and centroid2[0] is not None:
    dx = centroid2[0] - centroid1[0]
    dy = centroid2[1] - centroid1[1]
    print(f"\nThe second image is shifted relative to the first one by (x={dx}; y={dy})")
else:
    print("There is no offset")
