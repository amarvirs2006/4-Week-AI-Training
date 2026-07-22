# Day 27 – OpenCV Image Transformations

Today, I learned various image transformation techniques using **OpenCV**. I practiced resizing, cropping, flipping, and rotating images, which are commonly used in image processing and computer vision applications.

## Topics Learned

* Image Resizing
* Image Cropping
* Image Flipping
* Image Rotation
* Transformation Matrix
* Image Manipulation using OpenCV

---

# Image Resizing

Image resizing changes the dimensions of an image without changing its content. It is useful for reducing image size, preparing images for machine learning models, or displaying images at different resolutions.

### Example

```python
resized = cv2.resize(image, (300, 200))
```

---

# Image Cropping

Cropping extracts a specific portion of an image by selecting a range of rows and columns.

### Example

```python
cropped = image[200:400, 1000:1200]
```

Cropping is commonly used to focus on a region of interest (ROI).

---

# Image Flipping

Flipping creates a mirror image by reversing the image horizontally or vertically.

### Flip Codes

* `0` → Vertical Flip
* `1` → Horizontal Flip
* `-1` → Both Horizontal and Vertical

### Example

```python
flipped = cv2.flip(image, 1)
```

---

# Image Rotation

Rotation changes the orientation of an image around a specified center point.

In today's program:

* Rotation Angle = **120°**
* Scale = **0.5**

### Example

```python
(h, w) = image.shape[:2]

center = (w // 2, h // 2)

M = cv2.getRotationMatrix2D(center, 120, 0.5)

rotated = cv2.warpAffine(image, M, (w, h))
```

---

# Transformation Matrix

The `getRotationMatrix2D()` function creates a transformation matrix that specifies:

* Center of rotation
* Rotation angle
* Scaling factor

This matrix is then applied using `cv2.warpAffine()` to generate the rotated image.

---

# Applications of Image Transformations

Image transformation techniques are widely used in:

* Image Editing
* Data Augmentation
* Object Detection
* Face Recognition
* Medical Image Processing
* Computer Vision Projects

---

## What I Learned Today

* Learned how to resize images using `cv2.resize()`.
* Cropped a specific region from an image using array slicing.
* Flipped images horizontally using `cv2.flip()`.
* Rotated images using a transformation matrix.
* Understood the purpose of `getRotationMatrix2D()` and `warpAffine()`.
* Gained practical experience with basic image manipulation techniques in OpenCV.
