import tkinter as tk

def write(canvas: tk.Text, text: str) -> None:
    canvas.configure(state="normal")
    canvas.insert("end", text)
    canvas.configure(state="disabled")