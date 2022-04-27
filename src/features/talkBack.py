import sys
import pyttsx3
import random

hello_options = ['Hello! What can I do for you?',
                 'Hey there!', 'Hi! How are you?']
goodbye_options = ['Goodbye!', 'Bye! See you next time.', 'Until next time!']

speaker = pyttsx3.init()

# change the voice speed
speaker.setProperty('rate', 150)

# change the voice itself
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[2].id)


def talk(text):
    print("Transcript: ", text)
    speaker.say(text)
    speaker.runAndWait()


def hello():
    talk(random.choice(hello_options))


def closeAssistant():
    talk(random.choice(goodbye_options))
    sys.exit(0)
