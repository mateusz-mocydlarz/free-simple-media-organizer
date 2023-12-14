import tkinter as tk
from tkinter import ttk
import sqlite3


class dbSettings(tk.Toplevel):
    """Database settings

    Args:
        master: master window
        con: connection to db
    """

    db_settings_value = {'photo.thumbnail_max_side_length': '500',
                         'photo.face_recognition': '1',
                         'photo.face_recognition_level': '90',
                         'video.thumbnail_max_side_length': '480',
                         'video.face_recognition': '1',
                         'video.face_recognition_precision': '30',
                         'video.face_recognition_level': '90'}

    def __init__(self, master: tk.Tk, con: sqlite3.connect):
        super().__init__(master)

        frm_db_settings = tk.Frame(self)
        frm_db_settings.pack(fill="both", padx=10, pady=10, expand=True)
        frm_grid_main = tk.Frame(frm_db_settings)
        frm_grid_main.pack()
        
        frm_control = tk.Frame(frm_db_settings, pady=5)
        btn_cancel = ttk.Button(frm_control, text="Cancel") #, command=self.destroy)
        btn_create = ttk.Button(frm_control, text="Save")   #, command=self.create_db, state="disabled")

        grid_row = 0
        for setting in self.db_settings_value.keys():
            frm_grid = tk.Frame(frm_grid_main)
            frm_grid.grid(row=grid_row, column=0, padx=[0,5], sticky='e')
            lbl_setting = ttk.Label(frm_grid, text=setting)
            lbl_setting.pack()

            frm_grid = tk.Frame(frm_grid_main)
            frm_grid.grid(row=grid_row, column=1)
            ent_setting = ttk.Entry(frm_grid)
            ent_setting.insert(0, self.db_settings_value[setting])
            ent_setting.pack()

            grid_row += 1

        frm_control.pack(side='bottom', fill='both')
        btn_create.pack(side='right', padx=2)
        btn_cancel.pack(side='right', padx=2)


if __name__ == "__main__":
    from main_window import mainWindow
    root = mainWindow()
    root.con = sqlite3.connect('C:/Users/mateu/Qsync/Programming/tmp_free-simple-media-organizer/db/db.db')
    root.db_settings()
    root.mainloop()
