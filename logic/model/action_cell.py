from events import Events

from ..agent import ActionTypes
from ... import application


class ActionCell:

    def __init__(self, rectangle):
        self.rectangle = rectangle
        self.events = Events()

        self.event_dict = {
            'on_highlight': self.events.on_highlight,
        }

    def __str__(self):
        return f'<action_cell ({self.rectangle.pos_x}, {self.rectangle.pos_y})>'

    def bind(self, **kwargs):
        for key, value in kwargs.items():
            self.event_dict[key] += value

    def execute(self, action_type):
        self.events.on_highlight(self, action_type.duration)
        button = application.keyboard.get_button(*self.rectangle.center())
        button.execute(action_type) if button else None
