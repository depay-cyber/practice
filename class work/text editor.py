# from tkinter import *
# from tkinter.filedialog import asksaveasfile
# root =Tk()
# root.geometry('300x150')
# def save():
#     file=[('All Files', '*.*'),
#           ('Python File', '*.py'),
#           ('Text Document', '*. txt')
#           ]
#     file=asksaveasfile(filetypes=file,defaultextension=file)
# btn= Button(root,text='save',command=lambda:save())
# btn.pack(side=TOP) 
# mainloop()   

#top window
from tkinter import *
root=Tk()
root.geometry=('600x500')
root.title('Main')
def topwin():
    top=Toplevel()
    top.geometry=('200x300')
    top.title('Top window')
    label2=Label(top,text='Click me to open the top window')
    label2.pack()
    top.mainloop()
label1=Label(root,text='Welcome to top window')
btn=Button(root, text='Click here',command=topwin) 
label1.pack()
btn.pack()
mainloop()   