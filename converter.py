import moviepy.editor as mp
from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox

top = Tk()
files=""
def browsing():
   filename=askopenfilename()
   pathlabel.config(text=filename)
   global files
   files=filename
   myclip = mp.VideoFileClip(files)
   E2.insert(END, myclip.duration)

def conversion():
	if files=="" :
		tkMessageBox.showinfo( "WARNING", "Please select a file...!!")
	else:
		if float(E1.get())==float(E2.get()):
			tkMessageBox.showinfo( "WARNING", "Audio duration is 0...please enter a valid duration")
		elif str(E3.get())=="":
			tkMessageBox.showinfo( "WARNING", "Please enter an output filename...!!")
		clip = mp.VideoFileClip(files).subclip(float(E1.get()),float(E2.get()))
		clip.audio.write_audiofile("D:/"+str(E3.get())+".mp3")

browsebutton = Button(top, text="Browse", command=browsing)
browsebutton.grid(row=0, column=2)

pathlabel = Label(top)
pathlabel.grid(row=0,column=0)

L1 = Label(top, text="Start Point (in seconds)")
L1.grid( row=2)
E1 = Entry(top, bd =5)	
E1.insert(END, '0')
E1.grid( row=2, column=1)

L2 = Label(top, text="End Point (in seconds)")
L2.grid( row=3)
E2 = Entry(top, bd =5)
E2.insert(END, '0')
E2.grid( row=3, column=1)

L3 = Label(top, text="Output Filename")
L3.grid( row=4)
E3 = Entry(top, bd =5)
#E3.insert(END, files)
E3.grid( row=4, column=1)

B = Button(top, text ="Convert", command = conversion)
B.grid(row=5)

top.mainloop()