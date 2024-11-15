import tkinter as tk
from tkinter import Frame
from tkinter.scrolledtext import ScrolledText


class TextArea(ScrolledText):
    """
    Custom TextArea widget extending tk.scrolledtext.ScrolledText with predefined styling and positioning methods.

    Inherits from tk.scrolledtext.ScrolledText and applies LabelStyle configurations for consistent appearance
    across the application.
    """

    def __init__(self, parent: Frame) -> None:
        super().__init__(master=parent, wrap=tk.WORD, state="disabled", width=60, height=15)

    def pack_center(self) -> None:
        self.pack(expand=True, padx=10, pady=10)

    def destroy_area(self) -> None:
        self.pack_forget()
        self.destroy()
