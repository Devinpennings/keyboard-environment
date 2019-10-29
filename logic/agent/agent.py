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

    def execute(self, action_id):
        def execute_wait(action):
            action.execute()
            sleep(action.duration)

        try:
            thread = Thread(target=execute_wait, args=(self.action_dict[action_id], ))
            thread.start()
            return Result(self.keyboard.value, 0, bool(self.keyboard.value))

        except KeyError:
            return f'Action {action_id} does not exist'
