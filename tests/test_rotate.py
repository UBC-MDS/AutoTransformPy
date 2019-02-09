import sys
sys.path.append("../AutoTransformPy")
import AutoTransformPy as pre

def test_inputs():
    with pytest.raises(TypeError):
       pre.rotate(6, 5, 345) # Not a string for the file path
       pre.rotate("Path", "seven", 345) # Not a valid number of images
       pre.rotate("Path", 6, "eight") # Not a valid rotation amount

    with pytest.raises(ValueError):
        pre.rotate("Path", 7, 500) # Outside of the rotation range

def return_imgs():
    test_img = skimage.io.imread("test_img")
    returned_arr = pre.rotate("test_image", 5, 180)
    assert returned_arr.shape()[0] == 5
    assert returned_arr.shape()[1:] == test_img.shape()
