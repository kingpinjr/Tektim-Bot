import os

from skimage.io import imread
from skimage.transform import resize
from skimage.color import rgb2gray


# format image to be 256x256 b/w
def create_img_data(filepath):
    formatted_image = ''
    img = imread(filepath)[:,:,:3]
    formatted_image = resize(img, (256, 256))
    formatted_image = rgb2gray(formatted_image) # this requries only 3 channels.
    formatted_image = formatted_image.flatten()
    return formatted_image