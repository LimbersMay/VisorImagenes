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
        self.image_display_roll = ImageDisplayRoll(self)
        self.image_display = ImageDisplay(self)

        # Layout of the window
        self.image_display_roll.grid(row=0, column=0)
        self.image_display.grid(row=0, column=1)


class ImageDisplayRoll(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(
            width=300,
            height=500,
            bg="brown",
        )


class ImageDisplay(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(
            width=500,
            height=500,
            bg="darkred",
        )
