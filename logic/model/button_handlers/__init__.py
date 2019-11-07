from .value_append_handler import ValueAppendHandler
from .one_time_keyboard_handler import OneTimeKeyboardHandler

handlers = {
    'ValueAppendHandler': ValueAppendHandler,
    'OneTimeKeyboardHandler': OneTimeKeyboardHandler
}


def get_handler(k):
    if k in handlers:
        return handlers[k]
    raise NotImplementedError(f'Handler {k} is not implemented')
