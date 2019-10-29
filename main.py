from cmd import Cmd

import application
import config
from application_mode import ApplicationMode


def start_api_demo():
    print(application.agent.execute(0))
    print(application.agent.execute(24))
    print(application.agent.execute(3))


def start_api():
    print('API mode has no runtime.')


def start_console():
    while True:
        raw = input("> ")
        parsed = raw.split(' ')
        command = parsed[0]
        args = parsed[1:]
        print(application.cli.execute(command, *args))


def start_graphical():
    from ui import Interface
    Interface().run()


if __name__ == '__main__':
    mode = config.APPLICATION_MODE

    if mode == ApplicationMode.API:
        start_api()
    elif mode == ApplicationMode.CONSOLE:
        start_console()
    elif mode == ApplicationMode.GRAPHIC:
        start_graphical()
    elif mode == ApplicationMode.DEMO:
        start_api_demo()
    else:
        pass
