# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, filedialog


class MainWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Free simple media organizer")

        self.menu_bar = tk.Menu(self)

        self.menu_db = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_db.add_command(label="New...", command=self.dialog_new_db)
        self.menu_db.add_command(label="Open...")
        self.menu_db.add_command(label="Close database")
        self.menu_db.entryconfig("Close database", state="disabled")
        self.menu_bar.add_cascade(label="Database", menu=self.menu_db)

        self.menu_media = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_media.add_command(label="Sources...")
        self.menu_bar.add_cascade(label="Media", menu=self.menu_media)

        # self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # self.filemenu.add
        # self.filemenu.add_command(label="New", command=self.quit)
        # self.filemenu.add_command(label="Open", command=self.quit)
        # self.filemenu.add_command(label="Save", command=self.quit)
        # self.filemenu.add_separator()
        # self.filemenu.add_command(label="Exit", command=self.quit)
        # self.menubar.add_cascade(label="File", menu=self.filemenu)

        # self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        # self.helpmenu.add_command(label="Help Index", command=self.quit)
        # self.helpmenu.add_command(label="About...", command=lambda: self.donothing_test("about"))
        # self.menubar.add_cascade(label="Help", menu=self.helpmenu)

        self.config(menu=self.menu_bar)

    def dialog_new_db(self):
        new_db = filedialog.askdirectory()
        print(new_db)


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
