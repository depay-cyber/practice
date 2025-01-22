from tkinter import *
from datetime import date 
window = Tk()
window.title('Cheatah')
window.geometry('400x200')
lbl= Label(text='Welcome to fast speed on Cheatah',fg='orange', bg='brown',height=1,width=300)
name_lbl=Label(text=' Enter Full name',bg='brown')
name_entry=Entry()
def display():
    name=name_entry.get()
    Message='Welcome to app \n todays date: '
    greet = f'Hello, {name}!'
    text_box.insert (END,greet)
    text_box.insert (END,Message)
    text_box.insert(END,date.today())
text_box=Text(height=3)    
btn=Button(text='begin',command=display,height=1,bg='green',fg='sky blue')
lbl.pack()
name_lbl.pack()
btn.pack()
text_box.pack()
window.mainloop()