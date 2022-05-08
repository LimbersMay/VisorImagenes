from tkinter import *
from PIL import ImageTk, Image


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
        self.image_display = ImageDisplayComplete(self)

        # Layout of the window
        self.image_display_roll.grid(row=0, column=0)
        self.image_display.grid(row=0, column=1)


class ImageDisplayComplete(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(
            width=500,
            height=500,
            bg="darkred",
        )


class ImageDisplayRoll(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.config(
            width=200,
            height=500,
            bg="brown",
        )

        self.grid_propagate(False)

        # Parts of the window
        self.image_miniature = ImageMiniature(self)

        # Layout of the window
        self.image_miniature.grid(row=0, column=0)


class ImageMiniature(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.path = "resources/images/wallpaper.jpg"

        self.image = Image.open(self.path)
        self.photo_image = ImageTk.PhotoImage(self.image.resize((180, 150)))

        self.image_label = Label(self, image=self.photo_image)
        self.image_label.grid(row=0, column=0)

        self.config(
            width=200,
            height=150,
            bg="green",
        )
