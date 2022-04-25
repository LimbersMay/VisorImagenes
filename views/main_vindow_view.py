from tkinter import *


class MainWindowView(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Images visor")

        # Configurations of the window
        self.config(
            width=500,
            height=500,
            bg="#fff",
        )
