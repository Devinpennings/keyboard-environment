from .base_modifier import BaseModifier


class UppercaseModifier(BaseModifier):

    def modify(self, keyboard):
        for button in keyboard.buttons:
            if button.value == button.text:
                button.text = button.text.upper()
                button.value = button.value.upper()
        return keyboard

    def reverse(self, keyboard):
        for button in keyboard.buttons:
            if button.value == button.text:
                button.text = button.text.lower()
                button.value = button.value.lower()
        return keyboard
