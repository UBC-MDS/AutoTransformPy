import sys
sys.path.append("../AutoTransformPy")
import AutoTransformPy as pre

def test_inputs():
    with pytest.raises(TypeError):
       pre.mirror("Path", 7) # direction must be string
       pre.mirror(True, "horizontal") # image path must be a string

    with pytest.raises(ValueError):
        pre.mirror("Path", "h") # Not a valid string option for direction

    with pytest.raises(FileNotFoundError):
        pre.mirror("img/Path") # Incorrect directory/file not in location

def return_imgs(): # Tests that the number of images returned from translate is correct
    test_img = skimage.io.imread(test_image)
    returned_arr_1a = pre.mirror(test_img, "horizontal") # should return 1 image
    returned_arr_1b = pre.mirror(test_img, "vertical") # should return 1 image
    returned_arr_2a = pre.mirror(test_img, "all") # should return 2 images
    returned_arr_2b = pre.mirror(test_img) # all is default, should return 2 images
    
    assert returned_arr_1a.shape()[0] == 1
    assert returned_arr_1b.shape()[0] == 1
    assert returned_arr_2a.shape()[0] == 2
    assert returned_arr_2b.shape()[0] == 2
    assert returned_arr_1a.shape()[1:] == test_img.shape() # check that returned image shapes same as input image shape

def test_parameters():
    if direction == "horizontal": # pixel values from the 2nd to last column in original image should be in 2nd column in new image
        assert returned_arr_1a[:,1] == test_img[:, (test_img.shape[0] - 3)]

    if direction == "vertical": # pixel values from 2nd to last row in original image should be in 2nd row in new image
        assert returned_arr_1b[1,:] == test_img[(test_img.shape[0] - 3),:]

    if direction == "all": # test that first image in array is horizontally mirrored and second image is vertically mirrored
        assert returned_arr_2b[0,:,1] == test_img[0,:,(test_img.shape[0] - 3)] # check horizontal image
        assert returned_arr_2b[1,1,:] == test_img[1,(test_img.shape[0] - 3),:] # check vertical image
