import os
import cv2
import numpy as np
import pygame
import time

# Function to load the alarm sound with error checking
def load_alarm_sound(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"No such file: {file_path}")
    return pygame.mixer.Sound(file_path)

# Initialize Pygame for playing sounds
pygame.mixer.init()

# Specify the path to the alarm sound file
alarm_sound_path = 'D:/python_miniProject/alarm.wav'

# Load alarm sound with error checking
try:
    alarm_sound = load_alarm_sound(alarm_sound_path)
except FileNotFoundError as e:
    print(e)
    exit()


# Load Haar cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return len(faces) > 0

def motion_detection(video_source=0, threshold=1000):
    cap = cv2.VideoCapture(video_source)
    ret, frame1 = cap.read()
    alarm_active = False
    while True:
        ret, frame2 = cap.read()
        face_detected = detect_face(frame2)
        if face_detected:
            alarm_active = True
        else:
            alarm_active = False

        if alarm_active:
            cv2.putText(frame2, "ALARM ON", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            alarm_sound.play()
        else:
            cv2.putText(frame2, "ALARM OFF", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            alarm_sound.stop()
        cv2.imshow("Security Feed", frame2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    motion_detection()
