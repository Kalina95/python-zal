import tkinter as tk
from view.view_styles import LabelStyle



class MkLabel(tk.Label):

    def __init__(self, text, parent):
        super().__init__(master = parent, text=text, height=LabelStyle.height, padx=LabelStyle.padx, pady=LabelStyle.pady, bg=LabelStyle.background_color, justify=LabelStyle.justify, anchor=LabelStyle.anchor)

    def pack_center(self):
        self.pack(padx=LabelStyle.padx, pady=LabelStyle.pady)

    def pack_left(self):
        self.pack(side="left", padx=LabelStyle.padx, pady=LabelStyle.pady)