import os
import subprocess
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import psutil

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Change index to select different voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-us')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Could not understand audio")
        return "None"
    return query

def open_application(app_name):
    try:
        subprocess.Popen(app_name)
    except Exception as e:
        speak(f"Sorry, I couldn't open {app_name}. Make sure it's installed on your system.")

def check_system_info():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    speak(f"The system is currently at {percent} percent battery.")
    if plugged:
        speak("The system is currently plugged in and charging.")
    else:
        speak("The system is currently not plugged in.")

def assistant():
    greet()
    speak("How can I assist you today?")
    while True:
        query = listen().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get().open("https://www.youtube.com")
        elif 'open chatgpt' in query:
            webbrowser.get().open("https://chat.openai.com/")

        elif 'open google' in query:
            webbrowser.get().open("https://www.google.com")

        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {time}")

        elif 'shutdown' in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 1")

        elif 'word' in query:
            speak("Open Microsoft Word")
            open_application("winword")

        elif 'powerpoint' in query:
            speak("Open PowerPoint")
            open_application("powerpoint")

        elif 'excel' in query:
            speak("Open Excel")
            open_application("excel")

        elif 'settings' in query:
            speak("Opening Settings")
            open_application("ms-settings:")

        elif 'log out' in query:
            speak("Logging out the user")
            os.system("shutdown -l")

        elif 'open' in query:
            app_name = query.split('open', 1)[-1].strip()  # Extract the application name
            open_application(app_name)

        elif 'system info' in query:
            check_system_info()

        elif 'quit' in query or 'exit' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    assistant()
