
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from helpers import *


# intitialise tkinter     
root = Tk()
# window size
root.geometry("700x700")
# set window title
root.wm_title("Yoga Sequencer")

i = 0



class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        
        

        # set background color
        self.configure(bg = "blue")

        pose_image = Label(root)
        pose_image.place(x= 40, y =50)


        # place pose name in window
        pose_name = Label(self, text="", fg="Green", font=("Helvetica", 18))
        pose_name.place(x=40,y=450)
        #text.pack()

        ## place image under pose name
        # load images
        Bow = Image.open('images/Bow.jpg')
        Bow = Bow.resize((500,400), Image.ANTIALIAS)

        Camel = Image.open('images/Camel.jpg')
        Camel = Camel.resize((500,400), Image.ANTIALIAS)

        Cobra = Image.open('images/Cobra.jpg')
        Cobra = Cobra.resize((500,400), Image.ANTIALIAS)

        DownwardDog = Image.open('images/DownwardDog.jpg')
        DownwardDog = DownwardDog.resize((500,400), Image.ANTIALIAS)

        ForwardFold = Image.open('images/ForwardFold.jpg')
        ForwardFold = ForwardFold.resize((500,400), Image.ANTIALIAS)

        Plough = Image.open('images/Plough.jpg')
        Plough = Plough.resize((500,400), Image.ANTIALIAS)

        SeatedTwist = Image.open('images/SeatedTwist.jpg')
        SeatedTwist = SeatedTwist.resize((500,400), Image.ANTIALIAS)

        Shavasana = Image.open('images/Shavasana.jpg')
        Shavasana = Shavasana.resize((500,400), Image.ANTIALIAS)

        Triangle = Image.open('images/Triangle.jpg')
        Triangle = Triangle.resize((500,400), Image.ANTIALIAS)

        Warrior1 = Image.open('images/Warrior1.jpg')
        Warrior1 = Warrior1.resize((500,400), Image.ANTIALIAS)

        Warrior2 = Image.open('images/Warrior2.jpg')
        Warrior2 = Warrior2.resize((500,400), Image.ANTIALIAS)

        Wheel = Image.open('images/Wheel.jpg')
        Wheel = Wheel.resize((500,400), Image.ANTIALIAS)


        

        # make images usable for tkinter labels
        img1 = ImageTk.PhotoImage(Bow)
        img2 = ImageTk.PhotoImage(Camel)
        img3 = ImageTk.PhotoImage(Cobra)
        img4 = ImageTk.PhotoImage(DownwardDog)
        img5 = ImageTk.PhotoImage(ForwardFold)
        img6 = ImageTk.PhotoImage(Plough)
        img7 = ImageTk.PhotoImage(SeatedTwist)
        img8 = ImageTk.PhotoImage(Shavasana)
        img9 = ImageTk.PhotoImage(Triangle)
        img10 = ImageTk.PhotoImage(Warrior1)
        img11 = ImageTk.PhotoImage(Warrior2)
        img12 = ImageTk.PhotoImage(Wheel)

        names = ["Downward Facing Dog Pose", "Forward Fold", "Bow Pose", "Camel Pose", "Cobra Pose", "Plough Pose", "Seated Twist Pose", "Triangle Pose", "Warrior 1 Pose", "Warrior 2 Pose", "Wheel Pose"]


        # rudimentry version of random sequence generator
        sequence = [random.choice(names), random.choice(names), random.choice(names), random.choice(names), random.choice(names), random.choice(names), "Shavasana"]
        
        # dictionary associating pose names with images
        images = {"Bow Pose": img1, "Camel Pose": img2, "Cobra Pose": img3, "Downward Facing Dog Pose": img4, "Forward Fold": img5, "Plough Pose" :img6, "Shavasana" : img8, "Seated Twist Pose" : img7, "Triangle Pose" : img9, "Warrior 1 Pose" : img10, "Warrior 2 Pose" : img11, "Wheel Pose" : img12 }
    
        # button functions
        def start():
            global i # use global i
            pose_name["text"] = sequence[i]
            try:
                pose_image['image'] = images[pose_name["text"]]
            except KeyError:
                pose_image["image"] = images["Bow Pose"]
            if i < len(sequence) - 1 :
                i += 1
                root.after(5000, start) # run update again with i+1
            

        # create buttons
        btnStart = Button(self, text="Start", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE, command=start)
        btnStart.place(x=550, y=50)

        btnExit = Button(self, text="Exit", bg='black', fg='gold', width=6, font=('ariel 20 bold'), relief=GROOVE, command=self.clickExitButton)
        btnExit.place(x=550, y=260)

        self.pack(fill=BOTH, expand=1)
        
    # exit button callback
    def clickExitButton(self):
        exit()
    
app = Window(root)
# show window
root.mainloop()
