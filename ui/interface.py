import kivy
from kivy.app import App

from .widgets.main_screen import MainScreen

kivy.require('1.11.1')


class Interface(App):

    def build(self):
        self.title = 'Keyboard Environment'

        return MainScreen()


if __name__ == '__main__':
    Interface().run()
