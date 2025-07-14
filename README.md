# Eye Blink Detection with MediaPipe and OpenCV

This project implements a simple real-time eye state detection system (open or closed) using **MediaPipe** and **OpenCV** libraries, based on the Eye Aspect Ratio (EAR) calculation to detect blinking.

---

## Features

- Real-time video capture via webcam.
- Facial landmark detection using MediaPipe's FaceMesh model.
- Calculation of Eye Aspect Ratio (EAR) for each eye.
- Visual classification of eye state (open or closed) based on EAR.
- Display of eye landmarks and status overlay on the video feed.

---

## How to Use

### Requirements

- Python 3.x
- OpenCV
- MediaPipe
- SciPy

### Install dependencies

```bash
pip install opencv-python mediapipe scipy
````

### Running the script

1. Connect a webcam to your computer (or use the built-in webcam).
2. Run the Python script:

```bash
python your_script_name.py
```

3. A window will open showing the webcam video with eye detection and status ("EYES OPEN" or "EYES CLOSED").
4. Press the `ESC` key to exit.

---

## Technical Details

* EAR is calculated as the ratio between vertical and horizontal distances between specific eye landmarks.
* Eye landmarks are extracted from MediaPipe's FaceMesh.
* A fixed threshold of 0.2 is used to classify eyes as open or closed, adjustable based on environment and user.

---

## References

* Soukupová, T. & Čech, J. (2016). Real-Time Eye Blink Detection using Facial Landmarks.
* MediaPipe FaceMesh Documentation: [https://google.github.io/mediapipe/solutions/face\_mesh.html](https://google.github.io/mediapipe/solutions/face_mesh.html)
* OpenCV Documentation: [https://opencv.org/](https://opencv.org/)

---

## License

This project is licensed under the MIT License. Feel free to use and modify it according to your needs.

---




