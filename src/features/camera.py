from time import sleep
from features.handleKeyboard import handleKey, handleTyping


def openCamera():
    handleKey('Windows')
    sleep(1)
    handleTyping('camera')
    sleep(1)
    handleKey('Enter')


# take selfie