from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from ... import application
from .cli import CLI
from .keyboard import Keyboard

TEXT_INPUT_HEIGHT = 64
CLI_HEIGHT = 128


class MainScreen(BoxLayout):

    def __init__(self):
        super().__init__(orientation='vertical')

        if application.cli:
            Window.size = (application.grid.width, application.grid.height + TEXT_INPUT_HEIGHT + CLI_HEIGHT)
        else:
            Window.size = (application.grid.width, application.grid.height + TEXT_INPUT_HEIGHT)

        keyboard = Keyboard()
        keyboard.height = application.grid.height
        keyboard.width = application.grid.width

        text_input = TextInput()
        text_input.keyboard_mode = 'managed'
        text_input.is_focusable = False
        text_input.height = TEXT_INPUT_HEIGHT
        text_input.size_hint = (1, None)

        def text_change(value):
            text_input.text = value
        application.text.bind(on_change=text_change)

        def text_reset():
            text_input.text = ""
        application.text.bind(on_reset=text_reset)

        self.add_widget(text_input)
        self.add_widget(keyboard)

        if application.cli:
            cli = CLI()
            cli.height = application.cli.height
            cli.size_hint = (1, None)
            self.add_widget(cli)
