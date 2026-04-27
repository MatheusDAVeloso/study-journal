import tkinter as tk
from . import theme

class Divider:
    def __init__(self, parent: tk.Tk):
        self.text = tk.Text(
            parent,
            foreground = theme.FOREGROUND,
            background = theme.BACKGROUND,
        )

        self.text.insert('end', 'Hello, World!')
        self.text.configure(state = 'disabled')

        self.text.pack()
        
