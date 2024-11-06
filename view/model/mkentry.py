import tkinter as tk
from view.view_styles import EntryStyle



class MkEntry(tk.Entry):

    def __init__(self, parent):
        super().__init__(master=parent, width=30)

    def pack_center(self):
        self.pack(padx=EntryStyle.padx, pady=EntryStyle.pady)

    def pack_left(self):
        self.pack(side="left", padx=EntryStyle.padx, pady=EntryStyle.pady)