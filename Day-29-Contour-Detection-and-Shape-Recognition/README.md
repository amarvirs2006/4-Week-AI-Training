# Day 29 – Contour Detection and Shape Recognition

Today, I learned how to detect contours and identify basic geometric shapes using OpenCV. The program converts an image into grayscale, applies thresholding, detects contours, approximates their boundaries, and labels each detected shape on the image.

## Topics Learned

* Image Thresholding
* Contour Detection
* Drawing Contours
* Contour Approximation
* Shape Detection
* Shape Labeling

---

# What are Contours?

Contours are the boundaries of objects present in an image. They help identify the shape and outline of objects and are widely used in computer vision tasks such as object detection and shape recognition.

---

# Converting Image to Grayscale

The input image was first converted into a grayscale image before further processing.

### Example

```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```

Grayscale images simplify processing by reducing the image to a single intensity channel.

---

# Image Thresholding

Thresholding converts a grayscale image into a binary image by separating the foreground from the background.

### Example

```python
_, thresh = cv2.threshold(
    gray,
    200,
    255,
    cv2.THRESH_BINARY
)
```

---

# Contour Detection

Contours were detected using the `findContours()` function.

### Example

```python
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)
```

The detected contours represent the boundaries of objects in the image.

---

# Drawing Contours

Detected contours were drawn on the original image.

### Example

```python
cv2.drawContours(
    img,
    contours,
    -1,
    (0, 255, 0),
    3
)
```

---

# Contour Approximation

The contour boundaries were simplified using `approxPolyDP()`.

### Example

```python
approx = cv2.approxPolyDP(
    contour,
    0.01 * cv2.arcLength(contour, True),
    True
)
```

This reduces the number of points while preserving the overall shape.

---

# Shape Detection

The number of corner points obtained from the approximated contour was used to identify different shapes.

Examples:

* **3 corners** → Triangle
* **4 corners** → Rectangle
* **5 corners** → Polygon
* **More than 5 corners** → Circle

---

# Shape Labeling

After detecting the shape, its name was displayed on the image using `cv2.putText()`.

### Example

```python
cv2.putText(
    img,
    shape_name,
    (x, y),
    cv2.FONT_HERSHEY_COMPLEX,
    0.6,
    (0, 255, 0),
    2
)
```

---

## Applications

Contour detection and shape recognition are widely used in:

* Object Detection
* Image Segmentation
* Industrial Quality Inspection
* Traffic Sign Recognition
* Robotics
* Medical Image Analysis
* Document Processing

---

## What I Learned Today

* Learned how to detect contours in an image using OpenCV.
* Converted images to grayscale before processing.
* Applied binary thresholding to separate objects from the background.
* Detected object boundaries using `findContours()`.
* Simplified contour shapes using `approxPolyDP()`.
* Identified geometric shapes based on the number of detected corners.
* Displayed detected shape names directly on the image.
