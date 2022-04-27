from features.jokes import tellJoke
from features.talkBack import closeAssistant, hello
from features.time import currentTime
from features.youtube import openYoutube

from features.talkBack import talk
from neuralintents import GenericAssistant
import speech_recognition

listener = speech_recognition.Recognizer()


def handleUserRequest():
    global listener
    with speech_recognition.Microphone() as mic:
        listener.adjust_for_ambient_noise(mic, duration=1)
        audio = listener.listen(mic)
        
        
        # quando chamares o nome dele dá-lhe apenas 5seg para ouvir
        # audio = listener.record(mic, 5)
        command = listener.recognize_google(audio)
        return command.lower()


def runVirtualAssistant():
    talk('Initializing...')
    while True:
        global listener
        try:
            command = handleUserRequest()

            print('Command: ', command)
            assistant.request(command)

        except speech_recognition.UnknownValueError:
            talk("Can you repeat?")
            listener = speech_recognition.Recognizer()


mappings = {
    'greetings': hello,
    'goodbye': closeAssistant,
    'youtube': openYoutube,
    'time': currentTime,
    'joke': tellJoke,
}

assistant = GenericAssistant('./resources/intents.json',
                             intent_methods=mappings)
# assistant.train_model()
# assistant.save_model('Model/NeuralNine Model')
assistant.load_model('Model/NeuralNine Model')

runVirtualAssistant()
