import tkinter as tk
# from tkinter import ttk


class GuiMainWindow(tk.Tk):
    """App main window

    Args:
        ttk (_type_): _description_
    """

    def __init__(self):
        super().__init__()
        self.title("Free simple media organizer")

        self.menu_bar = tk.Menu(self)

        self.menu_db = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_db.add_command(label="New...")
        self.menu_db.add_command(label="Open..")

        self.menu_open_last = tk.Menu(self.menu_db, tearoff=0)
        self.menu_db.add_cascade(label="Open last", menu=self.menu_open_last)
        self.menu_db.add_separator()
        self.menu_db.add_command(label="Close")

        self.menu_settings = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_settings.add_command(label="Aplication...")
        self.menu_settings.add_command(label="Database...")

        self.menu_help = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_help.add_command(label="Information...")

        self.menu_bar.add_cascade(label="Database", menu=self.menu_db)
        self.menu_bar.add_cascade(label="Settings", menu=self.menu_settings)
        self.menu_bar.add_cascade(label="Help", menu=self.menu_help)

        self.config(menu=self.menu_bar)

    #     # self.menu_open_last.add_command(label="1")
    #     # self.menu_open_last.add_command(label="2")


if __name__ == "__main__":
    main_window = GuiMainWindow()
    main_window.mainloop()
