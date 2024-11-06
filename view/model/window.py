import tkinter as tk
from view.view_styles import WindowStyle

class Window(tk.Tk):
    def __init__(self, title):
        super().__init__()
        self.title(title)
        self.geometry(f"{WindowStyle.width}x{WindowStyle.height}")
        self.configure(bg=WindowStyle.background_color)