# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import gettext
import sqlite3
# import os.path
from functions.check_path_new_database import check_path_new_database
import pathlib
from socket import gethostname
from getpass import getuser

_ = gettext.gettext


class DialogNewDb(tk.Toplevel):
    """Dialog to create new database"""

    def __init__(self, parent: tk.Tk):
        super().__init__(parent)
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
        self.dlg_btn_next.config(state=tk.DISABLED)
        self.dlg_btn_next.pack(side="right", anchor="se")
        self.dlg_btn_cancel = ttk.Button(self.dlg_frm_navi, text=_("Cancel"), command=self.destroy)
        self.dlg_btn_cancel.pack(side="right", anchor="se")

        self.update()

        self.minsize(width=self.winfo_width(), height=self.winfo_height())

    def dialog_path_to_db(self):
        dialog = filedialog.askdirectory()
        self.dlg_ent_path.delete(0, tk.END)
        self.dlg_ent_path.insert(0, dialog)
        check = check_path_new_database(self.dlg_ent_path.get())
        if check != "OK":
            self.dlg_lbl_warning.config(text=check)
        else:
            self.dlg_btn_next.config(state=tk.NORMAL)

    def dialog_next(self):
        # create dirs
        dir_thumbnails = pathlib.Path(self.dlg_ent_path.get(), "thumbnails")
        dir_thumbnails.mkdir(parents=True, exist_ok=True)
        dir_faces = pathlib.Path(self.dlg_ent_path.get(), "faces")
        dir_faces.mkdir(parents=True, exist_ok=True)

        # create database
        with open(pathlib.Path(pathlib.Path(__file__).parent, "database", "init.sql")) as script_file:
            script = script_file.read()

        con = sqlite3.connect(pathlib.Path(self.dlg_ent_path.get(), "database.db"))  # , isolation_level=)
        cur = con.cursor()
        cur.executescript(script)
        cur.execute("INSERT INTO app_informations VALUES (?, ?)", ("created_db_by", f"{ gethostname() }/{ getuser() }"))
        con.commit()
        con.close()

        self.destroy()


if __name__ == "__main__":
    parent = tk.Tk()
    dialog_new_db = DialogNewDb(parent)
    parent.mainloop()
