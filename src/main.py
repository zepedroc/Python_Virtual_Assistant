import sys
import pywhatkit
from talkBack import talk
import datetime
import pyjokes
from neuralintents import GenericAssistant
import speech_recognition


def closeAssistant():
    talk('Goodbye! See you next time.')
    sys.exit(0)


def hello():
    talk('Hello! What can I do for you?')


def openYoutube():
    talk('What video do you want me to put on?')
    # requestedVideo = handleRequest()
    # pywhatkit.playonyt(requestedVideo)
    # talk('Playing: ' + requestedVideo)


listener = speech_recognition.Recognizer()


def runVoiceAssistant():
    talk('Initializing...')
    while True:
        global listener
        try:
            with speech_recognition.Microphone() as mic:
                listener.adjust_for_ambient_noise(mic, duration=1)
                audio = listener.listen(mic)
                command = listener.recognize_google(audio)
                command = command.lower()

                print('Command: ', command)
                assistant.request(command)
            # elif 'time' in command:
            #     time = datetime.datetime.now().strftime('%I:%M %p')
            #     talk("Tt's currently" + time)
            # elif 'joke' in command:
            #     generatedJoke = pyjokes.get_joke()
            #     talk(generatedJoke)
            # else:
            #     talk("I didn't understand your request. Can you please repeat?")

        except speech_recognition.UnknownValueError:
            talk("I didn't understand your request. Can you please repeat?")
            listener = speech_recognition.Recognizer()


mappings = {
    'greetings': hello,
    'goodbye': closeAssistant,
    'youtube': openYoutube,
}

assistant = GenericAssistant('./resources/intents.json',
                             intent_methods=mappings)
# assistant.train_model()
# assistant.save_model('Model/NeuralNine Model')
assistant.load_model('Model/NeuralNine Model')

runVoiceAssistant()
