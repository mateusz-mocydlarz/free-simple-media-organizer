# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import gettext
import sqlite3
import os.path

_ = gettext.gettext


class DialogNewDb(tk.Tk):
    """Dialog to create new database"""

    def __init__(self):
        super().__init__()
        self.title(_("Create new media database"))
        # self.resizable(width=False, height=False)

        self.dlg_frm_info = ttk.Frame(self)
        self.dlg_frm_info.pack(fill="x", padx=10, pady=10)

        self.dlg_lbl_info = ttk.Label(self.dlg_frm_info, text=_("Choose direcotry to create database (must by empty):"))
        self.dlg_lbl_info.pack(side="left")

        self.dlg_frm_path = ttk.Frame(self)
        self.dlg_frm_path.pack(fill="x", padx=10)

        self.dlg_ent_path = ttk.Entry(self.dlg_frm_path)
        self.dlg_ent_path.pack(side="left", expand=True, fill="x")

        self.dlg_btn_path = ttk.Button(self.dlg_frm_path, text=_("Browse..."), command=self.dialog_path_to_db)
        self.dlg_btn_path.pack(side="left")

        self.dlg_frm_warning = ttk.Frame(self)
        self.dlg_frm_warning.pack(fill="x", padx=10)

        self.dlg_lbl_warning = ttk.Label(self.dlg_frm_warning, text=_(""), foreground="red")
        self.dlg_lbl_warning.pack(side="left")

        self.dlg_frm_navi = ttk.Frame(self)
        self.dlg_frm_navi.pack(fill="both", padx=10, pady=10, expand=True)

        self.dlg_btn_next = ttk.Button(self.dlg_frm_navi, text=_("Next"), command=self.dialog_next)
        self.dlg_btn_next.pack(side="right", anchor="se")
        self.dlg_btn_cancel = ttk.Button(self.dlg_frm_navi, text=_("Cancel"), command=self.destroy)
        self.dlg_btn_cancel.pack(side="right", anchor="se")

        self.update()

        self.minsize(width=self.winfo_width(), height=self.winfo_height())

    def dialog_path_to_db(self):
        dialog = filedialog.askdirectory()
        self.dlg_ent_path.delete(0, tk.END)
        self.dlg_ent_path.insert(0, dialog)

    def dialog_next(self):
        with open(os.path.join(os.path.dirname(__file__), "database", "init.sql")) as script_file:
            script = script_file.read()

        con = sqlite3.connect(os.path.join(self.dlg_ent_path.get(), "database.db"), isolation_level=)
        cur = con.cursor()
        cur.executescript(script)
        con.close()

        print("end")


if __name__ == "__main__":
    dialog_new_db = DialogNewDb()
    dialog_new_db.mainloop()
