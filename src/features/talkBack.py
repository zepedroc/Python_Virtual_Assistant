import sys
import pyttsx3

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)


def talk(text):
    print("Transcript: ", text)
    speaker.say(text)
    speaker.runAndWait()


def hello():
    talk('Hello! What can I do for you?')


def closeAssistant():
    talk('Goodbye! See you next time.')
    sys.exit(0)
