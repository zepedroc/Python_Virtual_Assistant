import pyjokes

from features.talkBack import talk


def tellJoke():
    talk(pyjokes.get_joke('en', 'all'))
