#Copyright 2019 Alycia Butterworth
# Licensed under the MIT License
# Use of this file must be in compliance with the License, LICENSE.md
#
# February 2019
# This script tests the function mirror.py of AutoTransformPy package.

# Input  :  An image location in string format
# Input  :  A direction of mirroring: ['horizontal','vertical','all']
# Output : An np.array of the mirrored image(s)

import sys
import pytest
from skimage.io import imread
import numpy as np
sys.path.append("../AutoTransformPy/")
import mirror as mir

def test_inputs():
    with pytest.raises(TypeError):
       mir.mirror("../tests/imgs/milad.jpg", 7) # direction must be string
    with pytest.raises(TypeError):
       mir.mirror(True, "horizontal") # image path must be a string

    with pytest.raises(ValueError):
        mir.mirror("../tests/imgs/milad.jpg", "h") # Not a valid string option for direction

    with pytest.raises(FileNotFoundError):
        mir.mirror("../tests/imgs/Path.jpg") # Incorrect directory/file not in location

def test_return_imgs(): # Tests that the number of images returned from translate is correct
    test_img = imread("../tests/imgs/milad.jpg")
    returned_arr_1a = mir.mirror("../tests/imgs/milad.jpg", "horizontal") # should return 1 image
    returned_arr_1b = mir.mirror("../tests/imgs/milad.jpg", "vertical") # should return 1 image
    returned_arr_2a = mir.mirror("../tests/imgs/milad.jpg", "all") # should return 2 images
    returned_arr_2b = mir.mirror("../tests/imgs/milad.jpg") # all is default, should return 2 images

    assert returned_arr_1a.shape[0] == 2  # check two image in array (original and mirrored)
    assert returned_arr_1b.shape[0] == 2  # check two image in array (original and mirrored)
    assert returned_arr_2a.shape[0] == 3  # check three images in array (original and mirrored both directions)
    assert returned_arr_2b.shape[0] == 3  # check three images in array (original and mirrored both directions)
    assert returned_arr_1a.shape[1:] == test_img.shape # check that returned image shapes same as input image shape

    assert np.all(returned_arr_1a[1,:,1] == test_img[:,(test_img.shape[1]-2)])  # check that image is correctly mirrored horizontally
    assert np.all(returned_arr_1b[1,1,:] == test_img[(test_img.shape[0] - 2),:])  # check that image is correctly mirrored vertically
    assert np.all(returned_arr_2b[1,:,1] == test_img[:,(test_img.shape[1] - 2)]) # check horizontal image mirroring on 'all'
    assert np.all(returned_arr_2b[2,1,:] == test_img[(test_img.shape[0] - 2),:]) # check vertical image mirroring on 'all'
