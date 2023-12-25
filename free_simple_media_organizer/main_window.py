# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog
import pathlib
import getpass
import socket

from app_functions import connect_sqlite
from create_new_db import createNewDb
from db_settings import dbSettings


class mainWindow(tk.Tk):
    """App main window"""

    APP_VERSION = 'v01.001.001.00'
    # APP_START_POINT = os.path.dirname(__file__)
    APP_START_POINT = pathlib.Path(__file__).parent
    APP_USER = f'{socket.gethostname()}/{getpass.getuser()}'

    def __init__(self):
        super().__init__()
        self.title("Free simple media organizer")

        self.menu_bar = tk.Menu(self)

        self.menu_db = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_db.add_command(label="New...", command=self.new_db)
        self.menu_db.add_command(label="Open...", command=self.open_db)

        self.menu_open_last = tk.Menu(self.menu_db, tearoff=0)
        self.menu_db.add_cascade(label="Open last", menu=self.menu_open_last)
        self.menu_db.add_separator()
        self.menu_db.add_command(label="Settings..", state='disabled', command=self.db_settings)
        self.menu_db.add_separator()
        self.menu_db.add_command(label="Close", state='disabled', command=self.db_close)

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
        self.dialog_control_block(True)
        dialog_create_new_db.wait_window()
        self.dialog_control_block(False)

        self.db_file_path = dialog_create_new_db.db_file_path
        print(self.db_file_path)
        self.db_menu_control()

        if self.db_file_path:
            self.db_settings()

    def open_db(self):
        direcotry_path = filedialog.askdirectory()
        self.db_main_path = pathlib.Path(direcotry_path)
        self.con = connect_sqlite(self.db_file_path)
        if self.con:
            self.db_menu_control()

    def db_settings(self):
        dialog_create_new_db = dbSettings(self, self.db_file_path)
        dialog_create_new_db.grab_set()
        self.dialog_control_block(True)
        dialog_create_new_db.wait_window()
        self.dialog_control_block(False)

    def db_close(self):
        self.db_file_path = None
        self.db_file_path = False
        self.db_menu_control()

    def db_menu_control(self):
        if self.db_file_path:
            self.menu_db.entryconfig("New...", state='disabled')
            self.menu_db.entryconfig("Open...", state='disabled')
            self.menu_db.entryconfig("Open last", state='disabled')
            self.menu_db.entryconfig("Settings..", state='active')
            self.menu_db.entryconfig("Close", state='active')
        else:
            self.menu_db.entryconfig("New...", state='active')
            self.menu_db.entryconfig("Open...", state='active')
            self.menu_db.entryconfig("Open last", state='active')
            self.menu_db.entryconfig("Settings..", state='disabled')
            self.menu_db.entryconfig("Close", state='disabled')

    def dialog_control_block(self, option: bool):
        if option:
            self.menu_bar.entryconfig("Database", state='disabled')
            self.menu_bar.entryconfig("Settings", state='disabled')
            self.menu_bar.entryconfig("Help", state='disabled')
            # self.withdraw()
        else:
            self.menu_bar.entryconfig("Database", state='active')
            self.menu_bar.entryconfig("Settings", state='active')
            self.menu_bar.entryconfig("Help", state='active')
            # self.deiconify()

    def app_settings(self):
        print("Settings")
        print(self.APP_START_POINT)


if __name__ == "__main__":
    main_window = mainWindow()
    main_window.mainloop()
