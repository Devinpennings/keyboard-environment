from abc import ABC, abstractmethod


class BaseModifier(ABC):

    @abstractmethod
    def modify(self, keyboard):
        pass

    @abstractmethod
    def reverse(self, keyboard):
        pass
