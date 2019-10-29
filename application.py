from events import Events

import config
from logic.agent.agent import Agent
from logic.model import Grid
from logic.model import Keyboard
from logic.model import CLI

__events__ = Events()
__event_dict__ = {
    'on_reset': __events__.on_reset
}


def reset():
    __events__.on_reset(None)


def bind(**kwargs):
    for key, value in kwargs.items():
        __event_dict__[key] += value


grid = Grid(config.KEYBOARD_WIDTH, config.KEYBOARD_HEIGHT, config.COLUMN_COUNT, config.ROW_COUNT)
keyboard = Keyboard(config.SYMBOLS, config.BUTTON_WIDTH, config.BUTTON_HEIGHT, config.KEYBOARD_WIDTH, config.KEYBOARD_HEIGHT)
agent = Agent(keyboard, grid, config.ACTION_TYPES)
cli = CLI(config.CLI_HEIGHT) if config.ENABLE_CLI else None
