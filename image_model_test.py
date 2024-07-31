import os

from skimage.io import imread
from skimage.transform import resize

input_dir = "C:\\Users\\timka\\Documents\\code\\python\\Tektim-Bot\\data\\images\\processed"
categories = ['cringe','neutral','funny']

# x-input
data = []
# y-output
labels = []
for category in categories:
    for file in os.listdir(os.path.join(input_dir, category)):
        img_path = os.path.join(input_dir, category, file)
        img = imread(img_path)
        img = resize(img, (15, 15)) # 15x15 is the size
        data.append(img.flatten())