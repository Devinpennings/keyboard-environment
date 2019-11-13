import json

from .... import application
from .base_button_handler import BaseButtonHandler


class OneTimeKeyboardHandler(BaseButtonHandler):

    def __init__(self, keyboard):
        self.keyboard = keyboard

    def handle(self, obj, action):
        from .. import Keyboard
        file = open(f'{application.config.KEYBOARD_PATH}/{self.keyboard}.json')
        template = json.load(file)

        origin = application.keyboard

        application.set_keyboard(Keyboard.from_template(template))

        def reset(_obj):
            application.set_keyboard(origin)

        application.text.bind(on_change=reset)
