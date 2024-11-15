import tkinter as tk
from typing import Any

from view.view_styles import ButtonStyle


class Button(tk.Button):
    """
    Custom button widget extending tk.Button with predefined styling and positioning methods.

    Inherits from tk.Button and applies ButtonStyle configurations for consistent appearance
    across the application.
    """

    def __init__(self, text: str, command: str, window: tk.Frame) -> None:
        super().__init__(master=window, text=text, width=ButtonStyle.width, height=ButtonStyle.height,
                         padx=ButtonStyle.padx, pady=ButtonStyle.pady, bg=ButtonStyle.background_color, command=command)

    def pack_center(self) -> None:
        self.pack(padx=ButtonStyle.padx, pady=ButtonStyle.pady)

    def pack_left(self) -> None:
        self.pack(side="left", padx=ButtonStyle.padx, pady=ButtonStyle.pady)
