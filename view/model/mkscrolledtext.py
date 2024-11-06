import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class MkScrolledText(ScrolledText):
    def __init__(self, parent):
        super().__init__(master=parent, wrap=tk.WORD, state="disabled", width=60, height=15)

    def pack_center(self):
        self.pack(expand=True, padx=10, pady=10)

    def destroy_area(self):
        self.pack_forget()
        self.destroy()