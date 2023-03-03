from Point import Point
from Window import Window
from Line import Line
from Cell import Cell
from Maze import Maze

window = Window(800, 600)
maze = Maze(100, 100, 10, 15, window, 0.001)
maze.solve()

window.wait_for_close()

