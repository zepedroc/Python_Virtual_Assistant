import sys
import os

# getting the name of the directory
# where this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from controls.keyboard import pressKey, simulateTyping


def handleKey(key, hold=''):
    pressKey(key, hold)


def handleTyping(text):
    simulateTyping(text)
