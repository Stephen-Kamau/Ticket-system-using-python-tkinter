# an advanced ticket app using object oriented pyhton programming

#imports
from tkinter import*
from tkinter import filedialog,messagebox ,Tk, StringVar ,ttk ,messagebox
import random
import time;
import datetime
root=Tk()

#class definition
class guiDefinition:
	def __init__(self,root):
		#crate window for the application

		self.root = root
		#title for the application
		self.root.title("Ticket app advance")
		self.add_frames()
		self.top_definition()
		self.configs()



	def configs(self):
		self.root.configure(background="cyan")

	

	def add_frames(self):
		#main frames definition
		self.top= Frame (self.root,width=1400,height=80,bd=6,relief='raised').pack(side=TOP)
		#self.top.configure(background='white')
		#ints backround color
		self.f1 = Frame (self.root,width=900,height=660,bd=5,relief='sunken').pack(side=LEFT)
		#self.f1.configure(background='black')
		self.f2 = Frame (self.root,width=500,height=660,bd=5,relief='sunken').pack(side=RIGHT)
		#self.f2.configure(background='black')

		#subFrames of of f2
		self.frametopright = Frame (self.f2,width=440,height=650,bd=12,relief='raised').pack(side=TOP)
		self.framebottomright = Frame (self.f2,width=440,height=50,bd=16,relief='raised').pack(side=BOTTOM)

		#sub frames of f1
		self.f1a = Frame (self.f1,width=1350,height=100,bd=14,relief='raised').pack(side=TOP)
		self.f2a = Frame (self.f1,width=1350,height=100,bd=14,relief='raised').pack(side=BOTTOM)
		self.topleft1 = Frame (self.f1a,width=300,height=200,bd=16,relief='raised').pack(side=LEFT)
		self.topleft2 = Frame (self.f1a,width=300,height=200,bd=16,relief='raised').pack(side=RIGHT)
		self.topleft3 = Frame (self.f1a,width=300,height=200,bd=16,relief='raised').pack(side=RIGHT)


		#>>>>>>>>>>>>>>>bottom frames <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
		self.bottomleft1 = Frame (self.f2a,width=450,height=450,bd=14,relief='raised').pack(side=LEFT)
		self.bottomleft2 = Frame (self.f2a,width=450,height=450,bd=14,relief='raised').pack(side=RIGHT)


	def top_definition(self):
		self.sys_title= Label (self.top,font=('arial',35,'bold'),bd=7,width=35,text='New System dela Advance',justify='center').pack(side=LEFT)

	#add_frames(root)
	

guiDefinition(root)
root.mainloop()