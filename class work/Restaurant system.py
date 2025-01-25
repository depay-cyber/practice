import tkinter as tk
from tkinter import ttk , messagebox
class Ordermanagement:
    def __init__(self, root):
        self.root=root
        self.root.title('Restaurant Management App')
        self.menuitem={
            'fries Meal': 2,
            'Lunch Meal': 2,
            'Burger':3,
            'Pizza Meal':4,
            'Cheese':3.5,
            'Drinks':1
        }
        self.exhangerate=30000
        self.setup_background(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(
            frame,text='restaurant order managment',
            font=('arial',20,'bold').grid(
                row=0,
                columnspan=3,
                padx=10,
                pady=10
            )
        )
        self.menu_label={}
        self.menu_qualities={}
        for i ,(item,price) in enumerate(self.menuitem.items(),start=1):
            label=ttk.Label(frame,text=f'{item} ($ {price}) ',
                            font=('arial',12)
                            )
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menu_label[item]=label
            quantity_entry=ttk.Entry (frame,width=5)
            quantity_entry.grid(row=i,column=1,padx=10,pady=5)
            self.menu_qualities[item]=quantity_entry
obj=Ordermanagement()            