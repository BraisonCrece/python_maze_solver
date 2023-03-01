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
        if seed is not None:
            random.seed(seed)
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
        self._break_walls_r(0,0)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        print(f"current cell: i -> {i}, j -> {j}")
        adjacents = []
        if i == 0:
            if j == 0:
                adjacents.append([i,j+1])
                adjacents.append([i+1,j])
            if j == self.num_cols -1:
                adjacents.append([i,j-1])
                adjacents.append([i+1,j])
        elif i == self.num_rows -1:
            if j == 0:
                adjacents.append([i+1,j])
                adjacents.append([i,j+1])
            if j == self.num_cols -1:
                adjacents.append([i-1,j])
                adjacents.append([i,j-1])
        elif j == 0:
            adjacents.append([i-1,j])
            adjacents.append([i,j+1])
            adjacents.append([i+1,j])
        elif j == self.num_cols -1:
            adjacents.append([i-1, j])
            adjacents.append([i, j-1])
            adjacents.append([i+1, j])
        elif i != 0 and i != self.num_rows -1 and j != 0 and j != self.num_cols-1:
            adjacents.append([i,j-1])
            adjacents.append([i,j+1])
            adjacents.append([i+1,j])
            adjacents.append([i-1,j])

        print(f"adjacents -> {adjacents}")

        move_options = []
        for cell in adjacents:
            if self._cells[cell[0]][cell[1]].visited == False:
                move_options.append(cell)
        #############################
        # Take a look at this point #
        #############################
        if len(move_options) == 1:
            cell_to_move = move_options[0]
        elif len(move_options) == 0:
            print("returned")
            return
        else:
            cell_to_move = move_options[random.randint(0,len(move_options)-1)]

        print(f"move options -> {move_options}")
        print(f"cell to move -> {cell_to_move}")

        # move to left
        if i == cell_to_move[0] and j > cell_to_move[1]:
            self._cells[i][j].has_left_wall = False
            self._cells[cell_to_move[0]][cell_to_move[1]].has_right_wall = False
        # move right
        elif i == cell_to_move[0] and j < cell_to_move[1]:
            self._cells[i][j].has_right_wall = False
            self._cells[cell_to_move[0]][cell_to_move[1]].has_left_wall = False
        # move down
        elif i < cell_to_move[0] and j == cell_to_move[1]:
            self._cells[i][j].has_bottom_wall = False
            self._cells[cell_to_move[0]][cell_to_move[1]].has_top_wall = False
        # move up
        elif i > cell_to_move[0] and j == cell_to_move[1]:
            self._cells[i][j].has_top_wall = False
            self._cells[cell_to_move[0]][cell_to_move[1]].has_bottom_wall = False

        self._draw_cell(self._cells[i][j])
        self._draw_cell(self._cells[cell_to_move[0]][cell_to_move[1]])
        self._cells[i][j].draw_move(self._cells[cell_to_move[0]][cell_to_move[1]])

        #################################################
        # Then continue trying to do recursiveness work #
        #################################################
        self._break_walls_r(cell_to_move[0], cell_to_move[1])


