# Day 26 – Introduction to OpenCV

Today, I learned the basics of **OpenCV (Open Source Computer Vision Library)**. I understood how to install and import OpenCV, read and display images, access image properties, convert images to grayscale, and save processed images.

## Topics Learned

* Introduction to OpenCV
* Installing OpenCV
* Importing OpenCV
* Reading Images
* Displaying Images
* Image Properties
* Converting Images to Grayscale
* Saving Images

---

# What is OpenCV?

**OpenCV (Open Source Computer Vision Library)** is an open-source library used for computer vision and image processing. It provides a large collection of functions for working with images and videos and is widely used in Artificial Intelligence and Machine Learning projects.

---

# Installing OpenCV

OpenCV can be installed using pip.

### Command

```bash
pip install opencv-python
```

---

# Importing OpenCV

After installation, the library is imported using:

```python
import cv2
```

---

# Reading an Image

Images can be loaded using the `cv2.imread()` function.

### Example

```python
image = cv2.imread("image.jpeg")
```

If the image is not found, `cv2.imread()` returns `None`.

---

# Displaying an Image

An image can be displayed using `cv2.imshow()`. The window remains open until a key is pressed.

### Example

```python
cv2.imshow("My Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

# Checking Image Properties

The dimensions and number of color channels of an image can be obtained using the `shape` attribute.

### Example

```python
height, width, channels = image.shape

print(height, width, channels)
```

Where:

* Height → Number of rows
* Width → Number of columns
* Channels → Number of color channels (usually 3 for RGB/BGR images)

---

# Converting an Image to Grayscale

A colored image can be converted into a grayscale image using `cv2.cvtColor()`.

### Example

```python
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

Grayscale images contain only intensity values instead of color information.

---

# Saving an Image

The processed image can be saved using `cv2.imwrite()`.

### Example

```python
cv2.imwrite("output.jpeg", image)
```

---

## Applications of OpenCV

* Face Detection
* Object Detection
* Image Classification
* Video Processing
* Medical Image Analysis
* Self-Driving Cars
* Security and Surveillance

---

## What I Learned Today

* Learned what OpenCV is and its applications.
* Installed and imported the OpenCV library.
* Read images using `cv2.imread()`.
* Displayed images using `cv2.imshow()`.
* Retrieved image height, width, and channel information.
* Converted color images into grayscale images.
* Saved processed images using `cv2.imwrite()`.
* Understood the basic workflow of image processing using OpenCV.
