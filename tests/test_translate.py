import sys
import os
import pytest
from skimage.io import imread
from AutoTransformPy import translate as trans

fname = os.path.join(os.path.dirname(__file__), '../tests/imgs/milad.jpg')

def test_inputs():
    with pytest.raises(TypeError):
       trans.translate(6, 5, 2) # Not a string for the file path
    with pytest.raises(TypeError):
       trans.translate(fname, "seven", 2) # Not a valid number of images
    with pytest.raises(TypeError):
       trans.translate(fname, 6, "eight") # Not a valid translation amount

    with pytest.raises(ValueError):
        trans.translate(fname, 7, 1000) # Outside of the translation range, possible to get empty images
    with pytest.raises(ValueError):
        trans.translate(fname, -1, 500) # Nonsense number of images to return

    with pytest.raises(FileNotFoundError):
        trans.translate("../tests/imgs/Path.jpg", 7, 100) # Incorrect directory/file not in location


def test_return_imgs(): # Tests that the number of images returned from translate is correct
    test_img = imread(fname)
    returned_arr = trans.translate(fname, 5, 10)

    assert returned_arr[0].shape == test_img.shape
    assert returned_arr.shape[0] == 6
    assert returned_arr.shape[1:] == test_img.shape
