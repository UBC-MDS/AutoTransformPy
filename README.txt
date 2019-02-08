===============
 AutoTransform
===============

 =================== =================
 Contributors        GitHub
 =================== =================
 Alycia Butterworth  `alyciakb`_
 Brenden Everitt     `everittB`_
 Rayce Rossum        `RayceRossum`_
 =================== =================

Overview
--------

A common application of supervised machine learning is identifying the object of an image. One issue that users encounter is a model misclassifying a new image because the object is rotated or translated in some way that was not captured in the training images. The purpose of this package is to create a more robust set of images for users to train their model with. The package will accept a set of images as an input, apply a series of translations to them, and return a larger, robust training set. Translations include: rotating, mirroring, shifting the object's location in the frame, darkening, and colour manipulations.

Functions
---------

Rotate
------

- Parameters:
  - Image to transform
  - Number of images to generate (integer)
  - Maximum rotation in degrees (integer)
- Returns:
  - Array of randomly rotated (within max range) images of length based on number of images parameter

Mirror
------
- Parameters:
  - Image to transform
- Returns:
  - Array of a single mirrored image

Chameleon
---------
- Parameters:
  - Image to transform
  - Number of images to generate (integer)
  - Maximum change in pixel colour (integer)
- Returns:
  - Array of randomly colour modified (within max range) images of length based on number of images parameter


Similar Packages
----------------

Scikit-image is a image processing package that contains functions for performing various operations to images, such as rotating or resizing, among many others. R has a new package, OpenImageR, that is similar to scikit-image that has functions for image preprocessing, filtering, and image recognition. Our plan is to utilize some of these packages functionality and build them out so a user could pass in example images, from a training dataset for example, and get back different variations of them. We believe this could significantly help in the training of image classification algorithms.
