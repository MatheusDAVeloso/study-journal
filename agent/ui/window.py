import tkinter as tk
from . import theme

class Window :
    # ────────── Configure Window ──────────────────────────────
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1280x720")
        self.window.configure(bg=theme.BACKGROUND)
        self.window.title("Agent MDAV")

    def open(self):
        self.window.mainloop()
