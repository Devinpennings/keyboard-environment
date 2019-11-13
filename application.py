import json
import sys
import os
from pathlib import Path

from events import Events

from . import config
from .logic.agent import Agent
from .logic.model import *

__events = Events()
__event_dict = {
    'on_keyboard_change': __events.on_keyboard_change,
}


def bind(**kwargs):
    for key, value in kwargs.items():
        __event_dict[key] += value


root_path = Path().absolute()
grid = Grid(config.KEYBOARD_WIDTH, config.KEYBOARD_HEIGHT, config.COLUMN_COUNT, config.ROW_COUNT)

keyboard = None


def set_keyboard(new):
    global keyboard
    keyboard = new
    __events.on_keyboard_change()


def init_keyboard():
    global keyboard
    if len(sys.argv) > 2:
        _file = open(f'{config.KEYBOARD_PATH}/{config.KEYBOARD_NAME}.json')
        _template = json.load(_file)
        set_keyboard(Keyboard.from_template(_template))
    else:
        set_keyboard(Keyboard.from_symbols(config.KEYBOARD_WIDTH,
                                         config.KEYBOARD_HEIGHT,
                                         config.BUTTON_WIDTH,
                                         config.BUTTON_HEIGHT,
                                         config.SYMBOLS))


init_keyboard()

agent = Agent(grid, config.ACTION_TYPES)
cli = CLI(config.CLI_HEIGHT) if config.ENABLE_CLI else None
text = Text()
