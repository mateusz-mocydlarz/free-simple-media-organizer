from gui.gui_main_window import GuiMainWindow


class MainWindow(GuiMainWindow):
    """_summary_

    Args:
        GuiMainWindow (_type_): _description_
    """

    def __init__(self):
        super().__init__()

        self.title("test")


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()
