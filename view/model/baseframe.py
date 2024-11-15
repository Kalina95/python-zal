import tkinter as tk
from tkinter import Frame


class BaseFrame(tk.Frame):
    """Base frame component providing common functionality for UI elements.

    This class extends tk.Frame to provide centralized positioning and consistent
    background color management for derived UI components.
    """

    def __init__(self, parent: Frame, bg_color: str) -> None:
        super().__init__(master=parent, bg=bg_color)

    def pack_center(self) -> None:
        self.pack(expand=False, anchor="center")

    def destroy_frame(self) -> None:
        self.pack_forget()
        self.destroy()
