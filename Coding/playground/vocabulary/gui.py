#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.filedialog as tkfdl
import os.path as path


class Application:
    def __init__(self, func, master=None):
        self.matching_module = func
        self.master = master
        self.frame = tk.Frame(self.master)
        self.file_name = None

        w = 200
        h = 120
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        x = ws/2 - w/2
        y = hs/2 - h/2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

        self.wordInput = tk.Entry(self.frame)
        self.button1 = tk.Button(
            self.frame, text='Look up', width=25, command=self.check)
        self.button2 = tk.Button(
            self.frame, text='Add SRT file', width=25, command=self.addFile)
        self.button3 = tk.Button(
            self.frame, text='Exit', width=25, command=self.master.destroy)

        self.wordInput.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.frame.pack()

    def addFile(self):
        self.file_name = tkfdl.askopenfilename(
            title='Choose your srt file', filetypes=(('SRT', '*.srt'),))

    def check(self):
        self.target = self.wordInput.get() or -1
        if self.target != -1:
            result = self.matching_module(self.target, self.file_name)

            t = tk.Toplevel(self.frame)
            s = tk.Scrollbar(t)
            b = tk.Button(t, text='OK', width=10, command=t.destroy)
            text = tk.Text(t, height=25, width=120)
            t.wm_title('Result')
            text.pack(side=tk.LEFT, fill=tk.Y)
            s.pack(side=tk.RIGHT, fill=tk.Y)
            b.pack(side=tk.BOTTOM)
            s.config(command=text.yview)
            text.config(yscrollcommand=s.set)
            text.insert(tk.END, result)
