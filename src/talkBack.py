import pyttsx3

engine = pyttsx3.init()


def talk(text):
    print("Transcript: ", text)
    engine.say(text)
    engine.runAndWait()
