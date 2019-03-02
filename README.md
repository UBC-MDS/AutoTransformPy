# AutoTransform

## Contributors

| Name | GitHub |
|---|---|
| Alycia Butterworth | [alyciakb](https://github.com/alyciakb) |
| Brenden Everitt | [everittB](https://github.com/everittB) |
| Rayce Rossum | [RayceRossum](https://github.com/RayceRossum) |


## Overview

A common application of supervised machine learning is identifying the object of an image. One issue that users encounter is a model misclassifying a new image because the object is rotated or translated in some way that was not captured in the training images. The purpose of this package is to create a more robust set of images for users to train their model with. The package will accept an image as an input, apply a series of transformations to it, and return an array of transformed pixel values. Transformations include: rotating, mirroring, and translating (shifting the object's location in the frame).

## Functions

#### Rotate

Rotates an image the user-specified number of times. The degree of rotation is chosen randomly and may be in either the clockwise or counter-clockwise direction. The user specifies the maximum rotation angle. It returns the pixel values of the rotated images.

#### Mirror

Mirrors an image in the horizontal and/or vertical direction and returns the pixel values of the mirrored image(s).

#### Translate

Translate will move an image within its frame, so that the topic of the image will be shifted to a new location in the frame. The distance and direction of translation will be chosen randomly, but the user specifies the maximum distance of the translation and the number of images they want generated. It returns the pixel values of the translated images.


## Python Environment

Scikit-image is a image processing package that contains functions for performing various operations to images, such as rotating or resizing, among many others. AutoTransformPy utilizes some of this packages functionality and builds it out, so the user can easily gain many variations of an image. The intended usage of this package is for the development of a larger set of training images for the training of an image classification algorithms.


## Installation

To install AutoTransformPy:

1. In your console, type: `pip install git+https://github.com/UBC-MDS/AutoTransformPy.git`
2. You can now use AutoTransformPy. See usage instructions below:

## Usage

### Rotate

`from AutoTransformPy.rotate import rotate`

`rotate(image_path, num_images, max_rotation)`

**Arguments:**

- `image_path`: file path of the input image (string)
- `num_images`: number of randomly rotated images to be returned (integer)
- `max_rotation`: maximum allowable degrees of rotation of the images (integer) between 1 and 360

**Output:**

- An np.array of pixel values of the rotated images. Array contains `num_images` + 1 images (original plus all rotated images)

**Example:**

- `rotate("../tests/imgs/milad.jpg", 10, 280)`


### Mirror

`from AutoTransformPy.mirror import mirror`

`mirror(image_path, direction)`

**Arguments:**

- `image_path`: file path of the input image (string)
- `direction`: direction of mirroring (string, optional) 'horizontal', 'vertical', or 'all'. If not specified, defaults to 'all'

**Output:**

- An np.array of pixel values of the mirrored images. Array contains 3 images if `direction = 'all'` (original, horizontally mirrored, vertically mirrored) or 2 images if direction is horizontal or vertical (original image, mirrored image)

**Example:**

- `mirror("../tests/imgs/milad.jpg", "horizontal")`


### Translate

`from AutoTransformPy.translate import translate`

`translate(image_path, num_images, max_translation)`

**Arguments:**

- `image_path`: file path of the input image (string)
- `num_images`: number of randomly translated images to be returned (integer)
- `max_translation`: maximum distance in pixels that the image can be translated (integer)

**Output**

- An np.array of pixel values of the translated images. Array contains `num_images` + 1 images (original plus all translated images)

**Example:**

- `translate("../tests/imgs/milad.jpg", 5, 80)`


## Package Dependencies

- `numpy`
- `skimage`
- `os`


## Full Usage Example & Output

```
# pip install git+https://github.com/UBC-MDS/AutoTransformPy.git

from AutoTransformPy.mirror import mirror
from AutoTransformPy.rotate import rotate
from AutoTransformPy.translate import translate
from skimage.io import imshow

# perform transformations
m = mirror("../tests/imgs/milad.jpg", "horizontal")
r = rotate("../tests/imgs/milad.jpg", 10, 280)
t = translate("../tests/imgs/milad.jpg", 5, 80)

# view dimensions of returned arrays
m.shape  # mirror function
r.shape  # rotate function
t.shape  # translate function

# display original image
imshow(m[0])
imshow(r[0])
imshow(t[0])

# display one of the transformed images
imshow(m[1])
imshow(r[1])
imshow(t[1])

```

# Tests Output

