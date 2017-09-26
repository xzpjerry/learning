#!/usr/bin/env python3

#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox as tkmb
import tkinter.filedialog as tkfdl
import os.path as path


class Application:
    counter = 0
    def __init__(self, func = None, master=None):
        self.matching_module = func
        self.master = master
        self.frame = tk.Frame(self.master)
        self.file_name = None

        self.wordInput = tk.Entry(self.frame)
        self.button1 = tk.Button(
            self.frame, text='Look up', width=25, command=master.destroy)
        self.button2 = tk.Button(
            self.frame, text='create new windows', width=25, command=self.cw)
        self.button3 = tk.Button(
            self.frame, text='Exit', width=25, command=self.master.destroy)

        self.wordInput.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.frame.pack()

    def cw(self):
        self.counter += 1
        t = tk.Toplevel(self.frame)
        t.wm_title(self.counter)
        s = tk.Scrollbar(t)
        text = tk.Text(t, height=4, width=50)
        text.pack(side=tk.LEFT, fill=tk.Y)
        s.pack(side=tk.RIGHT, fill=tk.Y)
        s.config(command=text.yview)
        text.config(yscrollcommand=s.set)
        text.insert(tk.END, 'HHHHHSSSSSSSSSSSSSSSSSSSSS\n\n\n\n\n')

basic = tk.Tk()
basic.maxsize(1920, 1080)
basic.title('SRT dictionary')
app = Application(master=basic)
basic.mainloop()

