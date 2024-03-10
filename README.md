# Hand Tracking and Mouse Control with OpenCV, MediaPipe, and PyAutoGUI

This Python program allows you to control the mouse cursor and perform clicks using hand gestures detected from a video feed captured by a camera. It utilizes OpenCV for video capturing and processing, MediaPipe for hand detection, and PyAutoGUI for mouse control.

## Requirements

- Python 3.x
- OpenCV (`opencv-python` package)
- MediaPipe (`mediapipe` package)
- PyAutoGUI (`pyautogui` package)

You can install the required packages using pip:
pip install opencv-python mediapipe pyautogui


## How to Use

1. Clone or download this repository to your local machine.
2. Make sure you have a webcam connected to your computer.
3. Navigate to the directory where the program files are located.
4. Run the `main.py` script:

5. A window will appear showing the video feed from your webcam. Place your hand in front of the camera.
6. Move your index finger to control the mouse cursor. The cursor will follow the movement of your index finger.
7. Lift your middle finger to perform a click. A green circle will appear on the screen to indicate that a click has been performed.
8. To exit the program, press the 'q' key on your keyboard.

## Troubleshooting

- If the program does not detect your hand or fingers accurately, try adjusting the lighting conditions or the position of your hand relative to the camera.
- If the mouse cursor moves erratically or the clicks are not performed correctly, try adjusting the sensitivity thresholds in the code (`abs(newX - prevX)` and `abs(newY - prevY)`).
