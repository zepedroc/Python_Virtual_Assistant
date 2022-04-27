
import screen_brightness_control as screen


def increaseBrightness():
    currentBrightness = screen.get_brightness()
    screen.set_brightness(currentBrightness[0] + 10)


def decreaseBrightness():
    currentBrightness = screen.get_brightness()
    screen.set_brightness(currentBrightness[0] - 10)
