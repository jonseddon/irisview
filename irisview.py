"""
irisview

A simple file viewer based on Iris
"""
from __future__ import absolute_import, division, print_function
import six.moves.tkinter as tk


class IrisView:
    def __init__(self, master):
        """
        Initialise the class
        
        :param tkinter.Tk master: The root Tkinter object
        """
        self.master = master

        self.add_menu()


    def add_menu(self):
        """
        Add a menu bar to the main window.
        """
        menubar = tk.Menu(self.master)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label='Open...', command=hello)
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



def hello():
    print('hello!')

def about():
    print('Wibble')


if __name__ == '__main__':
    root = tk.Tk()
    irisview_window = IrisView(root)
    root.title('irisview')
    tk.mainloop()
