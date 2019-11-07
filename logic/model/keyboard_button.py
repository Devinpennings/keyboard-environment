from events import Events

from ..agent import ActionTypes


class KeyboardButton:

    def __init__(self, value, rectangle, props={}, text=None):
        self.value = value
        self.text = text if text else value
        self.rectangle = rectangle
        self.events = Events()
        self.widget = None
        self.props = props
        self.event_dict = {
            ActionTypes.CLICK.event: self.events.on_click,
            ActionTypes.HOLD.event: self.events.on_hold,
            'on_action': self.events.on_action
        }

    def __str__(self):
        return f'<Button: {self.text} ({self.rectangle.width}, {self.rectangle.height})>'

    def intersects(self, x, y):
        return \
            self.rectangle.pos_x <= x <= self.rectangle.pos_x + self.rectangle.width and \
            self.rectangle.pos_y <= y <= self.rectangle.pos_y + self.rectangle.height

    def bind(self, **kwargs):
        for key, value in kwargs.items():
            self.event_dict[key] += value

    def bind_handler(self, event, handler):
        self.event_dict[event] += handler.handle

    def execute(self, action_type):
        self.event_dict[action_type.event](self, action_type)
        self.events.on_action(self, action_type)
