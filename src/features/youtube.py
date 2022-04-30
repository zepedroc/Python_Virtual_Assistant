import pywhatkit
import speech_recognition

from features.talkBack import talk
from features.handleKeyboard import handleKey

listener = speech_recognition.Recognizer()


def handleUserRequest():
    global listener
    with speech_recognition.Microphone() as mic:
        listener.adjust_for_ambient_noise(mic, duration=0.5)
        audio = listener.record(mic, 3)
        command = listener.recognize_google(audio)
        return command.lower()


def openYoutube():
    talk('What do you want me to put on?')
    requestedVideo = handleUserRequest()
    pywhatkit.playonyt(requestedVideo)
    talk('Playing: ' + requestedVideo)


def nextYoutubeVideo():
    handleKey('n', 'Shift')
