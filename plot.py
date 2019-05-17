import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import ttk
from tkinter import Menu

class Graph(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        # Create container 
        self.big_frame = ttk.LabelFrame(self, text="Big Frame")
        self.big_frame.grid(column=0, row=0)

        # Frame input
        self.frame1 = ttk.LabelFrame(self.big_frame, text="frame1")
        self.frame1.grid(row=0, column=1)

        # Frame Figure
        self.frame2 = ttk.LabelFrame(self.big_frame, text="Figure Frame")
        self.frame2.grid(row=0, column=0)

        ###### Add widget ######

        #### input box  u#####
        tk.Label(self.frame1, text='u :').grid(row=0, column=0)
        self.entry_u = tk.Entry(self.frame1, bd=3, width=5)
        self.entry_u.grid(row=0, column=1)

        tk.Label(self.frame1, text='a :').grid(row=1, column=0)
        self.entry_a = tk.Entry(self.frame1, bd=3, width=5)
        self.entry_a.grid(row=1, column=1)

        tk.Label(self.frame1, text='t :').grid(row=2, column=0)
        self.entry_t = tk.Entry(self.frame1, bd=3, width=5)
        self.entry_t.grid(row=2, column=1)

        # Button plot
        self.btn_plot = tk.Button(self.frame1, text="Plot", command=self.getData, width=8)
        self.btn_plot.grid(row=4, column=1)

        # fig 
        self.fig = Figure(figsize=(4, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame2)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        self.canvas.draw()

        # Menu Bar
        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)
        self.create_menu_bar()
 
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
        self.canvas.draw()

    #####   Menu Bar  ######

    def create_menu_bar(self):
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self._quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

   ##### exit function menu bar #####

    def _quit(self):
        self.quit()
        self.destroy()
        exit()

        
####################
#     STRAT GUI    #
####################
if __name__ == "__main__":
    app = Graph()
    app.mainloop()
