from tkinter import *
from PIL import Image, ImageTk

from helpers import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

    def update():
        load = Image.open("images/pose2.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        root.after(1000, update)

    update()


root = Tk()
app = Window(root)

root.geometry("1000x1000")
root.wm_title("Yoga Poses")

root.mainloop()