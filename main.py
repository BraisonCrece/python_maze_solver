from Point import Point
from Window import Window
from Line import Line
from Cell import Cell

point1 = Point(100,400 )
point2 = Point(150, 500)
point3 = Point(20, 100)
point4 = Point(250, 300)

line1 = Line(point1, point2)
line2 = Line(point3, point4)

window = Window(800, 600)
cell = Cell(window, 100, 200, 100, 200, True, False, True, True)
cell.draw()

window.wait_for_close()

