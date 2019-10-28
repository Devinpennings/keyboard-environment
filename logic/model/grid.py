from logic.model.action_cell import ActionCell
from logic.model import Rectangle


class Grid:

    def __init__(self, width, height, column_count, row_count):
        self.width = width
        self.height = height
        self.column_count = column_count
        self.row_count = row_count
        self.cells = []
        self.initialize()

    def initialize(self):
        cell_width = self.width / self.column_count if self.column_count else 0
        cell_height = self.height / self.row_count if self.row_count else 0

        for y in range(self.row_count):
            for x in range(self.column_count):
                cell = ActionCell(Rectangle(cell_width, cell_height, x * cell_width, y * cell_height))
                self.cells.append(cell)

    def cell_count(self):
        return len(self.cells)
