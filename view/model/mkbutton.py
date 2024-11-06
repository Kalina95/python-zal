import tkinter as tk
from view.view_styles import ButtonStyle


class MkButton(tk.Button):

    def __init__(self, text, command, window):
        super().__init__(master=window, text=text, width=ButtonStyle.width, height=ButtonStyle.height, padx=ButtonStyle.padx, pady=ButtonStyle.pady, bg=ButtonStyle.background_color, command=command)

    def pack_center(self) -> None:
        self.pack(padx=ButtonStyle.padx, pady=ButtonStyle.pady)

    def pack_left(self) -> None:
        self.pack(side="left", padx=ButtonStyle.padx, pady=ButtonStyle.pady)