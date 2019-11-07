from abc import ABC, abstractmethod


class BaseButtonHandler(ABC):

    @abstractmethod
    def handle(self, obj, action):
        pass
