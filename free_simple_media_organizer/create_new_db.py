# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pathlib
import hashlib
import time

from app_functions import connect_sqlite


class createNewDb(tk.Toplevel):
    """Create new database

    Args:
        master: master window
    """

    db_file_path = None

    def __init__(self, master: tk.Tk):
        super().__init__(master)

        frm_new_db = tk.Frame(self)
        frm_new_db.pack(fill="both", padx=10, pady=10, expand=True)

        frm_label = tk.Frame(frm_new_db)
        frm_path = tk.Frame(frm_new_db)
        frm_warning = tk.Frame(frm_new_db)
        frm_control = tk.Frame(frm_new_db)

        lbl_new_db = ttk.Label(frm_label, text="Select empy directory, to create new db:")

        self.entry_path_db = tk.StringVar()
        self.entry_path_db.trace('w', self.check_path)
        self.ent_path_db = ttk.Entry(frm_path, textvariable=self.entry_path_db)
        btn_path_db = ttk.Button(frm_path, text="Select directory", command=self.select_directory)

        self.lbl_warning = tk.Label(frm_warning, fg="red")

        btn_cancel = ttk.Button(frm_control, text="Cancel", command=self.destroy)
        self.btn_create = ttk.Button(frm_control, text="Create", command=self.create_db, state="disabled")

        frm_label.pack(side='top', fill='x')
        lbl_new_db.pack(side='left')

        frm_path.pack(fill='both')
        self.ent_path_db.pack(side='left', fill='x', expand=True)
        btn_path_db.pack()

        frm_warning.pack(fill='both')
        self.lbl_warning.pack(side='left')

        frm_control.pack(side='bottom', fill='both')
        self.btn_create.pack(side='right', padx=2)
        btn_cancel.pack(side='right', padx=2)

        self.geometry('400x150')
        self.resizable(False, False)

    def create_db(self):
        """Create a directories trees and db"""
        # create main directories
        self.db_main_path.mkdir(parents=True, exist_ok=True)

        # create directories
        db_directories = ['thumbnails',
                          'faces',]
        for d in db_directories:
            self.db_main_path.joinpath(d).mkdir(parents=True, exist_ok=True)

        # create db
        db_version = self.master.APP_VERSION.split(".")[1]
        self.db_file_path = self.db_main_path.joinpath('db.db')
        self.con = connect_sqlite(self.db_file_path)
        cur = self.con.cursor()

        with open(pathlib.Path(self.master.APP_START_POINT).joinpath('db/install').joinpath(f'{db_version}.sql'), 'r') as script_new_db:
            cur.executescript(script_new_db.read())

        init_data_informations = [
            ('db_version', db_version, self.master.APP_USER, self.master.APP_USER),
            ('db_token', hashlib.md5(str(time.time()).encode()).hexdigest(), self.master.APP_USER, self.master.APP_USER),
        ]

        cur.executemany('''INSERT INTO db_informations (information, value, created_by, modified_by)
                        VALUES (?, ?, ?, ?)''', init_data_informations)

        # init_data_settings = [
        #     ('max_thumbnail_resolution', '500.500', self.master.APP_USER, self.master.APP_USER),
        # ]

        # cur.executemany('''INSERT INTO db_settings (setting, value, created_by, modified_by)
        #                 VALUES (?, ?, ?, ?)''', init_data_settings)
        self.con.commit()
        self.con.close()

        self.destroy()

    def select_directory(self):
        direcotry_path = filedialog.askdirectory()
        self.ent_path_db.delete(0, tk.END)
        self.ent_path_db.insert(0, direcotry_path)

    def check_path(self, *args):
        """Validate path to directory and set variable"""

        self.db_main_path = pathlib.Path(self.entry_path_db.get())
        self.set_warning_information("")
        btn_state = 'active'

        if not self.db_main_path.is_absolute() and btn_state == 'active':
            self.set_warning_information("Path is not valid")
            btn_state = 'disabled'

        if btn_state == 'active':
            if self.db_main_path.is_dir():
                if list(self.db_main_path.iterdir()):
                    self.set_warning_information("Directory is not empty")
                    btn_state = 'disabled'
            elif self.db_main_path.is_file():
                self.set_warning_information("This is a file")
                btn_state = 'disabled'
                # else:
                #     self.set_warning_information("This is not a directory")
                #     btn_state = 'disabled'

        if not self.db_main_path.exists() and btn_state == 'active':
            self.set_warning_information("The directory does not exist, it will be created")

        self.btn_create.configure(state=btn_state)

    def set_warning_information(self, information):
        self.lbl_warning.configure(text=information)


if __name__ == "__main__":
    from main_window import mainWindow
    root = mainWindow()
    root.new_db()
    root.mainloop()
