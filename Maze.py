from Cell import Cell
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, win, seed=None):
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
        if seed is not None:
            random.seed(seed)

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
        time.sleep(0.002)

    def _break_entrance_and_exit(self):
        first_cell = self._cells[0][0]
        first_cell.has_top_wall = False
        self._draw_cell(first_cell)
        last_cell = self._cells[-1][-1]
        last_cell.has_bottom_wall = False
        self._draw_cell(last_cell)
        self._break_walls_r(0,0)

    def _break_walls_r(self, i, j):
        cell = self._cells[i][j]
        cell.visited = True
        neighbors = self._get_unvisited_neighbors(i, j)

        while len(neighbors) > 0:
            random_idx = random.randint(0, len(neighbors) - 1)
            neighbor_i, neighbor_j = neighbors.pop(random_idx)
            neighbor_cell = self._cells[neighbor_i][neighbor_j]
            if neighbor_cell.visited:
                continue
            if neighbor_i < i:
                cell.has_top_wall = False
                neighbor_cell.has_bottom_wall = False
            elif neighbor_i > i:
                cell.has_bottom_wall = False
                neighbor_cell.has_top_wall = False
            elif neighbor_j < j:
                cell.has_left_wall = False
                neighbor_cell.has_right_wall = False
            elif neighbor_j > j:
                cell.has_right_wall = False
                neighbor_cell.has_left_wall = False

            self._draw_cell(cell)
            self._draw_cell(neighbor_cell)

            self._break_walls_r(neighbor_i, neighbor_j)


    def _get_unvisited_neighbors(self, i, j):
        neighbors = []
        if i > 0 and not self._cells[i - 1][j].visited:
            neighbors.append((i - 1, j))
        if i < self.num_rows - 1 and not self._cells[i + 1][j].visited:
            neighbors.append((i + 1, j))
        if j > 0 and not self._cells[i][j - 1].visited:
            neighbors.append((i, j - 1))
        if j < self.num_cols - 1 and not self._cells[i][j + 1].visited:
            neighbors.append((i, j + 1))
        return neighbors

    def _reset_cell_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self):
        self._solve_r(0,0)

    def _solve_r(self, i, j):
        if(i == 0 and j == 0 ):
            self._reset_cell_visited()
        if(i == len(self._cells) - 1 and j == len(self._cells[0]) - 1):
            return True
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        neighbors = self._get_unvisited_neighbors(i,j)
        for neighbor in neighbors:
            neighbor_cell = self._cells[neighbor[0]][neighbor[1]]
            if neighbor[0] > i and not neighbor_cell.has_top_wall and not current_cell.has_bottom_wall:
                current_cell.draw_move(neighbor_cell)
                if self._solve_r(neighbor[0], neighbor[1]):
                    return True
                current_cell.draw_move(neighbor_cell, undo=True)
            elif neighbor[0] < i and not current_cell.has_top_wall and not neighbor_cell.has_bottom_wall:
                current_cell.draw_move(neighbor_cell)
                if self._solve_r(neighbor[0], neighbor[1]):
                    return True
                current_cell.draw_move(neighbor_cell, undo=True)
            elif neighbor[1] > j and not current_cell.has_right_wall and not neighbor_cell.has_left_wall:
                current_cell.draw_move(neighbor_cell)
                if self._solve_r(neighbor[0], neighbor[1]):
                    return True
                current_cell.draw_move(neighbor_cell, undo=True)
            elif neighbor[1] < j and not current_cell.has_left_wall and not neighbor_cell.has_right_wall:
                current_cell.draw_move(neighbor_cell)
                if self._solve_r(neighbor[0], neighbor[1]):
                    return True
                current_cell.draw_move(neighbor_cell, undo=True)
