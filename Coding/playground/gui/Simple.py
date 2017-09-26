#!/usr/bin/env python3
'''
Author: Zhipeng Xie

Topic:

Effect:

'''

from tkinter import *
import tkinter.messagebox as messagebox
class test(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Who are you, my friend?')
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Confirm', command=self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
        

    def hello(self):
        name = self.nameInput.get() or 'Blank'
        messagebox.showinfo('Welcome', 'Hello, %s' % name)

app = test()
app.master.title('Hi')
app.mainloop()
