from ... import application


class CLI:

    def __init__(self, height):
        self.height = height

    def list_to_string(self, col):
        def to_string(obj):
            return f'{{{str(obj)}}},\n'

        value = ""
        for i in col:
            value = value + to_string(i)
        return value

    def actions(self):
        return self.list_to_string(application.agent.actions)

    def action_count(self):
        return len(application.agent.actions)

    def action(self, action_id):
        try:
            return application.agent.execute(int(action_id))
        except ValueError:
            return 'Invalid argument'

    def buttons(self):
        return application.agent.buttons

    def reset(self):
        application.agent.reset()

    def state(self):
        return application.agent.state()

    def exit(self):
        quit()

    def execute(self, command, *args):
        try:
            function = getattr(self, command)
        except AttributeError:
            return "Command not recognized"
        # try:
        result = function(*args)
        return str(result) if result else None
        # except TypeError:
        #     return "Missing argument"
