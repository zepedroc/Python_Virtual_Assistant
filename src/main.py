import pywhatkit
from convertSpeech import handleRequest
from talkBack import talk
import datetime
import pyjokes


def runVoiceAssistant():
    command = handleRequest()
    if 'play' in command:
        command = command.replace('play', '')
        talk('Playing ' + command)
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("Right now it's " + time)
    elif 'joke' in command:
        generatedJoke = pyjokes.get_joke()
        talk(generatedJoke)


runVoiceAssistant()
