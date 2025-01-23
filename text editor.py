from tkinter import *
from tkinter.filedialog import asksaveasfile
root =Tk()
root.geometry('300x150')
def save():
    file=[('All Files', '*.*'),
          ('Python File', '*.py'),
          ('Text Document', '*. txt')
          ]
    file=asksaveasfile(filetypes=file,defaultextension=file)
btn= Button(root,text='save',command=lambda:save())
btn.pack(side=TOP) 
mainloop()   