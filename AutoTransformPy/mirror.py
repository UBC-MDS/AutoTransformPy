# Copyright 2019 Alycia Butterworth
# Licensed under the MIT License
# Use of this file must be in compliance with the License, LICENSE.md
#
# February 2019
# This script is for AutoTransformPy function Mirror.


import numpy as np
from skimage.ip import imread

def mirror(image_path, direction = 'all'):
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

    # import image as array
    img = imread(image_path)
    mirrored_images = []

    # flip horizontally
    if direction == 'horizontal' or direction == 'all':
        horiz_image = np.fliplr(img)
        mirrored_images.append(horiz_image)

    # flip vertically
    if direction == 'vertical' or direction == 'all':
        vert_image = img[::-1]
        mirrored_images.append(vert_image)

    # convert mirrored_images back to an array
    mirrored_images = np.asarray(mirrored_images)

    return mirrored_images
