import re

from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

import application


class CLI(BoxLayout):

    def __init__(self):
        super().__init__(orientation='vertical')

        self.text_input = TextInput()
        self.text_input.height = 32
        self.text_input.size_hint = (1, None)
        self.text_input.multiline = False
        self.text_input.pos_hint = {'top': 1}
        self.text_input.bind(on_text_validate=self.on_submit)

        self.text_output = TextInput()
        self.text_output.size_hint = (1, 1)
        self.text_output.keyboard_mode = 'managed'
        self.text_output.cursor = False

        self.add_widget(self.text_input)
        self.add_widget(self.text_output)

        self.show_keyboard(None)

    def on_submit(self, instance):
        text = instance.text

        if text:
            self.text_input.text = ""
            parsed = text.split(' ')
            command = parsed[0]
            args = parsed[1:]

            result = application.cli.execute(command, *args)

            if result:
                if self.text_output.text != "":
                    result = '\n' + result
                self.text_output.text = self.text_output.text + result

        Clock.schedule_once(self.show_keyboard)

    def show_keyboard(self, event):
        self.text_input.focus = True

