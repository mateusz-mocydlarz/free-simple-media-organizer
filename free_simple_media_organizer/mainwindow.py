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
        self.menu_db.add_command(label=_("Close database"), state=tk.DISABLED)
        self.menu_db.add_separator()
        self.menu_db.add_command(label=_("Settings..."), command=self.dialog_db_settings, state=tk.DISABLED)

        self.menu_media = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=_("Media"), menu=self.menu_media)
        self.menu_media.add_command(label=_("Sources..."), state=tk.DISABLED)

        self.menu_settings = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label=_("Settings"), menu=self.menu_settings)

        self.config(menu=self.menu_bar)

    def menu_bar_state(self, in_state: bool):
        if in_state is False:
            tk_state = tk.DISABLED
        else:
            tk_state = tk.NORMAL

        self.menu_bar.entryconfig(_("Database"), state=tk_state)
        self.menu_bar.entryconfig(_("Media"), state=tk_state)
        self.menu_bar.entryconfig(_("Settings"), state=tk_state)

    def dialog_new_db(self):
        self.menu_bar_state(False)
        dialog_new_db = dialognewdb.DialogNewDb(self)
        dialog_new_db.grab_set()

    def dialog_db_settings(self):
        self.menu_bar_state(False)
        dialog_new_db = dialogdbsettings.DialogDbSettings(self)
        dialog_new_db.grab_set()


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
