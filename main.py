import sys

from . import application
from . import config
from .application_mode import ApplicationMode


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
        result = application.cli.execute(command, *args)
        if result:
            print(result)


def start_graphical():
    from .ui.interface import Interface
    Interface().run()


def start(mode=None):

    if mode is None:
        mode = config.APPLICATION_MODE

    print(f'Starting with mode {mode}...')

    if mode == ApplicationMode.API.value or mode == ApplicationMode.API:
        start_api()
    elif mode == ApplicationMode.CONSOLE.value or mode == ApplicationMode.CONSOLE:
        start_console()
    elif mode == ApplicationMode.GRAPHIC.value or mode == ApplicationMode.GRAPHIC:
        start_graphical()
    elif mode == ApplicationMode.DEMO.value or mode == ApplicationMode.DEMO:
        start_api_demo()
    else:
        pass


def is_notebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter


if __name__ == '__main__':
    start(sys.argv[1] if len(sys.argv) > 1 else None)
