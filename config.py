from . import application_mode
from .logic.agent import ActionTypes

KEYBOARD_PATH = 'C:\\Users\\Devin\\Documents\\School\\Semester 7\\HERE\\keyboard_environment\\keyboards'
KEYBOARD_NAME = "default"

ENABLE_CLI = True
CLI_HEIGHT = 128

APPLICATION_MODE = application_mode.ApplicationMode.GRAPHIC

SYMBOLS = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';'
]

BUTTON_WIDTH = 50
BUTTON_HEIGHT = 50

COLUMN_COUNT = 24
ROW_COUNT = 4

KEYBOARD_WIDTH = 762
KEYBOARD_HEIGHT = 200

ACTION_TYPES = [ActionTypes.CLICK]

