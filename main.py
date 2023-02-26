from Point import Point
from Window import Window
from Line import Line

point1 = Point(100, 500)
point2 = Point(150, 500)
point3 = Point(20, 500)
point4 = Point(25, 500)

line1 = Line(point1, point2)
line2 = Line(point3, point4)

window = Window(800, 600)
window.draw_line(line1, "red")
window.draw_line(line2, "blue")
window.wait_for_close()

