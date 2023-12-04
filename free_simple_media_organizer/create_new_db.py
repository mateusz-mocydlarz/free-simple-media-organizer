import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import sqlite3


class createNewDb(tk.Toplevel):
    """Create new database

    Args:
        master: master window
    """

    con = False

    def __init__(self, master: tk.Tk):
        super().__init__(master)

        frm_new_db = tk.Frame(self)
        frm_label = tk.Frame(frm_new_db)
        frm_path = tk.Frame(frm_new_db)
        frm_warning = tk.Frame(frm_new_db)
        frm_control = tk.Frame(frm_new_db)

        lbl_new_db = ttk.Label(frm_label, text="Select empy directory, to create new db:")

        self.entry_path_db = tk.StringVar()
        self.entry_path_db.trace("w", self.check_path)
        self.ent_path_db = ttk.Entry(frm_path, textvariable=self.entry_path_db)
        btn_path_db = ttk.Button(frm_path, text="Select directory", command=self.select_dictionary)

        self.lbl_warning = tk.Label(frm_warning, fg="red")

        btn_cancel = ttk.Button(frm_control, text="Cancel", command=self.destroy)
        self.btn_create = ttk.Button(frm_control, text="Create", command=self.next_dialog, state="disabled")

        frm_new_db.pack(fill="both", padx=10, pady=10, expand=True)

        frm_label.pack(side="top", fill="x")
        lbl_new_db.pack(side="left")

        frm_path.pack(fill="both")
        self.ent_path_db.pack(side="left", fill="x", expand=True)
        btn_path_db.pack()

        frm_warning.pack(fill="both")
        self.lbl_warning.pack(side="left")

        frm_control.pack(side="bottom", fill="both")
        self.btn_create.pack(side="right", padx=2)
        btn_cancel.pack(side="right", padx=2)

        self.geometry("400x150")
        self.resizable(False, False)

    def next_dialog(self):
        """Create a directories trees and db"""
        # create main directories
        os.makedirs(self.ent_path_db.get(), exist_ok=True)

        # create directories
        db_directories = ["thumbnails",
                          "faces",]
        for d in db_directories:
            os.makedirs(os.path.join(self.ent_path_db.get(), d), exist_ok=True)

        # create db
        db_version = self.master.APP_VERSION.split(".")[1]
        con = sqlite3.connect(os.path.join(self.ent_path_db.get(), "db.db"))
        con.execute("PRAGMA foreign_keys = ON")
        cur = con.cursor()

        with open(os.path.normpath(os.path.join(self.master.APP_START_POINT,
                                                "db/install",
                                                f"{db_version}.sql")), "r") as script_new_db:
            cur.executescript(script_new_db.read())

        init_data_informations = [
            ("db_version", db_version, self.master.APP_USER, self.master.APP_USER),
        ]

        cur.executemany("""INSERT INTO db_informations (information, value, created_by, modified_by)
                        VALUES (?, ?, ?, ?)""", init_data_informations)

        init_data_settings = [
            ("max_thumbnail_resolution", "500.500", self.master.APP_USER, self.master.APP_USER),
        ]

        cur.executemany("""INSERT INTO db_settings (setting, value, created_by, modified_by)
                        VALUES (?, ?, ?, ?)""", init_data_settings)
        con.commit()

        self.con = con

        con.close()

        self.destroy()

    def select_dictionary(self):
        direcotry_path = filedialog.askdirectory()
        self.ent_path_db.delete(0, tk.END)
        self.ent_path_db.insert(0, direcotry_path)

    def check_path(self, *args):
        """Validate path to directory"""

        if os.path.isabs(self.entry_path_db.get()):
            if os.path.exists(self.entry_path_db.get()):
                if os.path.isdir(self.entry_path_db.get()):
                    if os.listdir(self.ent_path_db.get()):
                        self.set_warning_information("Directory is not empty")
                        self.btn_create.configure(state="disabled")
                    else:
                        self.set_warning_information("")
                        self.btn_create.configure(state="active")
                elif os.path.isfile(self.entry_path_db.get()):
                    self.set_warning_information("This is a file")
                    self.btn_create.configure(state="disabled")
            else:
                # print(os.path.splitdrive(self.entry_path_db.get()))
                self.set_warning_information("The directory does not exist, it will be created")
                self.btn_create.configure(state="active")
        else:
            self.set_warning_information("Path is not valid")
            self.btn_create.configure(state="disabled")

    def set_warning_information(self, information):
        self.lbl_warning.configure(text=information)


if __name__ == "__main__":
    root = tk.Tk()
    root.APP_VERSION = "v01.001.001.00"
    root.APP_START_POINT = os.path.dirname(__file__)
    root.APP_USER = "host/user"
    dialog = createNewDb(root)
    dialog.mainloop()
