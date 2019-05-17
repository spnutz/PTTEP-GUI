import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import ttk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Graph(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Graph GUI")

        # Create Tap
        self.tabControl = ttk.Notebook(self)

        # create tab1
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="S-T")

        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text="tab2")

        self.tabControl.grid()

        # Menu Bar
        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)
        self.create_menu_bar()

        ###############################  Tab1   ##########################################
        # Create container 
        self.big_frame = ttk.LabelFrame(self.tab1)
        self.big_frame.grid(column=0, row=0)

        # Frame input
        self.frame1 = ttk.LabelFrame(self.big_frame, text="  Input")
        self.frame1.grid(row=0, column=1, padx=20, pady=20)

        # Frame Figure
        self.frame2 = ttk.LabelFrame(self.big_frame, text="Figure Frame")
        self.frame2.grid(row=0, column=0, padx=10, pady=5)

        # Add widget #
        #### input box  #####
        tk.Label(self.frame1, text='u :').grid(row=0, column=0)
        self.entry_u = tk.Entry(self.frame1, bd=3, width=5)
        self.entry_u.grid(row=0, column=1)

        tk.Label(self.frame1, text='a :').grid(row=1, column=0)
        self.entry_a = tk.Entry(self.frame1, bd=3, width=5)
        self.entry_a.grid(row=1, column=1)

        tk.Label(self.frame1, text='t :').grid(row=2, column=0)
        self.entry_t = tk.Entry(self.frame1, bd=3, width=5)
        self.entry_t.grid(row=2, column=1)

        tk.Label(self.frame1, text="s: ").grid(row=3, column=0)
    

        # Button plot
        self.btn_plot = tk.Button(self.frame1, text="Plot", command=self.getData, width=5)
        self.btn_plot.grid(row=4, column=1)

        # fig 
        self.fig = Figure(figsize=(4, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame2)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        self.canvas.draw()

    #### get data from input #####

    def getData(self):
        u = float(self.entry_u.get())
        a = float(self.entry_a.get())
        t = float(self.entry_t.get())

        # calculate
        s = float((u*t) + (0.5*t*t))
        print('u: {}\na: {}\nt: {}\ns: {}\n'.format(u, a, t, s))
        self.plot_graph(s, t)

    #####    Plot   #####

    def plot_graph(self,s,t):
        a = self.fig.add_subplot(111)
        a.clear()
        a.plot([t,s])
        a.grid(True)
        a.legend(['S-T Graph'])
        self.canvas.draw()

    #####   Menu Bar  ######

    def create_menu_bar(self):
        # file menu bar
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self._quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Help menu bar
        help_menu = Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._msg)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

   ##### exit function menu bar #####

    def _quit(self):
        self.quit()
        self.destroy()
        exit()

    ######   Message Box   ######

    def _msg(self):
        msg.showinfo("Graph info","Program Plot Graph ")

        
####################
#     STRAT GUI    #
####################
if __name__ == "__main__":
    app = Graph()
    app.mainloop()
