from tkinter import *

class HomePage(Frame):

    def __init__(self, parent, controller):

        Frame.__init__(self, parent)
        self.controller = controller

        self.LabelTitle = Label(self, text="Welcome to \nSmart Home System", fg="Navy Blue",
                                font=('arial', 35, 'bold'), bd=30)
        self.LabelTitle.grid(row=2, column=0, columnspan=2, pady=200, padx = 100)