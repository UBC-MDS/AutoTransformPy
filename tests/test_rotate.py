import sys
import os
import pytest
from skimage.io import imread
from AutoTransformPy import rotate as rot

fname = os.path.join(os.path.dirname(__file__), '../tests/imgs/milad.jpg')

def test_inputs():
    with pytest.raises(TypeError):
       rot.rotate(6, 5, 345) # Not a string for the file path
       rot.rotate(fname, "seven", 345) # Not a valid number of images
       rot.rotate(fname, 6, "eight") # Not a valid rotation amount

    with pytest.raises(ValueError):
        rot.rotate(fname, 7, 500) # Outside of the rotation range
        rot.rotate(fname, -1, 500) # Nonsense number of images to return

    with pytest.raises(FileNotFoundError):
        rot.rotate("../tests/imgs/Path.jpg", 7, 100) # Incorrect directory/file not in location

def test_return_imgs(): # Tests that the number of images returned from rotate is correct
    test_img = imread(fname)
    returned_arr = rot.rotate(fname, 5, 180)
    assert returned_arr.shape[0] == 6
    assert returned_arr.shape[1:] == test_img.shape
