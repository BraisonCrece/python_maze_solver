class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.x2 = win.width - x1
        self.y2 = win.height - y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        width = win.width - (x1**2)
        height = win.height - (y1**2)
        self.cell_size_x = num_cols / width
        self.cell_size_y = num_rows / height
        self.window = win
        self._cells = []

    def _create_cells(self):
        num_cells = self.num_rows * self.num_cols
        for cell in range(num_cells):
            pass
            # self._draw_cell(self, , )

        # Continue HERE --> Create the method `_draw_cell(self, i, j) --> Cell(win, x1, x2, y1, y2, True, True, True, True)`


