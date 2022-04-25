import pyttsx3

speaker = pyttsx3.init()
speaker.setProperty('rate', 150)

def talk(text):
    print("Transcript: ", text)
    speaker.say(text)
    speaker.runAndWait()
