import speech_recognition

from talkBack import talk

listener = speech_recognition.Recognizer()


def handleRequest():
    try:
        with speech_recognition.Microphone() as mic:
            print('Listening...')
            listener.adjust_for_ambient_noise(mic, duration=1)
            audio = listener.listen(mic)
            command = listener.recognize_google(audio)
            print('Command--- ', command)

    except:
        talk("I didn't understand your request")

    return command.lower()
