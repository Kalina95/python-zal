import tkinter as tk

class MkRow(tk.Frame):

    def __init__(self, parent):
        super().__init__(master=parent, bg="white")
        self.pack(anchor="w")