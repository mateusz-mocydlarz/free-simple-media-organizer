# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import gettext
import platformdirs
import json

platformdirs.user_config_dir("free_simple_media_organizer")

platformdirs.user_config_path("free_simple_media_organizer")

_ = gettext.gettext

class DialogNewDb(tk.Tk):
    """Dialog to create new database"""

    def __init__(self):
        super().__init__()
        self.title(_("Create new media database"))
        self.resizable(width=False, height=False)

        frm_info = ttk.Frame(self)
        frm_info.pack(fill="x", padx=10, pady=10)

        lbl_info = ttk.Label(frm_info, text=_("Choose direcotry to create database (must by empty):"))
        lbl_info.pack(side="left")

        frm_path = ttk.Frame(self)
        frm_path.pack(fill="x", padx=10)

        ent_path = ttk.Entry(frm_path)
        ent_path.pack(side="left", expand=True, fill="x")

        btn_path = ttk.Button(frm_path, text=_("Browse..."), command=self.dialog_path_to_db)
        btn_path.pack(side="left")

        frm_warning = ttk.Frame(self)
        frm_warning.pack(fill="x", padx=10)

        lbl_warning = ttk.Label(frm_warning, text=_(""), foreground="red")
        lbl_warning.pack(side="left")

        frm_navi = ttk.Frame(self)
        frm_navi.pack(fill="x", padx=10, pady=10, expand=True)

        btn_next = ttk.Button(frm_navi, text=_("Next"), command=self.dialog_next)
        btn_next.pack(side="right", anchor="se")
        btn_cancel = ttk.Button(frm_navi, text=_("Cancel"), command=self.destroy)
        btn_cancel.pack(side="right", anchor="se")

        self.update()

        self.minsize(width=self.winfo_width(), height=10)

    def dialog_path_to_db(self):
        dialog = filedialog.askdirectory()
        print(dialog)

    def dialog_next(self):
        print(self.winfo_width())


if __name__ == "__main__":
    dialog_new_db = DialogNewDb()
    dialog_new_db.mainloop()
