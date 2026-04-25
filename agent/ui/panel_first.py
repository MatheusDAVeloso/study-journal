import tkinter as tk
from . import theme

def create_first_panel(parent: tk.Tk) -> tk.Text:
    canvas = tk.Text(
        parent,
        font        = theme.FONT,
        bg          = theme.BACKGROUND,
        fg          = theme.FOREGROUND,
        borderwidth = 0,
    )
    
    canvas.pack(expand=True, fill="both")
    
    return canvas