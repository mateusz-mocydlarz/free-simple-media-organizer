import tkinter as tk
# from tkinter import ttk
from create_new_db import createNewDb
import os
import socket


class mainWindow(tk.Tk):
    """App main window"""

    APP_VERSION = "v01.001.001.00"
    APP_START_POINT = os.path.dirname(__file__)
    APP_USER = f"{socket.gethostname()}/{os.getlogin()}"

    def __init__(self):
        super().__init__()
        self.title("Free simple media organizer")

        self.menu_bar = tk.Menu(self)

        self.menu_db = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_db.add_command(label="New...", command=self.new_db)
        self.menu_db.add_command(label="Open...")

        self.menu_open_last = tk.Menu(self.menu_db, tearoff=0)
        self.menu_db.add_cascade(label="Open last", menu=self.menu_open_last)
        self.menu_db.add_separator()
        self.menu_db.add_command(label="Settings..", state="disabled", command=self.db_settings)
        self.menu_db.add_separator()
        self.menu_db.add_command(label="Close", state="disabled", command=self.db_close)

        self.menu_settings = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_settings.add_command(label="Aplication...", command=self.app_settings)
        self.menu_settings.add_command(label="Database...")

        self.menu_help = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_help.add_command(label="Information...")

        self.menu_bar.add_cascade(label="Database", menu=self.menu_db)
        self.menu_bar.add_cascade(label="Settings", menu=self.menu_settings)
        self.menu_bar.add_cascade(label="Help", menu=self.menu_help)

        self.config(menu=self.menu_bar)

    #     # self.menu_open_last.add_command(label="1")
    #     # self.menu_open_last.add_command(label="2")

    def new_db(self):
        dialog_create_new_db = createNewDb(self)
        dialog_create_new_db.grab_set()
        dialog_create_new_db.wait_window()

        self.con = dialog_create_new_db.con
        self.db_menu_control()

    def db_settings(self):
        print("db_settings")

    def db_close(self):
        self.con.close()
        self.con = False
        self.db_menu_control()

    def db_menu_control(self):
        if self.con:
            self.menu_db.entryconfig("New...", state="disabled")
            self.menu_db.entryconfig("Open...", state="disabled")
            self.menu_db.entryconfig("Open last", state="disabled")
            self.menu_db.entryconfig("Settings..", state="active")
            self.menu_db.entryconfig("Close", state="active")
        else:
            self.menu_db.entryconfig("New...", state="active")
            self.menu_db.entryconfig("Open...", state="active")
            self.menu_db.entryconfig("Open last", state="active")
            self.menu_db.entryconfig("Settings..", state="disabled")
            self.menu_db.entryconfig("Close", state="disabled")

    def app_settings(self):
        print("Settings")


if __name__ == "__main__":
    main_window = mainWindow()
    main_window.mainloop()
