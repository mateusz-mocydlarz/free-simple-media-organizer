import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os
import sqlite3


class dbSettings(tk.Toplevel):
    """Database settings

    Args:
        master: master window
        con: connection to db
    """

    def __init__(self, master: tk.Tk, con: sqlite3.connect):
        super().__init__(master)

        frm_new_db = tk.Frame(self)
        frm_label = tk.Frame(frm_new_db)
        frm_path = tk.Frame(frm_new_db)
        frm_warning = tk.Frame(frm_new_db)
        frm_next = tk.Frame(frm_new_db)

        lbl_new_db = ttk.Label(frm_label, text="Select empy directory, to create new db:")

        self.entry_path_db = tk.StringVar()
        self.entry_path_db.trace("w", self.check_path)
        self.ent_path_db = ttk.Entry(frm_path, textvariable=self.entry_path_db)
        btn_path_db = ttk.Button(frm_path, text="Select directory", command=self.select_dictionary)

        self.lbl_warning = tk.Label(frm_warning, fg="red")

        btn_cancel = ttk.Button(frm_next, text="Cancel", command=self.close_dialog)
        self.btn_next = ttk.Button(frm_next, text="Next >", command=self.next_dialog, state="disabled")

        frm_new_db.pack(fill="both", padx=10, pady=10, expand=True)

        frm_label.pack(side="top", fill="x")
        lbl_new_db.pack(side="left")

        frm_path.pack(fill="both")
        self.ent_path_db.pack(side="left", fill="x", expand=True)
        btn_path_db.pack()

        frm_warning.pack(fill="both")
        self.lbl_warning.pack(side="left")

        frm_next.pack(side="bottom", fill="both")
        self.btn_next.pack(side="right", padx=2)
        btn_cancel.pack(side="right", padx=2)

        self.geometry("400x150")
        self.resizable(False, False)



if __name__ == "__main__":
    root = tk.Tk()
    root.APP_VERSION = "v01.001.001.00"
    root.APP_START_POINT = os.path.dirname(__file__)
    root.APP_USER = "host/user"
    dialog = createNewDb(root)
    dialog.mainloop()
