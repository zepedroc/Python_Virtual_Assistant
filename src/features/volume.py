from handleKeyboard import handleKey


def increaseVolume():
    for _ in range(5):
        handleKey('Volume UP')


def decreaseVolume():
    for _ in range(5):
        handleKey('Volume DOWN')


def mute():
    handleKey('Mute')
