import tkinter as tk

class MkFrame(tk.Frame):

    def __init__(self, parent, bg_color):
        super().__init__(master=parent, bg=bg_color)

    def pack_center(self):
        self.pack(expand=False, anchor="center")
