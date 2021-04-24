import cv2 as cv
import matplotlib as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from skimage import data, io, filters
import sklearn as skl


def print_versions():
    print(f'tensorflow: {tf.__version__}')
    print(f'matplotlib: {plt.__version__}')
    print(f'numpy: {np.__version__}')
    print(f'opencv: {cv.__version__}')
    print(f'pandas: {pd.__version__}')
    print(f'scikit-learn: {skl.__version__}')


def draw_something():
    image = data.coins()
    edges = filters.sobel(image)
    io.imshow(edges)
    io.show()


if __name__ == '__main__':
    print_versions()
    draw_something()






def segment_diaphram2(image):
    for x in image[0]:
        minimum, maximum, _, _ = ndimage.extrema(x)
        print(f'min: {minimum}, max: {maximum}')

        blurred_image = ndimage.gaussian_filter(x, sigma=3)
        x = tf.where(blurred_image > 195, 0, x) 
    return image

def tf_segment_diaphram(image, label):
    pass