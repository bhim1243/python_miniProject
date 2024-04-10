import cv2
import numpy as np
import pyttsx3
import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        transcript = r.recognize_google(audio)
        print(f"You said: {transcript}")
        return transcript
    except Exception as e:
        print("Speech recognition failed:", e)
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def object_detection():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Object detection code using OpenCV and a pre-trained model
        # You can add your object detection logic here

        cv2.imshow('Object Detection', frame)

        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    while True:
        print("Press Enter to start object detection and speech recognition...")
        # Wait for Enter key press
        while True:
            if cv2.waitKey(1) == 13:  # 13 is the Enter key code
                break

        object_detection()

        try:
            command = recognize_speech().lower()
            speak(f"You said: {command}")
        except Exception as e:
            print("Speech recognition failed:", e)

        if input("Do you want to continue? (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    main()
