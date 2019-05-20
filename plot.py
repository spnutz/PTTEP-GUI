import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import ttk
from tkinter import IntVar

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math

class Graph(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Graph GUI")

        # Create Tap
        self.tabControl = ttk.Notebook(self)

        # create tab1
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="AVO")

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
        self.frame1 = ttk.LabelFrame(self.big_frame, text="Layer 1")
        self.frame1.grid(row=0, column=1, padx=20, pady=20)
        self.frame_layer2 = ttk.LabelFrame(self.big_frame, text="Layer 2")
        self.frame_layer2.grid(row=0, column=2, padx=20, pady=20)

        # Frame Figure
        self.frame2 = ttk.LabelFrame(self.big_frame)
        self.frame2.grid(row=0, column=0, padx=10, pady=5)

        # Add widget #
        #### input box  #####

        # P-Wave 1
        tk.Label(self.frame1, text='P-Wave Velocity1 :').grid(row=0, column=0)
        self.entry_P1 = tk.Entry(self.frame1, bd=3, width=5)
        self.entry_P1.grid(row=0, column=1)

        # P-Wave 2
        tk.Label(self.frame_layer2, text='P-Wave Velocity2 :').grid(row=0, column=0)
        self.entry_P2 = tk.Entry(self.frame_layer2, bd=3, width=5)
        self.entry_P2.grid(row=0, column=1)

        # Density 1
        tk.Label(self.frame1, text='Density1 :').grid(row=1, column=0)
        self.entry_D1 = tk.Entry(self.frame1, bd=3, width=5)
        self.entry_D1.grid(row=1, column=1)

        # Density 2
        tk.Label(self.frame_layer2, text='Density2 :').grid(row=1, column=0)
        self.entry_D2 = tk.Entry(self.frame_layer2, bd=3, width=5)
        self.entry_D2.grid(row=1, column=1)

        # S-Wave1
        tk.Label(self.frame1, text='S-Wave1 :').grid(row=2, column=0)
        self.entry_S1 = tk.Entry(self.frame1, bd=3, width=5)
        self.entry_S1.grid(row=2, column=1)

        # S-Wave2
        tk.Label(self.frame_layer2, text='S-Wave1 :').grid(row=2, column=0)
        self.entry_S2 = tk.Entry(self.frame_layer2, bd=3, width=5)
        self.entry_S2.grid(row=2, column=1)
    

        # show poisson into GUI
        tk.Label(self.frame1, text="Poisson's ratio 1: ").grid(row=3, column=0)
        self.poisson1 =0
        self.label_poisson1 = IntVar()
        self.label_poisson1.set(self.poisson1)
        self.total_s = tk.Label(self.frame1, textvariable=self.label_poisson1)
        self.total_s.grid(row=3, column=1)

        tk.Label(self.frame_layer2, text="Poisson's ratio 2: ").grid(row=3, column=0)
        self.poisson2 =0
        self.label_poisson2 = IntVar()
        self.label_poisson2.set(self.poisson2)
        self.total_poisson2 = tk.Label(self.frame_layer2, textvariable=self.label_poisson2)
        self.total_poisson2.grid(row=3, column=1)

        # show Vp/Vs
        tk.Label(self.frame1, text="Vp/Vs :").grid(row=4, column=0)
        self.vp_vs1 = 0
        self.label_vp_vs1 = IntVar()
        self.label_vp_vs1.set(self.vp_vs1)
        self.total_vp_vs1 = tk.Label(self.frame1, textvariable=self.label_vp_vs1)
        self.total_vp_vs1.grid(row=4, column=1)

        tk.Label(self.frame_layer2, text="Vp/Vs :").grid(row=4, column=0)
        self.vp_vs2 = 0
        self.label_vp_vs2 = IntVar()
        self.label_vp_vs2.set(self.vp_vs2)
        self.total_vp_vs2 = tk.Label(self.frame_layer2, textvariable=self.label_vp_vs2)
        self.total_vp_vs2.grid(row=4, column=1)

        # show Zp
        tk.Label(self.frame1, text="Zp1 :").grid(row=5, column=0)
        self.zp1 = 0
        self.label_zp1 = IntVar()
        self.label_zp1.set(self.zp1)
        self.total_zp1 = tk.Label(self.frame1, textvariable=self.label_zp1)
        self.total_zp1.grid(row=5, column=1)

        tk.Label(self.frame_layer2, text="Zp2 :").grid(row=5, column=0)
        self.zp1 = 0
        self.label_zp2 = IntVar()
        self.label_zp2.set(self.zp1)
        self.total_zp2 = tk.Label(self.frame_layer2, textvariable=self.label_zp2)
        self.total_zp2.grid(row=5, column=1)

        # Button plot
        self.btn_plot = tk.Button(self.frame1, text="Plot", command=self.getData, width=5)
        self.btn_plot.grid(row=6, column=1)

        # fig 
        self.fig = Figure(figsize=(5, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame2)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        self.canvas.draw()

    #### get data from input #####

    def getData(self):
        P1 = float(self.entry_P1.get())
        D1 = float(self.entry_D1.get())
        S1 = float(self.entry_S1.get())

        P2 = float(self.entry_P2.get())
        D2 = float(self.entry_D2.get())
        S2 = float(self.entry_S2.get())

        # calculate poisson
        self.poisson1 = self.cal_poisson(S1, P1)
        self.label_poisson1.set(self.poisson1)

        self.poisson2 = self.cal_poisson(S2, P2)
        self.label_poisson2.set(self.poisson2)

        # calculate Vp/Vs1
        self.vp_vs1 = P1/S1
        self.label_vp_vs1.set(self.vp_vs1)

        self.vp_vs2 = P2/S2
        self.label_vp_vs2.set(self.vp_vs2)

        # calculate Zp1
        self.zp1 = D1*P1
        self.label_zp1.set(self.zp1)

        self.zp2 = D2*P2
        self.label_zp2.set(self.zp2)

        #calculate reflection
        data_x = []
        data_y = []
        for n in range(11):
            t = math.pi
            x = (n*t)/180 # radians
            reflect = self.reflection(P1, D1, P2, D2, self.poisson1, self.poisson2, x)
            data_x.append(float(reflect))
            data_y.append(float(n*10))
        print(data_x)
        print(data_y)
        
        # plot
        self.plot_graph(data_y, data_x)

    ###########  Formula  ###########
    
    def cal_poisson(self, s_wave, p_wave):
        # (0.5-(s_wave / p_wave)^2)/(1-(s_wave/p_wave)^2)
        P = (0.5-(s_wave/p_wave)**2)/(1-(s_wave/p_wave)**2)
        return P

    def reflection(self, P1, D1, P2, D2, poisson1, poisson2, x):
        # R = ((P2*D2 - P1*D1)/(P2*D2 + P1*D1))*(cos(x)^2)+ (poisson2-poisson1)/((1-(poisson2+poisson1)/2)^2)*(sin(x)^2)
        R = ((P2*D2 - P1*D1)/(P2*D2 + P1*D1))*(math.cos(x)**2)+ (poisson2-poisson1)/((1-(poisson2+poisson1)/2)**2)*(math.sin(x)**2)
        return R
   
    #####    Plot   #####

    def plot_graph(self,x,y):
        #a = self.fig.add_subplot(1,1,1)
        a = self.fig.add_subplot(1,1,1)
        a.clear()
        a.plot(x,y)
        a.grid(True)
        a.set_title('Shuey(AVO) Approximation')
        a.set_xlabel('Incidence Angle(Degrees)')
        a.set_ylabel('Y')
        a.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80 ,90])
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
