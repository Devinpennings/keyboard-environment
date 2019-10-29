from . import application_mode
from .logic.agent import ActionType

SYMBOLS = ['a', 'b', 'c', '@']

COLUMN_COUNT = 12
ROW_COUNT = 3

KEYBOARD_WIDTH = 300
KEYBOARD_HEIGHT = 80

BUTTON_WIDTH = 50
BUTTON_HEIGHT = 50

ACTION_TYPES = [ActionType.CLICK]

ENABLE_CLI = True
CLI_HEIGHT = 128

APPLICATION_MODE = application_mode.ApplicationMode.API
