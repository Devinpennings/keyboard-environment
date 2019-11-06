class Rectangle:

    def __init__(self, width, height, pos_x, pos_y):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y

    def raw(self):
        return self.pos_x, self.pos_y, self.width, self.height

    def center(self):
        return (
            self.pos_x + self.width / 2,
            self.pos_y + self.height / 2,
        )

    def __str__(self):
        return f'rectangle: ({self.pos_x}, {self.pos_y}) | w: {self.width} h: {self.height}'
