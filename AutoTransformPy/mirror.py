def mirror(image_path, direction = 'all'):
  """Returns an array of image(s) that are the mirrored form of the original image

    Mirror takes the path to an image and generates a mirrored version of that image in the horizontal direction, vertical direction, or both.
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

