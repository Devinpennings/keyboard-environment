import json
from threading import Thread
from time import sleep

from ...agent import ActionTypes
from ..keyboard_modifiers import modifiers
from .... import application
from .base_button_handler import BaseButtonHandler


class OneTimeButtonHandler(BaseButtonHandler):

    def __init__(self, keyboard=None, modifier=None):
        self.active = False
        self.keyboard_template = keyboard
        self.keyboard = None
        self.toggle_only = False
        self.origin = None
        if modifier:
            self.modifier = modifiers[modifier]()

    def load(self):
        from .. import Keyboard
        file = open(f'{application.root_path}/keyboards/{self.keyboard_template}.json')
        template = json.load(file)
        new = Keyboard.from_template(template)
        if new.name == application.keyboard.name:
            self.keyboard = application.keyboard
        else:
            self.keyboard = new

    def handle(self, obj, action):
        if self.active:
            self.reset(ActionTypes.CLICK.duration)
            return

        if not self.keyboard:
            self.load()

        if self.modifier:
            self.keyboard = self.modifier.modify(self.keyboard)

        self.origin = application.keyboard
        self.set_keyboard_timeout(self.keyboard, action.duration)

        def on_touch(touched, action_type):
            if not self.toggle_only and touched != obj:
                self.reset(action_type.duration)

        self.active = True
        application.keyboard.bind(on_touch=on_touch)

    def reset(self, duration):
        if self.modifier:
            self.keyboard = self.modifier.reverse(self.keyboard)
            self.set_keyboard_timeout(self.keyboard, duration)
        else:
            self.set_keyboard_timeout(self.origin, duration)
        self.active = False

    def set_keyboard_timeout(self, keyboard, timeout):
        def execute_wait(duration):
            sleep(duration)
            application.set_keyboard(keyboard)

        thread = Thread(target=execute_wait, args=[timeout])
        thread.start()
