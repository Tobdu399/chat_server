import tkinter
from lib.misc import background_color, foreground_color

checkboxes = []


class Checkbox(tkinter.Checkbutton):
    def __init__(self, root, x, y, variable, text):
        super().__init__(text=text, bg=background_color, fg=foreground_color,
                         activebackground=background_color, activeforeground=foreground_color,
                         selectcolor=background_color, variable=variable)

        self.root = root
        self.x = x
        self.y = y
        self.text = text

    def show(self):
        self.place(x=self.x, y=self.y)


if __name__ == "__main__":
    exit()
