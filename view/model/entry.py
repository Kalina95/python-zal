import tkinter as tk
from tkinter import Frame

from view.view_styles import EntryStyle


class Entry(tk.Entry):

    """
    Custom entry widget extending tk.Entry with predefined styling and positioning methods.

    Inherits from tk.Entry and applies EntryStyle configurations for consistent appearance
    across the application.
    """

    def __init__(self, parent: Frame) -> None:
        super().__init__(master=parent, width=30)

    def pack_center(self) -> None:
        self.pack(padx=EntryStyle.padx, pady=EntryStyle.pady)

    def pack_left(self) -> None:
        self.pack(side="left", padx=EntryStyle.padx, pady=EntryStyle.pady)
