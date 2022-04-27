from time import sleep
from pynput.keyboard import Key, Controller

keyboard = Controller()

# with keyboard.pressed(Key.shift):
#     keyboard.tap('a')


def simulateTyping(text):
    for char in text:
        keyboard.tap(char)
        sleep(0.1)


def pressKey(key, hold=''):
    if hold == 'Shift':
        with keyboard.pressed(Key.shift):
            keyboard.tap(key)

    if key == 'Windows':
        keyboard.tap(Key.cmd)
    if key == 'Enter':
        keyboard.tap(Key.enter)
    if key == 'Volume UP':
        keyboard.tap(Key.media_volume_up)
    if key == 'Volume DOWN':
        keyboard.tap(Key.media_volume_down)
    if key == 'Mute':
        keyboard.tap(Key.media_volume_mute)
