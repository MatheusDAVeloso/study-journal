from ui.window import create_window
from ui.panel_first import create_first_panel
from ui.write import write

window = create_window()
first_panel = create_first_panel(window)
write(first_panel, "Hello World!")

window.mainloop()