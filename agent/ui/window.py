import tkinter as tk
from . import theme

# ────────── Configure Window ──────────────────────────────
def create_window() -> tk.Tk:
    window = tk.Tk()
    window.geometry("1280x720")
    window.configure(bg=theme.BACKGROUND)
    window.title("Agent MDAV")
    return window