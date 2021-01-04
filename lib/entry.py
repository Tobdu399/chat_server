import tkinter

entries = {}


class InputField(tkinter.Entry):
    def __init__(self, root, x, y, width, height, placeholder):
        super().__init__()

        self.root = root
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.placeholder = placeholder
        self.placeholder_color = "grey"
        self.default_fg_color = self["fg"]

        self.focus_out()
        self.bind("<FocusIn>", self.focus_in)
        self.bind("<FocusOut>", self.focus_out)

    def show(self):
        self.place(x=self.x, y=self.y, width=self.width, height=self.height)

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self["fg"] = self.placeholder_color

    def focus_in(self, *args):
        if self["fg"] == self.placeholder_color:
            self.delete('0', "end")
            self["fg"] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()


if __name__ == "__main__":
    exit()
