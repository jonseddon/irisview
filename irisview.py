"""
irisview

A simple file viewer based on Iris
"""
from __future__ import absolute_import, division, print_function
import six.moves.tkinter as tk
from six.moves import tkinter_tkfiledialog

import iris

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

class IrisView:
    def __init__(self, master):
        """
        Initialise the class
        
        :param tkinter.Tk master: The root Tkinter object
        """
        self.master = master
        self.filename = None
        self.cubelist = None

        frame = tk.Frame(master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        self.add_menu()

    def file_open(self):
        """
        Implement the menu File->Open action.
        """
        filename = tkinter_tkfiledialog.askopenfilename()
        if filename:
            self.filename = filename
            # self.cubelist = iris.load(filename)
            self.master.title('irisview {}'.format(filename))

    def add_menu(self):
        """
        Add a menu bar to the main window.
        """
        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open...', command=self.file_open)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label='About', command=self.show_about)
        menubar.add_cascade(label='Help', menu=helpmenu)

        self.master.config(menu=menubar)
    
    def show_about(self):
        """
        Display an About dialogue box.
        """
        toplevel = tk.Toplevel(self.master, bg='white')
        toplevel.transient(self.master)
        toplevel.title('About')
        tk.Label(toplevel, text='A simple iris viewer', fg='navy', bg='white').pack(pady=20)
        tk.Label(toplevel, text="Based on Scitools' Iris", bg='white').pack()
        tk.Button(toplevel, text='Close', command=toplevel.withdraw).pack(pady=30)


if __name__ == '__main__':
    root = tk.Tk()
    
    irisview_window = IrisView(root)
    root.title('irisview')
    tk.mainloop()
