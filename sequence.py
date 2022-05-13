
import _tkinter as tk

from helpers import *
from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        yoga_pose = sequence()

        # intialise label
        text = Label(self, text="".join(yoga_pose), fg="Green", font=("Helvetica", 18))
        text.place(x=40,y=0)
        #text.pack()
        

        # initialise exit button
        self.pack(fill=BOTH, expand=1)
        exitButton = Button(self, text="Exit", command=self.clickExitButton)
        exitButton.place(x=0, y=0)

    # exit button callback
    def clickExitButton(self):
        exit()

def sequence():
    return("Sun Salutation \n",
    standing(),
    standing(),
    standing(), "\n",
    seated(), "\n",
    twist(), "\n",
    fold(), "\n",
    seated(), "\n",
    inversion(), "\n",
    backbend(), "\n",
    "Shavasana")



# intitialise tkinter     
root = Tk()
app = Window(root)

# window size
root.geometry("700x500")


# set window title
root.wm_title("Window")

# show window
root.mainloop()
