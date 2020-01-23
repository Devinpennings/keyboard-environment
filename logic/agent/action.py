class Action:

    def __init__(self, identifier, location, action_type):
        self.identifier = identifier
        self.location = location
        self.action_type = action_type

    def __str__(self):
        return f'<Action: {self.identifier} | ' \
               f'({self.location.rectangle.pos_x}, {self.location.rectangle.pos_y}) | ' \
               f'{self.action_type}>'

    def execute(self):
        return self.location.execute(self.action_type)
