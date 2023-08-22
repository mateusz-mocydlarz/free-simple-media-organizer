# -*- coding: utf-8 -*-
import tkinter as tk
import gettext
import dialognewdb
import dialogdbsettings

_ = gettext.gettext


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Free media library")

        self.menu_bar = tk.Menu(self)

        self.menu_db = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=_("Database"), menu=self.menu_db)
        self.menu_db.add_command(label=_("New..."), command=self.dialog_new_db)
        self.menu_db.add_command(label=_("Open..."))
        self.menu_db.add_command(label=_("Close database"))
        self.menu_db.add_separator()
        self.menu_db.add_command(label=_("Settings..."), command=self.dialog_db_settings)
        self.menu_db.entryconfig(_("Close database"), state=tk.DISABLED)
        self.menu_db.entryconfig(_("Settings..."), state=tk.DISABLED)

        self.menu_media = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=_("Media"), menu=self.menu_media)
        self.menu_media.add_command(label=_("Sources..."))

        self.menu_settings = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=_("Settings"), menu=self.menu_settings)

        self.config(menu=self.menu_bar)

    def open_dialog(self):
        self.menu_bar.entryconfig(_("Database"), state=tk.DISABLED)
        self.menu_bar.entryconfig(_("Media"), state=tk.DISABLED)
        self.menu_bar.entryconfig(_("Settings"), state=tk.DISABLED)

    def dialog_new_db(self):
        self.open_dialog()
        dialog_new_db = dialognewdb.DialogNewDb(self)
        dialog_new_db.grab_set_global()

    def dialog_db_settings(self):
        self.open_dialog()
        dialog_new_db = dialogdbsettings.DialogDbSettings(self)
        dialog_new_db.grab_set_global()


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
