import tkinter as tk

from view.view_styles import WindowStyle


class Window(tk.Tk):
    """
    A custom Tkinter window class that extends the default Tkinter window (tk.Tk).

    This class allows you to create a window with a predefined title, dimensions, and background color.
    It is customizable through the WindowStyle class, which provides the style configurations like window size and background color.
    """
    def __init__(self, title: str) -> None:
        super().__init__()
        self.title(title)
        self.geometry(f"{WindowStyle.width}x{WindowStyle.height}")
        self.configure(bg=WindowStyle.background_color)
