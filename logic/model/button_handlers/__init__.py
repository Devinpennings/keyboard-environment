from .toggle_button_handler import ToggleButtonHandler
from .value_append_handler import ValueAppendHandler
from .one_time_button_handler import OneTimeButtonHandler

handlers = {
    'ValueAppendHandler': ValueAppendHandler,
    'OneTimeButtonHandler': OneTimeButtonHandler,
    'ToggleButtonHandler': ToggleButtonHandler
}


def get_handler(k):
    if k in handlers:
        return handlers[k]
    raise NotImplementedError(f'Handler {k} is not implemented')
