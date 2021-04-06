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
