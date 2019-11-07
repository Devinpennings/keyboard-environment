from events import Events


class Text:

    def __init__(self):
        self.value = ""
        self.events = Events()
        self.event_dict = {
            'on_reset': self.events.on_reset,
            'on_change': self.events.on_change
        }

    def append(self, value):
        self.value += value
        self.events.on_change(self.value)

    def reset(self):
        self.value = ""
        self.events.on_reset()

    def bind(self, **kwargs):
        for key, value in kwargs.items():
            self.event_dict[key] += value
