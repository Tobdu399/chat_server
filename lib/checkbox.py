import tkinter
from .misc import background_color

checkboxes = []


class Checkbox(tkinter.Checkbutton):
    def __init__(self, root, x, y, variable, text):
        super().__init__(text=text, bg=background_color, activebackground=background_color, variable=variable)

        self.root = root
        self.x = x
        self.y = y
        self.text = text

    def show(self):
        self.place(x=self.x, y=self.y)
