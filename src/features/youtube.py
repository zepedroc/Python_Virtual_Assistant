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
    talk('O que queres que ponha a dar?')
    requestedVideo = handleUserRequest()
    pywhatkit.playonyt(requestedVideo)
    talk('A iniciar' + requestedVideo)


def nextYoutubeVideo():
    handleKey('n', 'Shift')
