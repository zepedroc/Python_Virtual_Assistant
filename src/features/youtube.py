import pywhatkit

from features.talkBack import talk
import speech_recognition

listener = speech_recognition.Recognizer()


def handleUserRequest():
    global listener
    with speech_recognition.Microphone() as mic:
        listener.adjust_for_ambient_noise(mic, duration=1)
        audio = listener.record(mic, 5)
        command = listener.recognize_google(audio)
        return command.lower()


def openYoutube():
    talk('What do you want me to put on?')
    requestedVideo = handleUserRequest()
    pywhatkit.playonyt(requestedVideo)
    talk('Playing: ' + requestedVideo)
