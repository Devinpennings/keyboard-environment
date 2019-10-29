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
        print(application.cli.execute(command, *args))


def start_graphical():

    if isnotebook():
        print('Cannot start graphic mode from notebook.')
        return

    from .ui.interface import Interface
    Interface().run()


def start(mode=None):

    if mode is None:
        mode = config.APPLICATION_MODE

    print(f'Starting with mode {mode}...')

    if mode == ApplicationMode.API.value:
        start_api()
    elif mode == ApplicationMode.CONSOLE.value:
        start_console()
    elif mode == ApplicationMode.GRAPHIC.value:
        start_graphical()
    elif mode == ApplicationMode.DEMO.value:
        start_api_demo()
    else:
        pass


def isnotebook():
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
    start()
