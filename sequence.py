
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from helpers import *


# intitialise tkinter     
root = Tk()
# window size
root.geometry("700x900")
# set window title
root.wm_title("Yoga Sequencer")

i = 0



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        yoga_pose = sequence()

        pose_image = Label(root)
        pose_image.place(x= 40, y =50)


        # place pose name in window
        pose_name = Label(self, text="", fg="Green", font=("Helvetica", 18))
        pose_name.place(x=40,y=450)
        #text.pack()

        ## place image under pose name
        # load images
        image1 = Image.open('images/pose1.jpg')
        image1 = image1.resize((500,400), Image.ANTIALIAS)

        image2 = Image.open('images/pose2.jpg')
        image2 = image2.resize((500,400), Image.ANTIALIAS)

        image3 = Image.open('images/pose3.jpg')
        image3 = image3.resize((500,400), Image.ANTIALIAS)

        image4 = Image.open('images/pose4.jpg')
        image4 = image4.resize((500,400), Image.ANTIALIAS)

        image5 = Image.open('images/pose5.jpg')
        image5 = image5.resize((500,400), Image.ANTIALIAS)

        image6 = Image.open('images/pose6.jpg')
        image6 = image6.resize((500,400), Image.ANTIALIAS)

        

        # make images usable for tkinter labels
        img1 = ImageTk.PhotoImage(image1)
        img2 = ImageTk.PhotoImage(image2)
        img3 = ImageTk.PhotoImage(image3)
        img4 = ImageTk.PhotoImage(image4)
        img5 = ImageTk.PhotoImage(image5)
        img6 = ImageTk.PhotoImage(image6)

        # make list of images
        images = [img1, img2, img3, img4, img5, img6]
        names = [standing(), seated(), twist(), inversion(), backbend(), "Shavasana"]
        
        def start():
            global i # use global i
            pose_image['image'] = images[i]
            pose_name["text"] = names[i]
            if i < len(images)-1:
                i +=1
                root.after(2000, start) # run update again with i+1

        # create buttons
        btnStart = Button(self, text="Start", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE, command=start)
        btnStart.place(x=550, y=50)

        btnPause = Button(self, text="Pause", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE, command=start)
        btnPause.place(x=550, y=120)

        btnInfo = Button(self, text="Info", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE, command=start)
        btnInfo.place(x=550, y=190)

        btnExit = Button(self, text="Exit", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE, command=self.clickExitButton)
        btnExit.place(x=550, y=260)

        self.pack(fill=BOTH, expand=1)
        
    # exit button callback
    def clickExitButton(self):
        exit()
    
def sequence():
    return(standing(),
    )



app = Window(root)
# show window
root.mainloop()
