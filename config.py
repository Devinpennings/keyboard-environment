from . import application_mode
from .logic.agent import ActionTypes

SYMBOLS = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';',
    '"', 'enter', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/'
]

KEYBOARD_PATH = '/home/devin/Documents/Semester 7/HERE/keyboard_environment/keyboards'
KEYBOARD_NAME = "default"

COLUMN_COUNT = 24
ROW_COUNT = 4

KEYBOARD_WIDTH = 762
KEYBOARD_HEIGHT = 200

BUTTON_WIDTH = 50
BUTTON_HEIGHT = 50

ACTION_TYPES = [ActionTypes.CLICK]

ENABLE_CLI = True
CLI_HEIGHT = 128

APPLICATION_MODE = application_mode.ApplicationMode.GRAPHIC
