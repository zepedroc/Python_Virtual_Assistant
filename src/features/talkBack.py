import os
import sys
import random
from gtts import gTTS
from playsound import playsound


def talk(text):
    audio_info = gTTS(text, lang='pt')
    randomNum = random.randint(0, 50000)
    audio_info.save(f'audio{randomNum}.mp3')
    playsound(f'audio{randomNum}.mp3')
    os.remove(f'audio{randomNum}.mp3')


hello_options = ['Olá! O que posso fazer por ti?',
                 'Boas, tudo bem?', 'Olá, estás de volta!']

goodbye_options = ['Adeus, até à próxima!',
                   'Entendido. Tchau Tchau', 'Falamos depois então. Com licença.']


def hello():
    talk(random.choice(hello_options))


def closeAssistant():
    talk(random.choice(goodbye_options))
    sys.exit(0)
