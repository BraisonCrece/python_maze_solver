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
        self._create_cells()

    def _create_cells(self):
        for row in range(self.num_rows):
            cell_row = []
            for col in range(self.num_cols):
                x1 = self.x1 + col * self.cell_size_x
                y1 = self.y1 + row * self.cell_size_y
                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y
                cell = Cell(self.window, x1, x2, y1, y2, True, True, True, True)
                cell_row.append(cell)
                self._draw_cell(cell)
            self._cells.append(cell_row)
        self._break_entrance_and_exit()

    def _draw_cell(self, cell):
        cell.draw()
        self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        first_cell.has_top_wall = False
        self._draw_cell(first_cell)
        last_cell = self._cells[-1][-1]
        last_cell.has_bottom_wall = False
        self._draw_cell(last_cell)




