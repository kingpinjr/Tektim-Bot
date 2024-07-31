import os

from skimage.io import imread
from skimage.transform import resize

img = imread("C:\\Users\\timka\\Documents\\code\\python\\Tektim-Bot\\data\\images\\processed\\12_1_1_image.png.9383beab-a697-4121-8349-0a6bcefba177.png")
img1 = img.flatten()
print(len(img1))

img2 = resize(img, (15, 15))
img2 = img2.flatten()
print(len(img2))