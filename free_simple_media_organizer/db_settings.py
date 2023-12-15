import tkinter as tk
from tkinter import ttk
import sqlite3


class dbSettings(tk.Toplevel):
    """Database settings

    Args:
        master: master window
        con: connection to db
    """

    db_settings_value = {
        'photo.thumbnail.max_side_length': {
            'description': "The maximum side length of the thumbnail in pixels",
            'value': '500'
            },
        'photo.thumbnail.quality': {
            'description': "Thumbnail quality",
            'value': '50'
            },
        'photo.face_recognition': {
            'description': "Face recognition in photos",
            'value': '1'
            },
        'photo.face_recognition.level': {
            'description': "Face recognition level in photos",
            'value': '90'
            },
        'video.thumbnail.max_resolution': {
            'description': "Maximum video resolution",
            'value': '480'
            },
        'video.face_recognition': {
            'description': "Face recognition in videos",
            'value': '1'
            },
        'video.face_recognition_level': {
            'description': "Face recognition level in photos",
            'value': '90'
            },
        'video.face_recognition_precision': {
            'description': "Maximum length of the photo side in pixels",
            'value': '30'
            }
        }

    def __init__(self, master: tk.Tk, con: sqlite3.connect):
        super().__init__(master)

        frm_main = tk.Frame(self)
        frm_main.pack(fill="both", padx=10, pady=10, expand=True)

        frm_grid = tk.Frame(frm_main)
        frm_grid.pack()

        grid_row = 0
        for setting in self.db_settings_value.keys():
            frm_grid = tk.Frame(frm_grid)
            frm_grid.grid(row=grid_row, column=0, padx=[0, 5], sticky='e')
            lbl_setting = ttk.Label(frm_grid, text=setting)
            lbl_setting.pack()

            frm_grid = tk.Frame(frm_grid)
            frm_grid.grid(row=grid_row, column=1)
            ent_setting = ttk.Entry(frm_grid)
            ent_setting.insert(0, self.db_settings_value[setting])
            ent_setting.pack()

            grid_row += 1

        frm_control = tk.Frame(frm_main)
        btn_cancel = ttk.Button(frm_control, text="Cancel", command=self.destroy)
        btn_save = ttk.Button(frm_control, text="Save")   #, command=self.create_db, state="disabled")
        frm_control.pack(side='bottom', fill='both', pady=[5, 0])
        btn_save.pack(side='right', padx=[5, 0])
        btn_cancel.pack(side='right', padx=[5, 0])
        self.resizable(False, False)


if __name__ == "__main__":
    from main_window import mainWindow
    root = mainWindow()
    root.con = sqlite3.connect('C:/Users/mateu/Qsync/Programming/tmp_free-simple-media-organizer/db/db.db')
    root.db_settings()
    root.mainloop()
