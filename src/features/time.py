import datetime

from features.talkBack import talk


def currentTime():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk("It's currently " + time)
