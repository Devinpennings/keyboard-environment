from events import Events

from ... import application

class ActionCell:

    def __init__(self, rectangle):
        self.rectangle = rectangle
        self.events = Events()
        self.event_dict = {
            'on_click': self.events.on_click
        }

    def __str__(self):
        return f'<action_cell ({self.rectangle.pos_x}, {self.rectangle.pos_y})>'

    def bind(self, **kwargs):
        for key, value in kwargs.items():
            self.event_dict[key] += value

    def click(self, duration):
        button = application.keyboard.get_button(*self.rectangle.center())
        if button:
            button.click(duration)
        self.events.on_click(self, duration)
        return f'Clicked cell {self.__str__()}'
