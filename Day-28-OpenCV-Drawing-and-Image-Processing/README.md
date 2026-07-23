# Day 28 – OpenCV Drawing and Image Processing

Today, I learned how to draw different shapes on images, add text, capture videos using a webcam, save videos, and apply basic image processing techniques such as blurring and sharpening using OpenCV.

## Topics Learned

* Drawing Lines
* Drawing Rectangles
* Drawing Circles
* Adding Text to Images
* Video Capture
* Saving Videos
* Median Blur
* Gaussian Blur
* Image Sharpening

---

# Drawing a Line

A line can be drawn on an image using the `cv2.line()` function.

### Example

```python
cv2.line(image, (50, 50), (250, 50), (0, 255, 0), 2)
```

Parameters:

* Starting Point
* Ending Point
* Color (BGR)
* Thickness

---

# Drawing a Rectangle

Rectangles are drawn using `cv2.rectangle()`.

### Example

```python
cv2.rectangle(image, (50, 50), (250, 180), (255, 0, 0), 3)
```

This function requires the top-left and bottom-right coordinates of the rectangle.

---

# Drawing a Circle

A circle can be drawn using `cv2.circle()`.

### Example

```python
cv2.circle(image, (150, 150), 60, (0, 0, 255), 3)
```

Parameters include:

* Center Point
* Radius
* Color
* Thickness

---

# Adding Text

Text can be displayed on an image using `cv2.putText()`.

### Example

```python
cv2.putText(
    image,
    "OpenCV",
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)
```

This allows annotations or labels to be added to images.

---

# Video Capture

OpenCV can access the system webcam using `VideoCapture()`.

### Example

```python
cap = cv2.VideoCapture(0)
```

Frames captured from the webcam can be displayed continuously until the user exits.

---

# Saving a Video

Captured video frames can be saved using the `VideoWriter` class.

### Example

```python
writer = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    20.0,
    (640, 480)
)
```

This enables recording webcam footage and storing it as a video file.

---

# Median Blur

Median Blur removes noise by replacing each pixel with the median value of its neighboring pixels.

### Example

```python
blur = cv2.medianBlur(image, 5)
```

It is particularly effective for removing salt-and-pepper noise while preserving edges.

---

# Gaussian Blur

Gaussian Blur smooths an image by applying a Gaussian filter.

### Example

```python
blur = cv2.GaussianBlur(image, (5, 5), 0)
```

It reduces image noise and detail, making it useful as a preprocessing step in many computer vision tasks.

---

# Image Sharpening

Sharpening enhances edges and fine details, making an image appear clearer.

This is commonly done using a sharpening kernel with image filtering.

### Example

```python
kernel = [[0, -1, 0],
          [-1, 5, -1],
          [0, -1, 0]]
```

Applying this kernel increases the contrast around edges and highlights important features.

---

## Applications

The techniques learned today are widely used in:

* Image Annotation
* Computer Vision
* Object Detection
* Image Enhancement
* Video Recording
* Surveillance Systems
* Image Preprocessing for Machine Learning

---

## What I Learned Today

* Drew lines, rectangles, and circles on images.
* Added text to images using OpenCV.
* Captured live video from a webcam.
* Learned how to save recorded video files.
* Applied Median Blur to reduce image noise.
* Applied Gaussian Blur for image smoothing.
* Understood image sharpening using convolution kernels.
* Gained practical knowledge of common image processing operations used in computer vision.
