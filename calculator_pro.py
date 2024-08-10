import tkinter as tk
from tkinter import Entry, Button, StringVar

class calculator:
    def __init__(self,master):
        master.title("calcultor")
        master.geometry('357x420+0+0')
        master.config(bg='gray')
        master.resizable(False,False)

        self.equation =StringVar
        self.display = tk.Entry(root, textvariable=self.equation, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)
        

    


root=tk.Tk()

root.mainloop()
