import datetime

from features.talkBack import talk


def currentTime():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk("São neste momento " + time)
