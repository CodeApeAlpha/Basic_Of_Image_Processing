# Article
# https://www.analyticsvidhya.com/blog/2014/12/image-processing-python-basics/
from matplotlib import pyplot as plt, cm
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread
example_file = glob.glob(r"Stars.jpg")[0]
image = imread(example_file, as_gray=True)
blobs_log = blob_log(image,max_sigma=30, num_sigma=10,threshold=0.1)
# Compute radi in the 3rd column
blobs_log[:, 2] = blobs_log[:, 2]*sqrt(2)
narrows = len(blobs_log)
print("Number of stars counted: ", narrows)
fig, ax = plt.subplots(1, 1)
plt.imshow(image, cmap=cm.gray)
for blob in blobs_log:
    y, x, r = blob
    c = plt.Circle((x, y), r+5, color="lime", linewidth=2, fill=False)
    ax.add_patch(c)
plt.show()