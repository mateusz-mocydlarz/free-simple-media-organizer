import tkinter as tk
from tkinter import ttk
import pathlib

# from app_functions import connect_sqlite


class dbSettings(tk.Toplevel):
    """Database settings

    Args:
        master: master window
        con: connection to db
    """

    db_settings_value = {
        'photo.thumbnail': {
            'value': '1',
            'description': "Generating thumbnails for photos",
            'widget': 'checkbutton'
        },
        'photo.thumbnail.max_side_length': {
            'value': '500',
            'description': "The maximum side length of the thumbnail in pixels",
            'widget': 'entry'
        },
        'photo.thumbnail.quality': {
            'value': '50',
            'description': "Thumbnail quality for photo",
            'widget': 'combobox'
        },
        'photo.face_recognition': {
            'value': '1',
            'description': "Face recognition in photos",
            'widget': 'checkbutton'
        },
        'photo.face_recognition.level': {
            'value': '0.6',
            'description': "Face recognition level in photos",
            'widget': 'scale'
        },
        'video.thumbnail': {
            'value': '1',
            'description': "Generating thumbnails for videos",
            'widget': 'checkbutton'
        },
        'video.thumbnail.max_resolution': {
            'value': '480',
            'description': "Maximum video resolution",
            'widget': 'combobox'
        },
        'video.thumbnail.codec': {
            'value': 'h.264',
            'description': "Codec for thumbnails video",
            'widget': 'combobox'
        },
        'video.thumbnail.quality': {
            'value': '50',
            'description': "Thumbnail quality for video",
            'widget': 'combobox'
        },
        'video.face_recognition': {
            'value': '1',
            'description': "Face recognition in videos",
            'widget': 'checkbutton'
        },
        'video.face_recognition.level': {
            'value': '0.6',
            'description': "Face recognition level in videos",
            'widget': 'scale'
        },
    }

    def __init__(self, master: tk.Tk, db_file_path: pathlib.Path):
        super().__init__(master)

        frm_main = tk.Frame(self)
        frm_main.pack(fill='both', padx=10, pady=10, expand=True)

        frm_grid = tk.Frame(frm_main)
        frm_grid.pack()
        
        grid_row = 0
        for setting in self.db_settings_value.keys():
            frm_description = tk.Frame(frm_grid)
            frm_description.grid(row=grid_row, column=0, padx=[0, 5], sticky='e')
            lbl_description = ttk.Label(frm_description, text=f"{self.db_settings_value[setting]['description']}:")
            lbl_description.pack()
            
            frm_value = tk.Frame(frm_grid)
            frm_value.grid(row=grid_row, column=1, sticky='w', pady=[0, 5])

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
    root.db_file_path = pathlib.Path('C:/Users/mateu/Qsync/Programming/tmp_free-simple-media-organizer/db/db.db')
    root.db_settings()
    root.mainloop()
