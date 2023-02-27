from Cell import Cell
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, win):
        self.x1 = x1
        self.y1 = y1
        self.x2 = win.width - x1
        self.y2 = win.height - y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.width = win.width - (x1*2)
        self.height = win.height - (y1*2)
        self.cell_size_x = self.width / num_cols
        self.cell_size_y = self.height / num_rows
        self.window = win
        self._cells = []
        print(self.x1)
        print(self.y1)
        print(self.x2)
        print(self.y2)
        print(self.width)
        print(self.height)
        print(self.cell_size_x)
        print(self.cell_size_y)
        self._create_cells()

    def _create_cells(self):
        start_x = self.x1
        start_y = self.y1
        to_x = round(self.width + self.x1)
        to_y = round(self.height + self.y1)
        step_x = round(self.cell_size_x)
        step_y = round(self.cell_size_y)

        for i in range(start_x, to_x, step_x):
            for j in range(start_y, to_y, step_y):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        cell = Cell(self.window,i, i + self.cell_size_x, j, j + self.cell_size_y, True, True, True, True)
        self._cells.append(cell)
        cell.draw()
        self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)


