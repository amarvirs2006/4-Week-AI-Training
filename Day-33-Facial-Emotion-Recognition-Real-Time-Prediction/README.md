# Day 33 – Facial Emotion Recognition Real-Time Prediction

Today, I completed the OpenCV implementation of my **Facial Emotion Recognition** project. I integrated the trained CNN model with OpenCV to perform **real-time emotion detection** using a webcam. The application detects faces, preprocesses the detected face, predicts the emotion using the trained model, and displays the predicted emotion on the live video feed.

## Project Title

**Facial Emotion Recognition**

---

## Topics Learned

* Loading a Trained CNN Model
* OpenCV Haar Cascade Classifier
* Webcam Integration
* Face Detection
* Image Preprocessing
* Emotion Prediction
* Displaying Emotion Labels
* Real-Time Emotion Recognition

---

# Loading the Trained Model

The CNN model trained on the FER-2013 dataset was loaded using TensorFlow.

### Example

```python
model = tf.keras.models.load_model("models/emotion_model.keras")
```

This model is used to predict the emotion of detected faces.

---

# Emotion Labels

The model predicts one of seven facial emotions.

The emotion classes are:

* Angry
* Disgust
* Fear
* Happy
* Neutral
* Sad
* Surprise

---

# Face Detection using Haar Cascade

OpenCV's Haar Cascade Classifier was used to detect human faces in each webcam frame.

### Example

```python
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)
```

This classifier identifies the location of faces before emotion prediction.

---

# Webcam Integration

The webcam was accessed using OpenCV to capture live video.

### Example

```python
camera = cv2.VideoCapture(0)
```

Frames are continuously captured until the user exits the application.

---

# Face Preprocessing

Each detected face was prepared before passing it to the CNN model.

The preprocessing steps included:

* Cropping the detected face
* Resizing the face to **48 × 48** pixels
* Converting image values to floating-point format
* Adding a batch dimension

These steps ensure that the input matches the format expected by the trained model.

---

# Emotion Prediction

The preprocessed face image was passed to the CNN model to predict the facial emotion.

### Example

```python
prediction = model.predict(face, verbose=0)

emotion = emotion_labels[np.argmax(prediction)]
```

The class with the highest probability is selected as the predicted emotion.

---

# Displaying Results

A rectangle was drawn around the detected face, and the predicted emotion label was displayed above it using OpenCV.

### Example

```python
cv2.putText(
    frame,
    emotion,
    (x, y-10),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0,255,0),
    2
)
```

This provides real-time visual feedback during webcam prediction.

---

## Applications

Real-time facial emotion recognition can be used in:

* Human–Computer Interaction
* Smart Surveillance Systems
* Healthcare Monitoring
* Online Learning Platforms
* Customer Experience Analysis
* Driver Monitoring Systems
* Interactive AI Applications

---

## What I Learned Today

* Loaded a trained CNN model for emotion recognition.
* Integrated OpenCV with the deep learning model.
* Detected faces using the Haar Cascade Classifier.
* Captured live video from the webcam.
* Preprocessed detected faces before prediction.
* Predicted facial emotions in real time.
* Displayed emotion labels on the live webcam feed.
* Completed the OpenCV implementation of the Facial Emotion Recognition project.
