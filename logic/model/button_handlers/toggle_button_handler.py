from .one_time_button_handler import OneTimeButtonHandler


class ToggleButtonHandler(OneTimeButtonHandler):

    def __init__(self, keyboard=None, modifier=None):
        super().__init__(keyboard, modifier)
        self.toggle_only = True
