import unittest
from Maze import Maze
from Window import Window

class Tests(unittest.TestCase):
    def setUp(self):
        self.window = Window(100, 100)
        self.num_columns = 12
        self.num_rows = 10
        self.maze = Maze(0, 0, self.num_rows, self.num_columns, self.window)

    def test_maze_create_cells(self):
        self.assertEqual(
            len(self.maze._cells[0]),
            self.num_columns,
        )
        self.assertEqual(
            len(self.maze._cells),
            self.num_rows,
        )

    def test_maze_open_entrance_and_exit(self):
        self.assertEqual(
            self.maze._cells[0][0].has_top_wall,
            self.maze._cells[self.num_rows - 1][self.num_columns - 1].has_bottom_wall
        )

    def test_all_cells_where_visited_after_break_walls_r(self):
        count = 0
        for row in self.maze._cells:
            for cell in row:
                if cell.visited:
                    continue
                else:
                    count += 1
        self.assertEqual(count, 0)

    def test_reset_visited_cells(self):
        total_cells = self.maze.num_cols * self.maze.num_rows
        count = 0
        self.maze._reset_cell_visited()
        for row in self.maze._cells:
            for cell in row:
                if cell.visited:
                    continue
                else:
                    count += 1
        self.assertEqual(count, total_cells)

    def test_maze_got_solved(self):
        self.assertTrue(self.maze.solve())



if __name__ == "__main__":
    unittest.main()

