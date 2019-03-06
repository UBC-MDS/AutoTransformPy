import sys
import os
import pytest
from skimage.io import imread
from AutoTransformPy import rotate as rot

def test_inputs():
    with pytest.raises(TypeError):
       rot.rotate(6, 5, 345) # Not a string for the file path
       rot.rotate("../../tests/imgs/milad.jpg", "seven", 345) # Not a valid number of images
       rot.rotate("../../tests/imgs/milad.jpg", 6, "eight") # Not a valid rotation amount

    with pytest.raises(ValueError):
        rot.rotate("../../tests/imgs/milad.jpg", 7, 500) # Outside of the rotation range
        rot.rotate("../../tests/imgs/milad.jpg", -1, 500) # Nonsense number of images to return

    with pytest.raises(FileNotFoundError):
        rot.rotate("../tests/imgs/Path.jpg", 7, 100) # Incorrect directory/file not in location

def test_return_imgs(): # Tests that the number of images returned from rotate is correct
    test_img = imread("../../tests/imgs/milad.jpg")
    returned_arr = rot.rotate("../../tests/imgs/milad.jpg", 5, 180)
    assert returned_arr.shape[0] == 6
    assert returned_arr.shape[1:] == test_img.shape
