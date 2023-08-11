# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk

main_window = tk.Tk()

label_first = ttk.Label(main_window, text="Testowy tkst")
label_first.pack(side=tk.LEFT)
entry_name = ttk.Entry(main_window)
entry_name.pack(side=tk.LEFT)
entry_name.insert(20, "test")

menu_bar = tk.Menu(main_window)
main_window.config(menu=menu_bar)

ttk.men

if __name__ == "__main__":
    main_window.mainloop()