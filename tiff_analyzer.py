import numpy as np
from PIL import Image


def tiff_to_nparray(f):
    im = Image.open(f)
    imarray = np.array(im)
    return imarray
