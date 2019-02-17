from skimage.io import imread, imshow
from skimage.transform import AffineTransform, warp
import numpy as np

def translate (image_path, num_images, max_translation):
    """Returns an array of images of length num_images randomly translated a random number of pixels up to max_rotation

    Translate takes the path to an image and generates randomly translated images, the desired number
    of times. Each translated image will not be translated more than the maximum distance provided.
    The translation can be in any direction.

    Inputs:
    -------
    image_path: string
        The file path of the image to be translated.
    num_images: integer
        The number of translated images to be returned.
    max_translation: integer
        The maximum distance in pixels that the image can be translated.

    Returns:
    --------
    translated_images: np.array
    """

    # Check for valid input paramters types
    if not isinstance(image_path, str):
        raise TypeError("The file path must be a string.")

    if not isinstance(num_images, int):
        raise TypeError("The number of images returned must be an integer.")

    if not isinstance(max_translation, int):
        raise TypeError("The maximum translation of images must be an integer.")

    # Check for valid input paramter values
    if num_images < 1:
        raise ValueError("The number of images returned must be 1 or greater.")

    org_image = imread(image_path)

    if max_translation >= org_image.shape[0] or max_translation >= org_image.shape[1]:
        raise ValueError("The maximum translation must be less than the width and height of the image.")

    # Perform image translation
    translations = (np.random.randint(-max_translation, max_translation, num_images), np.random.randint(-max_translation, max_translation, num_images))
    translated_images = [org_image]

    for i in range(len(translations[0])):
        tform = AffineTransform(translation=(translations[0][i], translations[1][i]))
        translated_images.append(warp(org_image, tform, mode="constant", preserve_range=True).astype('uint8'))

    return np.asarray(translated_images)
