from Point import Point
from Window import Window
from Line import Line
from Cell import Cell
from Maze import Maze

window = Window(800, 600)
maze = Maze(100, 100, 4, 6, window)

window.wait_for_close()

