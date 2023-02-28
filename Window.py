from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root_widget = Tk()
        self.__root_widget.title = "Maze Solver"
        self.canvas = Canvas(self.__root_widget, width=self.width, height=self.height)
        self.canvas.config(bg='white')

        self.canvas.pack()
        self.running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)





