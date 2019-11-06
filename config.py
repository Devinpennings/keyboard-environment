from . import application_mode
from .logic.agent import ActionType

SYMBOLS = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a','s', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"','enter' ,'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']

COLUMN_COUNT = 12
ROW_COUNT = 3

KEYBOARD_WIDTH = 600
KEYBOARD_HEIGHT = 150

BUTTON_WIDTH = 50
BUTTON_HEIGHT = 50

ACTION_TYPES = [ActionType.CLICK]

ENABLE_CLI = True
CLI_HEIGHT = 128

APPLICATION_MODE = application_mode.ApplicationMode.GRAPHIC