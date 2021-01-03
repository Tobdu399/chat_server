import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.bind_all("<MouseWheel>", self.mousewheel)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.place(x=463, height=180)

    def style(self):
        self.canvas.configure(yscrollcommand=self.scrollbar.set, bg="white", highlightbackground="white", highlightthickness=1)

    def mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
