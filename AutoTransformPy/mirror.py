# Copyright 2019 Alycia Butterworth
# Licensed under the MIT License
# Use of this file must be in compliance with the License, LICENSE.md
#
# February 2019
# This script is for AutoTransformPy function Mirror.

from skimage.io import imread
import os
import numpy as np

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

    try:
        # check for valid input parameters
        if not isinstance(image_path, str):
            raise TypeError("The file path must be a string.")

        if not isinstance(direction, str):
            raise TypeError("The direction must be a string: 'horizontal', 'vertical', or 'all'")

        if not direction.lower() in ["horizontal","vertical", "all"]:
            raise ValueError("The direction must be 'horizontal', 'vertical' or 'all'")

        img = imread(image_path)

    except TypeError as e:
        print("Invalid parameter types. Correct parameter types: image_path: str, num_images: int, direction: string")
        raise e
    except ValueError as e:
        print("Invalid direction value. The direction must be a string: 'horizontal', 'vertical', or 'all'")
        raise e
    except FileNotFoundError as e:
        raise e

    # import image as array
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
