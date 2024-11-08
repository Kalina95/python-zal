import tkinter as tk


class Row(tk.Frame):
    """
    A Frame widget that automatically packs itself with a white background.

    This widget is used as a building block for creating rows in the UI,
    particularly in the NbpApiView for titles.
    """

    def __init__(self, parent: tk.Frame) -> None:
        super().__init__(master=parent, bg="white")
        self.pack(anchor="w")
