import sys
import pytest
from skimage.io import imread
sys.path.append("../AutoTransformPy/")
from AutoTransformPy import translate as trans

def test_inputs():
    with pytest.raises(TypeError):
       trans.translate(6, 5, 2) # Not a string for the file path
       trans.translate("imgs/milad.jpg", "seven", 2) # Not a valid number of images
       trans.translate("imgs/milad.jpg", 6, "eight") # Not a valid translation amount

    with pytest.raises(ValueError):
        trans.translate("imgs/milad.jpg", 7, 1000) # Outside of the translation range, possible to get empty images

def test_return_imgs(): # Tests that the number of images returned from translate is correct
    test_img = imread("imgs/milad.jpg")
    returned_arr = trans.translate("imgs/milad.jpg", 5, 10)

    assert returned_arr[0].shape == test_img.shape
    assert returned_arr.shape[0] == 6
    assert returned_arr.shape[1:] == test_img.shape
