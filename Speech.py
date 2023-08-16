import speech_recognition as sr
import os

# Initialize the microphone instance
microphone = sr.Microphone()

# Using the microphone context manager
with microphone as source:
    recognizer = sr.Recognizer()
    print("Listening... Say something:")
    audio = recognizer.listen(source)

# Now you can perform speech recognition on the captured audio
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)

    # Custom commands based on recognized text
    if "open browser" in text:
        os.system("start https://www.google.com")
    elif "play music" in text:
        os.system("start your_music_file.mp3")
    # Add more commands here

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; check your network connection:", e)
