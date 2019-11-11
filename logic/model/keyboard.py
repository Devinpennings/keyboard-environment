from events import Events
from kivy.clock import mainthread

from .keyboard_button import KeyboardButton
from .rectangle import Rectangle
from .button_handlers import get_handler


class Keyboard:

    @classmethod
    def from_template(cls, template):
        buttons = []
        default_handlers = template['defaults']['handlers']
        row_widths = {}

        for bc in template['buttons']:
            width = bc['width'] if 'width' in bc else template['defaults']['button_width']
            height = bc['height'] if 'height' in bc else template['defaults']['button_height']
            props = bc['props'] if 'props' in bc else {}
            x = bc['x'] if 'x' in bc else row_widths[bc['row']] if 'row' in bc and bc['row'] in row_widths else 0
            y = bc['y'] if 'y' in bc else bc['row'] * 50 if 'row' in bc else 0
            value = bc['value'] if 'value' in bc else ''
            text = bc['text'] if 'text' in bc else bc['value']

            button = KeyboardButton(value, Rectangle(width, height, x, y), props, text)

            if 'row' in bc:
                if not bc['row'] in row_widths:
                    row_widths[bc['row']] = 0
                row_widths[bc['row']] += width

            handlers = dict(default_handlers)
            if 'handlers' in bc:
                handlers.update(bc['handlers'])

            for event, handler in handlers.items():
                handler = get_handler(handler['name'])(**handler['args'] if 'args' in handler else {})
                button.bind_handler(event, handler)

            buttons.append(button)

        return Keyboard(
            width=template['width'],
            height=template['height'],
            buttons=buttons,
            name=template['name'] if 'name' in template else None
        )

    @classmethod
    def from_symbols(cls, width, height, button_width, button_height, symbols):
        buttons = Keyboard.generate_buttons_from_symbols(width, button_width, button_height, symbols)
        return Keyboard(width, height, buttons)

    def __init__(self, width, height, buttons, name=None):
        self.width = width
        self.height = height
        self.buttons = buttons
        self.name = name
        self.events = Events()

        self.event_dict = {
            'on_touch': self.events.on_touch,
        }

        def on_action(obj, action_type):
            self.events.on_touch(obj, action_type)

        for b in self.buttons:
            b.bind(on_action=on_action)

    @staticmethod
    def generate_buttons_from_symbols(keyboard_width, button_width, button_height, symbols):
        buttons = []
        i = 0
        c_count = 0
        r_count = 0
        columns = keyboard_width / button_width

        for s in symbols:
            button = KeyboardButton(s, Rectangle(
                button_width,
                button_height,
                c_count * button_width,
                r_count * button_height))

            c_count += 1
            if c_count == columns:
                r_count += 1
                c_count = 0

            buttons.append(button)
            i += 1

        return buttons

    @mainthread
    def bind(self, **kwargs):
        for key, value in kwargs.items():
            self.event_dict[key] += value

    def symbols(self):
        return list(map(lambda b: b.value, self.buttons))

    def get_button(self, x, y):
        matches = [b for b in self.buttons if b.intersects(x, y)]
        return matches[0] if len(matches) > 0 else None

    def __hash__(self):
        string = ""
        for b in self.buttons:
            string += b.value
        return hash(string)
