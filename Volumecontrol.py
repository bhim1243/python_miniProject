import cv2
import mediapipe as mp
import numpy as np
import math
import pyautogui

# Initialize MediaPipe hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open webcam
cap = cv2.VideoCapture(0)

# Initialize variables for storing previous hand positions
prev_x, prev_y = 0, 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect hands in the frame
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmarks
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

            # Calculate the distance moved by the hand
            distance = math.sqrt((cx - prev_x) ** 2 + (cy - prev_y) ** 2)

            # If the hand is moved upwards, increase the volume
            if cy < prev_y:
                pyautogui.press('volumeup')

            # If the hand is moved downwards, decrease the volume
            elif cy > prev_y:
                pyautogui.press('volumedown')

            # Update previous hand position
            prev_x, prev_y = cx, cy

    # Display the output frame
    cv2.imshow('Gesture Volume Control', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the capture and destroy any OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Release MediaPipe hands instance
hands.close()
