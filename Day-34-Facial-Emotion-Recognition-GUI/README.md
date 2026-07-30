# Day 34 – Facial Emotion Recognition GUI

Today, I completed the graphical user interface (GUI) for my **Facial Emotion Recognition** project using **CustomTkinter**. The GUI provides a modern desktop application where users can start the webcam, detect emotions in real time, view prediction confidence for each emotion, monitor FPS, and save image snapshots.

The application integrates the trained CNN model with OpenCV and presents the results through an interactive interface.

## Project Title

**Facial Emotion Recognition**

---

## Topics Learned

* CustomTkinter GUI
* Desktop Application Development
* Live Webcam Feed
* Real-Time Emotion Detection
* Emotion Confidence Bars
* FPS Counter
* Snapshot Saving
* Background Threading
* User Interface Design

---

# CustomTkinter

The graphical interface was developed using **CustomTkinter**, which provides modern widgets and an improved appearance compared to the standard Tkinter library.

The application includes:

* Live camera display
* Control buttons
* Emotion display section
* Confidence bars
* FPS display
* Status messages

---

# Loading the Trained Model

The trained CNN model was loaded when the application started and used for real-time emotion prediction.

---

# Live Webcam Feed

The GUI allows users to start and stop the webcam. Video frames are continuously captured and processed for emotion detection.

---

# Real-Time Emotion Detection

For every detected face:

* The face is detected using the Haar Cascade classifier.
* The face image is resized to the required input size.
* The trained CNN model predicts the facial emotion.
* The predicted emotion is displayed on both the webcam feed and the GUI.

---

# Emotion Confidence Bars

The application displays confidence scores for all seven emotions using progress bars, allowing users to see the prediction probability for each emotion.

---

# FPS Counter

The application calculates and displays the current Frames Per Second (FPS), providing an indication of the real-time performance of the system.

---

# Snapshot Saving

Users can save snapshots of the webcam feed directly from the application. Captured images are stored automatically for future reference.

---

# Background Threading

Camera capture and model inference are executed in a separate background thread to ensure that the graphical interface remains responsive during real-time prediction.

---

# User-Friendly Interface

The GUI provides several interactive features:

* Start/Stop Camera
* Live Video Preview
* Real-Time Emotion Display
* Emotion Confidence Visualization
* FPS Monitoring
* Snapshot Capture
* Status Indicator

---

## What I Learned Today

* Developed a desktop GUI using CustomTkinter.
* Integrated the trained CNN model into the graphical application.
* Displayed a live webcam feed within the interface.
* Performed real-time facial emotion prediction.
* Visualized confidence scores using progress bars.
* Displayed FPS for monitoring application performance.
* Added snapshot saving functionality.
* Used background threading to keep the GUI responsive.
* Completed the user interface for the Facial Emotion Recognition project.
