# Copyright 2019 Alycia Butterworth
# Licensed under the MIT License
# Use of this file must be in compliance with the License, LICENSE.md
#
# February 2019
# This script is for AutoTransformPy function Mirror.


import numpy as np
from skimage.io import imread
import os

def mirror (image_path, direction = 'all'):
    """Returns an array of image(s) that are the mirrored form of the original image

    Mirror takes the path to an image and generates a mirrored version of that image
    in the horizontal direction, vertical direction, or both.
    It returns an array of pixel values for the mirrored image(s).

    Inputs:
    -------
    image_path: string
        The file path of the image to be mirrored.
    direction: string
        Direction of mirroring.
        Options: 'horizontal', 'vertical', 'all'
        Default: 'all'

    Returns:
    --------
    mirrored_images: np.array
    """

    # check for valid input parameters

    if not isinstance(image_path, str):
        raise TypeError("The file path must be a string.")

    if not isinstance(direction, str):
        raise TypeError("The direction must be a string: 'horizontal', 'vertical', or 'all'")

    if not direction.lower() in ["horizontal","vertical", "all"]:
        raise ValueError("The direction must be 'horizontal', 'vertical' or 'all'")

    if not os.path.isfile(image_path):
        raise FileNotFoundError("No image found at path")

    # import image as array
    img = imread(image_path)
    mirrored_images = [img]

    # flip horizontally
    if direction.lower() == 'horizontal' or direction.lower() == 'all':
        horiz_image = np.fliplr(img)
        mirrored_images.append(horiz_image)

    # flip vertically
    if direction.lower() == 'vertical' or direction.lower() == 'all':
        vert_image = img[::-1]
        mirrored_images.append(vert_image)

    # convert mirrored_images back to an array
    mirrored_images = np.asarray(mirrored_images)

    return mirrored_images
