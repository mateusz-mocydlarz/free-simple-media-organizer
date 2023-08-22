# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import gettext
import sqlite3
import pathlib
from functions.get_hostname_user import get_hostname_user

_ = gettext.gettext


class DialogDbSettings(tk.Toplevel):
    """Dialog to settings database"""

    def __init__(self, parent: tk.Tk, path_to_db: pathlib.Path):
        super().__init__(parent)
        self.path_to_db = path_to_db
        self.title(_("Settings database"))
        # self.resizable(width=False, height=False)

        self.db_setting = dict()
        self.is_new_db_setting = list()
        con = sqlite3.connect(self.path_to_db)
        cur = con.cursor()
        for row in cur.execute("SELECT setting, value FROM db_settings"):
            self.db_setting[row[0]] = row[1]
        con.close()

        self.dlg_frm_settings = ttk.Frame(self)
        self.dlg_frm_settings.pack(fill="x", padx=10, pady=10)

        self.dlg_lbl_create_thumbnails = ttk.Label(self.dlg_frm_settings, text=_("Create thumbnails?"))
        self.dlg_lbl_create_thumbnails.grid(row=0, column=0, sticky="w")

        if "create_thumbails" not in self.db_setting.keys():
            self.db_setting["create_thumbails"] = "1"
            self.is_new_db_setting.append("create_thumbails")
        self.var_chb_create_thumbnails = tk.StringVar(value=self.db_setting["create_thumbails"])
        self.dlg_chb_create_thumbnails = ttk.Checkbutton(self.dlg_frm_settings,
                                                         text=_("Yes"),
                                                         variable=self.var_chb_create_thumbnails,
                                                         command=self.change_dlg_chb_create_thumbnails)
        self.dlg_chb_create_thumbnails.grid(row=0, column=1, sticky="w")

        self.dlg_lbl_max_thumbnails = ttk.Label(self.dlg_frm_settings, text=_("The maximum side length of the thumbnail [px]:"))
        self.dlg_lbl_max_thumbnails.grid(row=5, column=0, sticky="w")

        if "max_thumbails" not in self.db_setting.keys():
            self.db_setting["max_thumbails"] = "500"
            self.is_new_db_setting.append("max_thumbails")
        self.dlg_ent_max_thumbnails = ttk.Entry(self.dlg_frm_settings, width=5)
        self.dlg_ent_max_thumbnails.insert(0, self.db_setting["max_thumbails"])
        self.dlg_ent_max_thumbnails.grid(row=5, column=1, sticky="w")

        self.dlg_btn_save = ttk.Button(self.dlg_frm_settings, text=_("Save"), command=self.save_setting)
        self.dlg_btn_save.grid(row=10, column=1, sticky="se")

        self.change_dlg_chb_create_thumbnails()
        self.update()
        self.minsize(width=self.winfo_width(), height=self.winfo_height())

    def save_setting(self):
        new_db_setting = dict()
        new_db_setting["create_thumbails"] = self.var_chb_create_thumbnails.get()
        new_db_setting["max_thumbails"] = self.dlg_ent_max_thumbnails.get()

        insert_list_values = list()
        update_list_values = list()
        for setting in self.db_setting.keys():
            if setting in self.is_new_db_setting:
                insert_list_values.append((setting, new_db_setting[setting], get_hostname_user(), get_hostname_user()))
            else:
                if self.db_setting[setting] != new_db_setting[setting]:
                    update_list_values.append((new_db_setting[setting], get_hostname_user(), setting))

        if len(insert_list_values) > 0 or len(update_list_values) > 0:
            con = sqlite3.connect(self.path_to_db)
            cur = con.cursor()
            if len(insert_list_values) > 0:
                cur.executemany("""INSERT INTO db_settings (setting, value, created_by, modified_by, creation_date, modification_date)
                                VALUES (?, ?, ?, ?, datetime('now','localtime'), datetime('now','localtime'))""", insert_list_values)
            if len(update_list_values) > 0:
                cur.executemany("""UPDATE db_settings SET value = ?, modified_by = ?, modification_date = datetime('now','localtime')
                                WHERE setting = ?""", update_list_values)
            con.commit()
            con.close()

        self.destroy()

    def change_dlg_chb_create_thumbnails(self):
        if self.var_chb_create_thumbnails.get() == "0":
            self.dlg_lbl_max_thumbnails.config(state=tk.DISABLED)
            self.dlg_ent_max_thumbnails.config(state=tk.DISABLED)
        else:
            self.dlg_lbl_max_thumbnails.config(state=tk.NORMAL)
            self.dlg_ent_max_thumbnails.config(state=tk.NORMAL)


if __name__ == "__main__":
    parent = tk.Tk()
    path_to_db = pathlib.Path("/Users/mocny/Documents/programming/python/free-simple-media-organizer/.tmp/2/database.db")
    dialog_new_db = DialogDbSettings(parent, path_to_db)
    dialog_new_db.grab_set()
    parent.mainloop()
