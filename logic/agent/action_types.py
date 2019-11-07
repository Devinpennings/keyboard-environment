from collections import namedtuple
from enum import Enum

ActionType = namedtuple('Action', ['value', 'event', 'duration'])


class ActionTypes(Enum):

    @property
    def event(self):
        return self.value.event

    @property
    def duration(self):
        return self.value.duration

    CLICK = ActionType('click', 'on_click', 0.3)
    HOLD = ActionType('hold', 'on_hold', 2)
