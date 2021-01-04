import tkinter

buttons = {}


class Button(tkinter.Button):
    def __init__(self, root, x, y, width, height, text, command, color, font):
        super().__init__(text=text, command=command, bg=color, activebackground=color, font=font, relief="groove", borderwidth=2)
        self.root = root
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)


if __name__ == "__main__":
    exit()
