from Point import Point
from Line import Line

class Cell:
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
        center_x = (self._x1 + self._x2) / 2
        center_y = (self._y1 + self._y2) / 2
        self.center_point = Point(center_x, center_y)

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

    def draw_move(self, to_cell, undo=False):
        move_left   = not self.has_left_wall    and not to_cell.has_right_wall
        move_right  = not self.has_right_wall   and not to_cell.has_left_wall
        move_bottom = not self.has_bottom_wall  and not to_cell.has_top_wall
        move_top    = not self.has_top_wall     and not to_cell.has_bottom_wall

        exists_move = move_left or move_right or move_top or move_bottom
        if exists_move and not undo:
            self._window.draw_line(Line(self.center_point, to_cell.center_point), "red")
        elif exists_move and undo:
            self._window.draw_line(Line(self.center_point, to_cell.center_point), "gray")
        else:
            return


