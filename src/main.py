from features.camera import openCamera
from features.talkBack import closeAssistant, hello
from features.time import currentTime
from features.volume import decreaseVolume, increaseVolume
from features.youtube import openYoutube, nextYoutubeVideo
from features.talkBack import talk
from data.patterns import helloPatterns, goodbyePatterns, cameraPatterns, youtubePatterns, louderPatterns, lowerVolPatterns, currentTimePatterns, nextPatterns

import speech_recognition

listener = speech_recognition.Recognizer()


def command_belongs(command, array):
    for i in range(0, len(array)):
        if array[i] in command:
            return True
    return False


def receiveCommand():
    global listener
    with speech_recognition.Microphone() as mic:
        listener.adjust_for_ambient_noise(mic, duration=0.5)
        audio = listener.record(mic, duration=3)
        command = listener.recognize_google(audio, language="pt-PT")
        return command.lower()


def handleUserRequest():
    command = receiveCommand()
    print('Pedido: ', command)
    if command_belongs(command, helloPatterns):
        hello()
    if command_belongs(command, goodbyePatterns):
        closeAssistant()
    if command_belongs(command, cameraPatterns):
        openCamera()
    if command_belongs(command, youtubePatterns):
        openYoutube()
    if command_belongs(command, louderPatterns):
        increaseVolume()
    if command_belongs(command, lowerVolPatterns):
        decreaseVolume()
    if command_belongs(command, currentTimePatterns):
        currentTime()
    if command_belongs(command, nextPatterns):
        nextYoutubeVideo()

    print('----Não reconhecido----')


def runVirtualAssistant():
    talk('Initializing...')
    while True:
        global listener
        try:
            handleUserRequest()
        except speech_recognition.UnknownValueError:
            listener = speech_recognition.Recognizer()


runVirtualAssistant()
