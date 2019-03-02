# Copyright 2019 Brenden Everitt
# Licensed under the MIT License
# Use of this file must be in compliance with the License, LICENSE.md
#
# February 2019
# This script is for AutoTransformPy function Rotate.

from skimage.io import imread
from skimage.transform import rotate as rot
import numpy as np
import os

def rotate (image_path, num_images, max_rotation):
    """Returns an array of images of length num_images randomly rotated a random degree up to max_rotation

    Rotate takes the path to an image and generates randomly rotated images, the desired number
    of times. Each rotated image will not be rotated more than the maximum rotation
    angle provided. The rotation can be both clockwise or counter-clockwise.

    Inputs:
    -------
    image_path: string
        The file path of the image to be rotated.
    num_images: integer
        The number of rotated images to be returned.
    max_rotation: integer
        The maximum allowable rotation for any of the rotated images. Can be
        between 1 and 360.

    Returns:
    --------
    rotated_images: np.array
    """

    # Check for valid input paramters types
    if not isinstance(image_path, str):
        raise TypeError("The file path must be a string.")

    if not isinstance(num_images, int):
        raise TypeError("The number of images returned must be an integer.")

    if not isinstance(max_rotation, int):
        raise TypeError("The maximum rotation of images must be an integer.")

    # Check for valid input paramter values
    if num_images < 1:
        raise ValueError("The number of images returned must be 1 or greater.")

    if max_rotation < 1 or max_rotation > 360:
        raise ValueError("The maximum rotation must be between 1 and 360.")

    if not os.path.isfile(image_path):
        raise FileNotFoundError("No image found at path")

    # Perform image rotation
    rotations = np.random.randint(-max_rotation, max_rotation, num_images)
    org_image = imread(image_path)
    rotated_images = [org_image]

    for a_rotation in rotations:
        rotated_images.append(rot(org_image, a_rotation, resize=False).astype('uint8'))

    return np.asarray(rotated_images)
