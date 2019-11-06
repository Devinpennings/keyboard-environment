from ... import application
from .keyboard_button import KeyboardButton
from .rectangle import Rectangle


class Keyboard:

    def __init__(self, symbols, button_width, button_height, width, heigth):
        self.symbols = symbols
        self.width = width
        self.height = heigth
        self.button_width = button_width
        self.button_height = button_height
        self.buttons = []
        self.initialize()
        self.value = ""

        def on_reset(obj):
            self.value = ""

        application.bind(on_reset=on_reset)

    def initialize(self):

        i = 0
        c_count = 0
        r_count = 0
        columns = self.width / self.button_width

        for s in self.symbols:
            button = KeyboardButton(s, Rectangle(
                self.button_width,
                self.button_height,
                c_count * self.button_width,
                r_count * self.button_height))

            c_count += 1
            if c_count == columns:
                r_count += 1
                c_count = 0

            def on_button_click(obj, duration):
                self.value += obj.symbol

            button.bind(on_click=on_button_click)

            self.buttons.append(button)
            i += 1

    def get_button(self, x, y):
        matches = [b for b in self.buttons if b.intersects(x, y)]
        return matches[0] if len(matches) > 0 else None
