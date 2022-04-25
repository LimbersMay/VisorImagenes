from tkinter import *


class MainWindowView(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        master.title("Images visor")

        # Configurations of the window
        self.config(
            width=800,
            height=500,
            bg="#fff",
        )

        self.grid_propagate(False)

        # Parts of the window
        self.image_display = ImageDisplayRoll(self)

        # Layout of the window
        self.image_display.grid(row=0, column=0)


class ImageDisplayRoll(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(
            width=300,
            height=500,
            bg="brown",
        )
