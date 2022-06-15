from tkinter import *
from PIL import Image, ImageTk
from random import *
root = Tk()

class Pose:
   
   # data members
   name = "Crow Pose"
   image_add = "images/pose6"
   info = "some pose information"
   sanskrit = "Bakasana"

   # class constructor
   def __init__(self, name, image_add, info, sanskrit):
       self.name = name
       self.image_add = image_add
       self.info = info
       self.sanskrit = sanskrit

   # user defined function of class
   def func(self):
      print("After calling func() method..")
      print("My pose's name is", self.name)
      print("The address of its image is", self.image_add)
      print("Information about the pose:", self.info)
      print("Its sanskrit name is", self.sanskrit)

# create instance
pose1 = Pose("Crow Pose", "images/pose5", "some info", "Bakasana")

# apply function to instance
pose1.func()

# access the attribute
print("\nDirect access of attributes using object..")
print(f"The name of the pose is {pose1.name}")

