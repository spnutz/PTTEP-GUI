import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time
import threading

class GraphGui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("600x600") # set size window
        self.resizable(False,False) # disable re-size
        
        self.continuePlot = False

        self.top_fram = tk.Frame(self)
        self.top_fram.pack(side = "top")
        self.bottom_fram = tk.Frame(self)
        self.bottom_fram.pack(side = "bottom")

        tk.Label(self.bottom_fram,text="u :").pack()
        self.u = tk.Entry(self.bottom_fram)
        self.u.pack()
        
        tk.Label(self.bottom_fram,text="a :").pack()
        self.a = tk.Entry(self.bottom_fram)
        self.a.pack()

        tk.Label(self.bottom_fram,text="t :").pack()
        self.t = tk.Entry(self.bottom_fram)
        self.t.pack()

        #tk.Label(self.bottom_fram,text="y2 :").pack()
        #self.y2 = tk.Entry(self.bottom_fram)
        #self.y2.pack()

        self.button = tk.Button(self.bottom_fram, text="Plot", command=self.getData)
        self.button.pack(side='left')

        self.btn_exit = tk.Button(self.bottom_fram, text='Qut', command=self.quit)
        self.btn_exit.pack(side='right')     
       

    def getData(self):
        data_u = float(self.u.get())
        data_a = float(self.a.get())
        data_t = float(self.t.get())
        #data_y2 = float(self.y2.get())

        print("u: {}\na: {}\nt: {} ".format(data_u, data_a, data_t))
        self.calculate(data_u, data_a, data_t)


    def calculate(self,u,a,t):
        s = (u*t) + (0.5*a*t*t)
        print("s:",s)
        self.change_state()
        self.plot_gui(s,t)

        
    def plot_gui(self,s,t):
        
        fig = Figure(figsize=(4,4))
        a = fig.add_subplot(111)
        a.plot([t,s])

        canvas = FigureCanvasTkAgg(fig, master=self.top_fram)
        canvas.get_tk_widget().pack()
        canvas.draw()
        
    def change_state(self):
        if self.continuePlot == True:
            self.continuePlot = False
        else:
            self.continuePlot = True


    


app = GraphGui()
app.mainloop()