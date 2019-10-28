import application
from logic.model import KeyboardButton, Rectangle


class Keyboard:

    def __init__(self, symbols, button_width, button_height):
        self.symbols = symbols
        self.button_width = button_width
        self.button_height = button_height
        self.buttons = []
        self.initialize()
        self.value = ""

        def on_reset(obj):
            self.value = ""

        application.bind(on_reset=on_reset)

    def initialize(self):
        for s in self.symbols:
            button = KeyboardButton(s, Rectangle(self.button_width, self.button_height, None, None))

            def on_button_click(obj, duration):
                self.value += obj.symbol

            button.bind(on_click=on_button_click)

            self.buttons.append(button)

    def get_button(self, x, y):
        matches = [b for b in self.buttons if b.intersects(x, y)]
        return matches[0] if len(matches) > 0 else None


