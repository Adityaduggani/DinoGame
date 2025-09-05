# 🦖 Dino Game with Hand Gesture Control (DirectKeys)

Play the **Google Chrome Dino Game** using **hand gestures** with low-level keyboard input!  
This version uses **DirectKeys** (`ctypes` + Windows API) instead of PyAutoGUI, so the controls are faster and more reliable for games.

---

## 🚀 Features
- Real-time hand tracking with webcam.
- Control Dino using gestures:
  - Raise hand → Jump (SPACE key).
  - Lower hand → Duck (DOWN arrow).
- Uses **DirectKeys** (Windows API) for accurate keypress simulation.

---

## 🛠 Tech Stack
- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/) – capture video
- [MediaPipe](https://developers.google.com/mediapipe) – hand tracking
- **DirectKeys (ctypes)** – low-level keyboard input

---

## 📂 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/dino-hand-directkeys.git
   cd dino-hand-directkeys
