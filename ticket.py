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
		self.configs()
		self.add_frames()
		self.top_definition()
		self.add_labels()
		



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

	def add_labels(self):#this function is not working as needed...to be continued
		#...........................................subframes frame.....................................
		self.lblreceit= Label (self.frametopright,font=('arial',14,'bold'),bd=5,width=31,text='Travelling receits',justify='center').grid(row=0,column=0)
		self.lblclass1= Label (self.framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Class',justify='center').grid(row=0,column=0)
		self.lblclass2= Label (self.framebottomright,relief='sunken',textvariable=class1,font=('arial',14,'bold'),width=8,justify='center').grid(row=1,column=0)
		self.lblticket1= Label (self.framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Ticket',justify='center').grid(row=0,column=1)
		self.lblticket2= Label (self.framebottomright,relief='sunken',textvariable=fees,font=('arial',14,'bold'),width=8,justify='center').grid(row=1,column=1)
		self.lbladult1= Label (self.framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Adult',justify='center').grid(row=0,column=2)
		self.lbladult2= Label (self.framebottomright,relief='sunken',textvariable=adult,font=('arial',14,'bold'),width=8,justify='center').grid(row=1,column=2)
		self.lblchild1= Label (self.framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Child',justify='center').grid(row=0,column=3)
		self.lblchild2= Label (self.framebottomright,textvariable=child,relief='sunken',font=('arial',14,'bold'),width=8,justify='center').grid(row=1,column=3)
		self.lblfrom1= Label (self.framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='From',justify='center').grid(row=2,column=1)
		self.lblfrom2= Label (self.framebottomright,relief='sunken',textvariable=from1,font=('arial',14,'bold'),width=8,justify='center').grid(row=2,column=2)
		self.lblto1= Label (self.framebottomright,text='To', relief='sunken',font=('arial',14,'bold'),width=8,justify='center').grid(row=3,column=1)
		self.lblto2= Label (self.framebottomright,relief='sunken',textvariable=to,font=('arial',14,'bold'),width=8,justify='center').grid(row=3,column=2)
		self.lblprice1= Label (self.framebottomright,text='Price',relief='sunken',font=('arial',14,'bold'),width=8,justify='center').grid(row=3,column=2)
		self.lblprice2= Label (self.framebottomright,relief='sunken',textvariable=price,font=('arial',14,'bold'),width=8,justify='center').grid(row=3,column=2)
		self.lblRefNo1= Label (self.framebottomright,relief='sunken',font=('arial',14,'bold'),width=8,text='Ref No',justify='center').grid(row=5,column=0)
		self.lblRefNo2= Label (self.framebottomright,textvariable=ref,relief='sunken',font=('arial',14,'bold'),width=8,justify='center').grid(row=6,column=0)
		self.lblTime1= Label (self.framebottomright, relief='sunken',font=('arial',14,'bold'),width=8,text='Time',justify='center').grid(row=5,column=1)
		self.lblTime2= Label (self.framebottomright,textvariable=time1,relief='sunken',font=('arial',14,'bold'),width=8,justify='center').grid(row=6,column=1)
		self.lbldate1= Label (self.framebottomright,text='Date',relief='sunken',font=('arial',14,'bold'),width=8,justify='center').grid(row=5,column=2)
		self.lbldate2= Label (self.framebottomright,textvariable=Date1,relief='sunken',font=('arial',14,'bold'),width=8,justify='center').grid(row=6,column=2)
		self.lblroute1= Label (self.framebottomright,text='Route',relief='sunken',font=('arial',14,'bold'),width=8,justify='center').grid(row=5,column=3)
		self.lblroute2= Label (self.framebottomright,relief='sunken',textvariable=route,font=('arial',14,'bold'),width=8,justify='center').grid(row=6,column=3)

	

guiDefinition(root)
root.mainloop()