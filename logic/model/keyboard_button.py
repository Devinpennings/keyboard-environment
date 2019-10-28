from events import Events


class KeyboardButton:

    def __init__(self, symbol, rectangle):
        self.symbol = symbol
        self.rectangle = rectangle
        self.events = Events()
        self.widget = None
        self.event_dict = {
            'on_click': self.events.on_click
        }

    def __str__(self):
        return f'<Button: {self.symbol} ({self.rectangle.width}, {self.rectangle.height})>'

    def intersects(self, x, y):
        return \
            self.rectangle.pos_x <= x <= self.rectangle.pos_x + self.rectangle.width and \
            self.rectangle.pos_y <= y <= self.rectangle.pos_y + self.rectangle.height

    def bind(self, **kwargs):
        for key, value in kwargs.items():
            self.event_dict[key] += value

    def click(self, duration):
        self.events.on_click(self, duration)
        return self.symbol
