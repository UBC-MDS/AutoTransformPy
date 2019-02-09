import sys
sys.path.append("../AutoTransformPy")
import AutoTransformPy as pre

def test_inputs():
    with pytest.raises(TypeError):
       pre.translate(6, 5, 2, False) # Not a string for the file path
       pre.translate("Path", "seven", 2, False) # Not a valid number of images
       pre.translate("Path", 6, "eight", False) # Not a valid translation amount

    with pytest.raises(ValueError):
        pre.translate("PathTo300x300Image", 7, 301, False) # Outside of the translation range, possible to get empty images

def return_imgs(): # Tests that the number of images returned from translate is correct
    test_img = skimage.io.imread("test_img")
    returned_arr = pre.translate("test_image", 5, 10, False)
    assert returned_arr.shape()[0] == 5
    assert returned_arr.shape()[1:] == test_img.shape()
