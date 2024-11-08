import tkinter as tk
from tkinter import Frame

from view.view_styles import LabelStyle


class Label(tk.Label):
    """
    Custom label widget extending tk.Label with predefined styling and positioning methods.

    Inherits from tk.Label and applies LabelStyle configurations for consistent appearance
    across the application.
    """

    def __init__(self, text: str, parent: Frame) -> None:
        super().__init__(master=parent, text=text, height=LabelStyle.height, padx=LabelStyle.padx, pady=LabelStyle.pady,
                         bg=LabelStyle.background_color, justify=LabelStyle.justify, anchor=LabelStyle.anchor)

    def pack_center(self) -> None:
        self.pack(padx=LabelStyle.padx, pady=LabelStyle.pady)

    def pack_left(self) -> None:
        self.pack(side="left", padx=LabelStyle.padx, pady=LabelStyle.pady)
