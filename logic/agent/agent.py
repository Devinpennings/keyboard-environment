from threading import Thread
from time import sleep

from ... import application
from .action import Action
from .result import Result


class Agent:

    def __init__(self, grid, action_types):
        self.grid = grid
        self.action_types = action_types
        self.actions = []
        self.action_dict = {}
        self.states = {}
        self.state()

        self.__init_actions()

    def __init_actions(self):
        identifier = 0
        for cell in self.grid.cells:
            for at in self.action_types:
                action = Action(identifier, cell, at)
                self.actions.append(action)
                self.action_dict[identifier] = action
                identifier += 1

    def reset(self):
        application.init_keyboard()
        application.text.reset()

    def __next_state__(self):
        max_s = -1
        for v in self.states.values():
            if v > max_s:
                max_s = v
        return max_s + 1

    def state(self):
        if application.keyboard.__hash__() not in self.states:
            self.states[application.keyboard.__hash__()] = self.__next_state__()
        return self.states[application.keyboard.__hash__()]

    def start_demo(self):
        for a in self.actions:
            print(self.execute(a.identifier))
            import time
            time.sleep(0.5)

    def execute(self, action_id):
        def execute_wait(action):
            action.execute()
            sleep(action.action_type.duration)

        try:
            thread = Thread(target=execute_wait, args=(self.action_dict[action_id], ))
            thread.start()
            return Result(application.text.value, self.state(), bool(application.text.value))

        except KeyError:
            return f'Action {action_id} does not exist'
