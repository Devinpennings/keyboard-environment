from threading import Thread
from time import sleep

from ... import application
from .action import Action
from .result import Result


class Agent:

    def __init__(self, keyboard, grid, action_types):
        self.keyboard = keyboard
        self.buttons = keyboard.buttons
        self.grid = grid
        self.action_types = action_types
        self.actions = []
        self.action_dict = {}
        self.states = {}

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
        application.reset()

    def __next_state__(self):
        max_s = -1
        for k, v in self.states.values():
            if v > max_s:
                max_s = v
        return max_s + 1

    def state(self):
        if self.keyboard not in self.states:
            self.states[self.keyboard] = self.__next_state__()
        return self.states[self.keyboard]

    def execute(self, action_id):
        def execute_wait(action):
            action.execute()
            sleep(action.duration)

        try:
            thread = Thread(target=execute_wait, args=(self.action_dict[action_id], ))
            thread.start()
            return Result(self.keyboard.value, self.state(), bool(self.keyboard.value))

        except KeyError:
            return f'Action {action_id} does not exist'
