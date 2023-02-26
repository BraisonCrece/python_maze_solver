from Point import Point
from Line import Line

class Cell:
  # has_left_wall
  # has_right_wall
  # has_top_wall
  # has_bottom_wall
  # _x1
  # _x2
  # _y1
  # _y2
  # _win
    def __init__(self, window, x1, x2, y1, y2, left, right, top, bottom):
        self._window = window
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom

    def draw(self):
        top_left_corner = Point(self._x1, self._y1)
        top_right_corner = Point(self._x2, self._y1)
        bottom_right_corner = Point(self._x2, self._y2)
        bottom_left_corner = Point(self._x1, self._y2)

        lines = []
        if self.has_top_wall:
            lines.append((top_left_corner, top_right_corner))
        if self.has_right_wall:
            lines.append((top_right_corner, bottom_right_corner))
        if self.has_bottom_wall:
            lines.append((bottom_left_corner, bottom_right_corner))
        if self.has_left_wall:
            lines.append((top_left_corner, bottom_left_corner))

        for line in lines:
            self._window.draw_line(Line(line[0], line[1]), "black")
