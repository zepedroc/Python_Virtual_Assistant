import pywhatkit
from convertSpeech import handleRequest
from talkBack import talk


def runVoiceAssistant():
    command = handleRequest()
    if 'play' in command:
        command = command.replace('play', '')
        talk('Playing ' + command)
        pywhatkit.playonyt(command)


runVoiceAssistant()
