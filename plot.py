import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import ttk
from tkinter import IntVar
from PIL import ImageTk, Image

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math
import numpy as np

class Graph(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(False, False) # disable resize window
        self.title("Graph GUI")

        # Add icon
        self.iconbitmap('Picture/logo.ico')

        # Create Tab
        self.tabControl = ttk.Notebook(self)

        # create tab1
        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text="AVO")

        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text="Tab2")

        self.tabControl.grid()

        # Menu Bar
        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)
        self.create_menu_bar()

        ###############################  Tab1   ##########################################
        # Create container 
        self.big_frame = ttk.LabelFrame(self.tab1)
        self.big_frame.grid(column=0, row=0)

        # Logo frame
        self.logo_frame = ttk.LabelFrame(self.big_frame)
        self.logo_frame.grid(row=0, column=1)

        ################################### Frame input ###################################
        self.frame_input = ttk.LabelFrame(self.logo_frame)
        self.frame_input.grid(row=1, column=0)
        
        self.frame_gas = ttk.LabelFrame(self.frame_input, text="Gas")
        self.frame_gas.grid(row=0, column=0)

        self.frame_water = ttk.LabelFrame(self.frame_input, text="Water")
        self.frame_water.grid(row=0, column=1)

        self.frame_oil = ttk.LabelFrame(self.frame_input, text="Oil")
        self.frame_oil.grid(row=0, column=2)

        # gas case
        self.frame1 = ttk.LabelFrame(self.frame_gas, text="Layer 1")
        self.frame1.grid(row=1, column=0, padx=20)
        
        self.frame_layer2 = ttk.LabelFrame(self.frame_gas, text="Layer 2")
        self.frame_layer2.grid(row=2, column=0, padx=20)

        # water case
        self.frame_layer1_water = ttk.LabelFrame(self.frame_water, text="Layer 1")
        self.frame_layer1_water.grid(row=0, column=0)

        self.frame_layer2_water = ttk.LabelFrame(self.frame_water, text="Layer 2")
        self.frame_layer2_water.grid(row=1, column=0)

        # oil case
        self.frame_layer1_oil = ttk.LabelFrame(self.frame_oil, text="Layer 1")
        self.frame_layer1_oil.grid(row=0, column=0)

        self.frame_layer2_oil = ttk.LabelFrame(self.frame_oil, text="Layer 2")
        self.frame_layer2_oil.grid(row=1, column=0)



        ##################################################################################

        # Frame Figure
        self.frame2 = ttk.LabelFrame(self.big_frame)
        self.frame2.grid(row=0, column=0, padx=10, pady=5)

        # Frame Change Scope axis 
        self.frame_axis = ttk.LabelFrame(self.frame_input, text='Change Axis')
        self.frame_axis.grid(row=3, column=0)

        # Add logo PTTEP
        self.img = ImageTk.PhotoImage(Image.open("Picture/icon.png"))
        self.panel = ttk.Label(self.logo_frame, image= self.img)
        self.panel.grid(row=0, column=0, padx=20) 


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

        # Axis default
        self.axis_default = 0
        self.axis_value_start = IntVar() # default start
        self.axis_value_start.set(self.axis_default)
        self.axis_value_stop = IntVar() # default  stop
        self.axis_value_stop.set(self.axis_default)
        # start
        tk.Label(self.frame_axis, text='Y :').grid(row=0, column=0)
        self.start_axis_y = tk.Entry(self.frame_axis, textvariable=self.axis_value_start,bd=3, width=5)
        self.start_axis_y.grid(row=0, column=1)
        # stop
        tk.Label(self.frame_axis, text=' to ').grid(row=0, column=2)
        self.stop_axis_y = tk.Entry(self.frame_axis, textvariable=self.axis_value_stop, bd=3, width=5)
        self.stop_axis_y.grid(row=0, column=3)
        
        # step
        self.default_step = IntVar()
        self.default_step.set(1)
        tk.Label(self.frame_axis, text='Step : ').grid(row=1,column=0)
        self.step = tk.Entry(self.frame_axis, textvariable=self.default_step, bd=3, width=5)
        self.step.grid(row=1, column=1)

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
        self.zp2 = 0
        self.label_zp2 = IntVar()
        self.label_zp2.set(self.zp2)
        self.total_zp2 = tk.Label(self.frame_layer2, textvariable=self.label_zp2)
        self.total_zp2.grid(row=5, column=1)

        # show Rp
        tk.Label(self.frame1, text="Rp :").grid(row=6, column=0)
        self.rp = 0
        self.label_rp = IntVar()
        self.label_rp.set(self.rp)
        self.total_rp = tk.Label(self.frame1, textvariable=self.label_rp)
        self.total_rp.grid(row=6, column=1)

        # Button plot
        self.btn_plot = tk.Button(self.frame_layer2, text="Plot", command=self.getData, width=5)
        self.btn_plot.grid(row=6, column=1)

        # fig AVO
        self.fig = Figure(figsize=(5,5.15))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame2)
        self.canvas.get_tk_widget().grid(row=0, column=0)
        self.canvas.draw()
        
        # add Fig Layer
        self.layer_img = ImageTk.PhotoImage(Image.open("Picture/layer.png"))
        self.panel_layer_img = ttk.Label(self.frame2, image=self.layer_img)
        self.panel_layer_img.grid(row = 1 ,column=0)

        ############ water input ############
        ##### Layer 1
        # P-Wave 1
        tk.Label(self.frame_layer1_water, text="P-Wave Velocity1 :").grid(row=0, column=0)
        self.entry_P1_water = tk.Entry(self.frame_layer1_water, bd=3, width=5)
        self.entry_P1_water.grid(row=0, column=1)
        # Density 1
        tk.Label(self.frame_layer1_water, text='Density1 :').grid(row=1, column=0)
        self.entry_D1_water = tk.Entry(self.frame_layer1_water, bd=3, width=5)
        self.entry_D1_water.grid(row=1, column=1)
        # S-Wave 1
        tk.Label(self.frame_layer1_water, text='S-Wave1 :').grid(row=2, column=0)
        self.entry_S1_water = tk.Entry(self.frame_layer1_water, bd=3, width=5)
        self.entry_S1_water.grid(row=2, column=1)
        # show poisson 1
        tk.Label(self.frame_layer1_water, text="Poisson's ratio 1: ").grid(row=3, column=0)
        self.poisson1_water =0
        self.label_poisson1_water = IntVar()
        self.label_poisson1_water.set(self.poisson1_water)
        self.total_s_water = tk.Label(self.frame_layer1_water, textvariable=self.label_poisson1_water)
        self.total_s_water.grid(row=3, column=1)
        # show Vp/Vs
        tk.Label(self.frame_layer1_water, text="Vp/Vs :").grid(row=4, column=0)
        self.vp_vs1_water = 0
        self.label_vp_vs1_water = IntVar()
        self.label_vp_vs1_water.set(self.vp_vs1_water)
        self.total_vp_vs1_water = tk.Label(self.frame_layer1_water, textvariable=self.label_vp_vs1_water)
        self.total_vp_vs1_water.grid(row=4, column=1)
        # show Zp1
        tk.Label(self.frame_layer1_water, text="Zp1 :").grid(row=5, column=0)
        self.zp1_water = 0
        self.label_zp1_water = IntVar()
        self.label_zp1_water.set(self.zp1_water)
        self.total_zp1_water = tk.Label(self.frame_layer1_water, textvariable=self.label_zp1_water)
        self.total_zp1_water.grid(row=5, column=1)
        # show Rp
        tk.Label(self.frame_layer1_water, text="Rp :").grid(row=6, column=0)
        self.rp_water = 0
        self.label_rp_water = IntVar()
        self.label_rp_water.set(self.rp)
        self.total_rp_water = tk.Label(self.frame_layer1_water, textvariable=self.label_rp_water)
        self.total_rp_water.grid(row=6, column=1)

        ##### Layer 2
        # P-Wave 2
        tk.Label(self.frame_layer2_water, text='P-Wave Velocity2 :').grid(row=0, column=0)
        self.entry_P2_water = tk.Entry(self.frame_layer2_water, bd=3, width=5)
        self.entry_P2_water.grid(row=0, column=1)
        # Density 2
        tk.Label(self.frame_layer2_water, text='Density2 :').grid(row=1, column=0)
        self.entry_D2_water = tk.Entry(self.frame_layer2_water, bd=3, width=5)
        self.entry_D2_water.grid(row=1, column=1)
        # S-Wave2
        tk.Label(self.frame_layer2_water, text='S-Wave2 :').grid(row=2, column=0)
        self.entry_S2_water = tk.Entry(self.frame_layer2_water, bd=3, width=5)
        self.entry_S2_water.grid(row=2, column=1)
        # show poisson 2
        tk.Label(self.frame_layer2_water, text="Poisson's ratio 2 :").grid(row=3, column=0)
        self.poisson2_water =0
        self.label_poisson2_water = IntVar()
        self.label_poisson2_water.set(self.poisson2_water)
        self.total_poisson2_water = tk.Label(self.frame_layer2_water, textvariable=self.label_poisson2_water)
        self.total_poisson2_water.grid(row=3, column=1)
        # show Vp/Vs 2
        tk.Label(self.frame_layer2_water, text="Vp/Vs :").grid(row=4, column=0)
        self.vp_vs2_water = 0
        self.label_vp_vs2_water = IntVar()
        self.label_vp_vs2_water.set(self.vp_vs2_water)
        self.total_vp_vs2_water = tk.Label(self.frame_layer2_water, textvariable=self.label_vp_vs2_water)
        self.total_vp_vs2_water.grid(row=4, column=1)
        # show Zp2
        tk.Label(self.frame_layer2_water, text="Zp2 :").grid(row=5, column=0)
        self.zp2_water = 0
        self.label_zp2_water = IntVar()
        self.label_zp2_water.set(self.zp2_water)
        self.total_zp2_water = tk.Label(self.frame_layer2_water, textvariable=self.label_zp2_water)
        self.total_zp2_water.grid(row=5, column=1)

        ######################  oil input  ######################
        ### Layer 1
        # P-Wave 1
        tk.Label(self.frame_layer1_oil, text="P-Wave Velocity1 :").grid(row=0, column=0)
        self.entry_P1_oil = tk.Entry(self.frame_layer1_oil, bd=3, width=5)
        self.entry_P1_oil.grid(row=0, column=1)
        # Density 1
        tk.Label(self.frame_layer1_oil, text='Density1 :').grid(row=1, column=0)
        self.entry_D1_oil = tk.Entry(self.frame_layer1_oil, bd=3, width=5)
        self.entry_D1_oil.grid(row=1, column=1)
        # S-Wave 1
        tk.Label(self.frame_layer1_oil, text='S-Wave1 :').grid(row=2, column=0)
        self.entry_S1_oil = tk.Entry(self.frame_layer1_oil, bd=3, width=5)
        self.entry_S1_oil.grid(row=2, column=1)
        # show poisson 1
        tk.Label(self.frame_layer1_oil, text="Poisson's ratio 1: ").grid(row=3, column=0)
        self.poisson1_oil =0
        self.label_poisson1_oil = IntVar()
        self.label_poisson1_oil.set(self.poisson1_oil)
        self.total_s_oil = tk.Label(self.frame_layer1_oil, textvariable=self.label_poisson1_oil)
        self.total_s_oil.grid(row=3, column=1)
        # show Vp/Vs
        tk.Label(self.frame_layer1_oil, text="Vp/Vs :").grid(row=4, column=0)
        self.vp_vs1_oil = 0
        self.label_vp_vs1_oil = IntVar()
        self.label_vp_vs1_oil.set(self.vp_vs1_water)
        self.total_vp_vs1_oil = tk.Label(self.frame_layer1_oil, textvariable=self.label_vp_vs1_oil)
        self.total_vp_vs1_oil.grid(row=4, column=1)
        # show Zp1
        tk.Label(self.frame_layer1_oil, text="Zp1 :").grid(row=5, column=0)
        self.zp1_oil = 0
        self.label_zp1_oil = IntVar()
        self.label_zp1_oil.set(self.zp1_water)
        self.total_zp1_oil = tk.Label(self.frame_layer1_oil, textvariable=self.label_zp1_oil)
        self.total_zp1_oil.grid(row=5, column=1)
        # show Rp
        tk.Label(self.frame_layer1_oil, text="Rp :").grid(row=6, column=0)
        self.rp_oil = 0
        self.label_rp_oil = IntVar()
        self.label_rp_oil.set(self.rp)
        self.total_rp_oil = tk.Label(self.frame_layer1_oil, textvariable=self.label_rp_oil)
        self.total_rp_oil.grid(row=6, column=1)
        #### Layer 2
        # P-Wave 2
        tk.Label(self.frame_layer2_oil, text='P-Wave Velocity2 :').grid(row=0, column=0)
        self.entry_P2_oil = tk.Entry(self.frame_layer2_oil, bd=3, width=5)
        self.entry_P2_oil.grid(row=0, column=1)
        # Density 2
        tk.Label(self.frame_layer2_oil, text='Density2 :').grid(row=1, column=0)
        self.entry_D2_oil = tk.Entry(self.frame_layer2_oil, bd=3, width=5)
        self.entry_D2_oil.grid(row=1, column=1)
        # S-Wave2
        tk.Label(self.frame_layer2_oil, text='S-Wave2 :').grid(row=2, column=0)
        self.entry_S2_oil = tk.Entry(self.frame_layer2_oil, bd=3, width=5)
        self.entry_S2_oil.grid(row=2, column=1)
        # show poisson 2
        tk.Label(self.frame_layer2_oil, text="Poisson's ratio 2 :").grid(row=3, column=0)
        self.poisson2_oil =0
        self.label_poisson2_oil = IntVar()
        self.label_poisson2_oil.set(self.poisson2_oil)
        self.total_poisson2_oil = tk.Label(self.frame_layer2_oil, textvariable=self.label_poisson2_oil)
        self.total_poisson2_oil.grid(row=3, column=1)
        # show Vp/Vs 2
        tk.Label(self.frame_layer2_oil, text="Vp/Vs :").grid(row=4, column=0)
        self.vp_vs2_oil = 0
        self.label_vp_vs2_oil = IntVar()
        self.label_vp_vs2_oil.set(self.vp_vs2_oil)
        self.total_vp_vs2_oil = tk.Label(self.frame_layer2_oil, textvariable=self.label_vp_vs2_oil)
        self.total_vp_vs2_oil.grid(row=4, column=1)
        # show Zp2
        tk.Label(self.frame_layer2_oil, text="Zp2 :").grid(row=5, column=0)
        self.zp2_oil = 0
        self.label_zp2_oil = IntVar()
        self.label_zp2_oil.set(self.zp2_oil)
        self.total_zp2_oil = tk.Label(self.frame_layer2_oil, textvariable=self.label_zp2_oil)
        self.total_zp2_oil.grid(row=5, column=1)


       


        


        ##############     tab2      ########################
        self.create_tab2()


    def create_tab2(self):
        ###### Create Frame   #########
        self.big_frame2 = ttk.LabelFrame(self.tab2)
        self.big_frame2.grid(row=0, column=0)
        tk.Label(self.big_frame2, text="")

        self.fig2_frame = ttk.LabelFrame(self.big_frame2)
        self.fig2_frame.grid(row=0, column=0)

        self.fig3_frame = ttk.LabelFrame(self.big_frame2)
        self.fig3_frame.grid(row=0, column=1)

        self.fig4_frame = ttk.LabelFrame(self.big_frame2)
        self.fig4_frame.grid(row=1, column=0)

        self.fig5_frame = ttk.LabelFrame(self.big_frame2)
        self.fig5_frame.grid(row=1, column=1)
        

        ### fig tab2 ###
        self.fig2 = Figure(figsize=(3,3)) # fig vp : D
        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.fig2_frame)
        self.canvas2.get_tk_widget().grid(row=0, column=0)
        self.canvas2.draw() 

        self.fig3 = Figure(figsize=(3,3)) # fig vs : D
        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.fig3_frame)
        self.canvas3.get_tk_widget().grid(row=0, column=0)
        self.canvas3.draw()

        self.fig4 = Figure(figsize=(3,3)) # fig vp : poisson
        self.canvas4 = FigureCanvasTkAgg(self.fig4, master=self.fig4_frame)
        self.canvas4.get_tk_widget().grid(row=0, column=0)
        self.canvas4.draw()

        self.fig5 = Figure(figsize=(3,3)) # fig vs : poisson
        self.canvas5 = FigureCanvasTkAgg(self.fig5, master=self.fig5_frame)
        self.canvas5.get_tk_widget().grid(row=0, column=0)
        self.canvas5.draw()

    def plot_graph_vp_density(self, P1, D1, P2, D2):
        '''plot Vp : Density'''
        ax = self.fig2.add_subplot(1,1,1)
        ax.clear()
        # set Label
        ax.set_xlabel('Density',fontsize=8)
        ax.set_ylabel('Vp',fontsize=8)
        # plot
        ax.plot(D1, P1, marker='v', label="Layer 1")
        ax.plot(D2, P2, marker = '^' , label="Layer 2")
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="x", labelsize=8)
        ax.legend()
        ax.grid()
        # draw figure into gui
        self.fig2.tight_layout()
        self.canvas2.draw()

    def plot_graph_vs_density(self, S1, D1, S2, D2):
        ''' plot Vs:Density'''
        ax = self.fig3.add_subplot(1,1,1)
        ax.clear()
        # set Label
        ax.set_xlabel('Density',fontsize=8)
        ax.set_ylabel('Vs',fontsize=8)
        # plot
        ax.plot(D1, S1, marker='*', label="Layer 1")
        ax.plot(D2, S2, marker = '^' , label="Layer 2")
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="x", labelsize=8)
        ax.legend()
        ax.grid()
        # draw figure into gui
        self.fig3.tight_layout()
        self.canvas3.draw()

    def plot_graph_vp_poisson(self, P1, poisson1, P2, poisson2):
        '''plot vp : poisson'''
        ax = self.fig4.add_subplot(1,1,1)
        ax.clear()
        # set Label
        ax.set_xlabel('Poisson',fontsize=8)
        ax.set_ylabel('Vp',fontsize=8)
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="x", labelsize=8)
        # plot
        ax.plot(poisson1, P1, marker='*', label="Layer 1")
        ax.plot(poisson2, P2, marker = '^' , label="Layer 2")
        ax.legend()
        ax.grid()
        # draw figure into gui
        self.fig4.tight_layout()
        self.canvas4.draw()

    def plot_graph_vs_poisson(self, S1, poisson1, S2, poisson2):
        '''plot vs : poisson'''
        ax = self.fig5.add_subplot(1,1,1)
        ax.clear()
        # set Label
        ax.set_xlabel('Poisson',fontsize=8)
        ax.set_ylabel('Vs',fontsize=8)
        ax.tick_params(axis="y", labelsize=8)
        ax.tick_params(axis="x", labelsize=8)
        # plot
        ax.plot(poisson1, S1, marker='*', label="Layer 1")
        ax.plot(poisson2, S2, marker = '^' , label="Layer 2")
        ax.legend()
        ax.grid()
        # draw figure into gui
        self.fig5.tight_layout()
        self.canvas5.draw()
  
    # def plot_graph_VP_VS_tab2(self, vp_vs1, D1, vp_vs2, D2):
    #     '''Vp/Vs and Density'''
    #     ax = self.fig2.add_subplot(1,1,1)
    #     ax.clear()
    #     # set Label
    #     ax.set_xlabel('Density',fontsize=8)
    #     ax.set_ylabel('Vp/Vs',fontsize=8)
    #     # plot
    #     ax.plot(D1, vp_vs1, marker='o', label="Layer 1")
    #     ax.plot(D2, vp_vs2, marker = '^' , label="Layer 2")
    #     ax.legend()
    #     ax.grid()
    #     # draw figure into gui
    #     self.fig2.tight_layout()
    #     self.canvas2.draw()
        
    #### get data from input #####

    def getData(self):
        try:
            # input of gas
            P1 = float(self.entry_P1.get())
            D1 = float(self.entry_D1.get())
            S1 = float(self.entry_S1.get())
            P2 = float(self.entry_P2.get())
            D2 = float(self.entry_D2.get())
            S2 = float(self.entry_S2.get())
            #input of water
            P1_water = float(self.entry_P1_water.get())
            D1_water = float(self.entry_D1_water.get())
            S1_water = float(self.entry_S1_water.get())
            P2_water = float(self.entry_P2_water.get())
            D2_water = float(self.entry_D2_water.get())
            S2_water = float(self.entry_S2_water.get())
            #input of oil
            P1_oil = float(self.entry_P1_oil.get())
            D1_oil = float(self.entry_D1_oil.get())
            S1_oil = float(self.entry_S1_oil.get())
            P2_oil = float(self.entry_P2_oil.get())
            D2_oil = float(self.entry_D2_oil.get())
            S2_oil = float(self.entry_S2_oil.get())
            # input of change axis
            start_y = int(self.start_axis_y.get())
            stop_y = int(self.stop_axis_y.get())

            # calculate poisson
            self.poisson1 = self.cal_poisson(S1, P1)
            self.label_poisson1.set(round(self.poisson1, 3))
            self.poisson2 = self.cal_poisson(S2, P2)
            self.label_poisson2.set(round(self.poisson2, 3))
            # calculate Vp/Vs1
            self.vp_vs1 = P1/S1
            self.label_vp_vs1.set(round(self.vp_vs1, 3))
            self.vp_vs2 = P2/S2
            self.label_vp_vs2.set(round(self.vp_vs2, 3))
            # calculate Zp1
            self.zp1 = D1*P1
            self.label_zp1.set(round(self.zp1, 3))
            self.zp2 = D2*P2
            self.label_zp2.set(round(self.zp2, 3))

            ############# part of water #############
            # calculate poisson
            self.poisson1_water = self.cal_poisson(S1_water, P1_water)
            self.label_poisson1_water.set(round(self.poisson1_water, 3))
            self.poisson2_water = self.cal_poisson(S2_water, P2_water)
            self.label_poisson2_water.set(round(self.poisson2_water, 3))
            # calculate Vp/Vs1
            self.vp_vs1_water = P1_water/S1_water
            self.label_vp_vs1_water.set(round(self.vp_vs1_water, 3))
            self.vp_vs2_water = P2_water/S2_water
            self.label_vp_vs2_water.set(round(self.vp_vs2_water, 3))
            # calculate Zp1
            self.zp1_water = D1_water*P1_water
            self.label_zp1_water.set(round(self.zp1_water, 3))
            self.zp2_water = D2_water*P2_water
            self.label_zp2_water.set(round(self.zp2_water, 3))

            ############### part of oil ###############
            # calculate poisson
            self.poisson1_oil = self.cal_poisson(S1_oil, P1_oil)
            self.label_poisson1_oil.set(round(self.poisson1_oil, 3))
            self.poisson2_oil = self.cal_poisson(S2_oil, P2_oil)
            self.label_poisson2_oil.set(round(self.poisson2_oil, 3))
            # calculate Vp/Vs1
            self.vp_vs1_oil = P1_oil/S1_oil
            self.label_vp_vs1_oil.set(round(self.vp_vs1_oil, 3))
            self.vp_vs2_oil = P2_oil/S2_oil
            self.label_vp_vs2_oil.set(round(self.vp_vs2_oil, 3))
            # calculate Zp1
            self.zp1_oil = D1_oil*P1_oil
            self.label_zp1_oil.set(round(self.zp1_oil, 3))
            self.zp2_oil = D2_oil*P2_oil
            self.label_zp2_oil.set(round(self.zp2_oil, 3))
 

            # Calculate A, B, C from Aki-Richards
            A = self.cal_A(P1, P2, D1, D2)
            B = self.cal_B(P1, P2, D1, D2, S1, S2)
            C = self.cal_C(P1, P2)

            #calculate reflection
            self.data_x = [] # data in AVO
            self.data_y = [] # data in Avo
            self.data_x_water = []
            self.data_y_water = []
            self.data_x_oil = []
            self.data_y_oil = []
            # data_x_aki = [] # data in Aki
            # data_y_aki = [] # data in Aki
            for n in range(91):
                t = math.pi
                x = (n*t)/180 # radians
                # AVO
                reflect = self.reflection(P1, D1, P2, D2, self.poisson1, self.poisson2, x)
                reflect_water = self.reflection(P1_water, D1_water, P2_water, D2_water, self.poisson1_water, self.poisson2_water, x)
                reflect_oil = self.reflection(P1_oil, D1_oil, P2_oil, D2_oil, self.poisson1_oil, self.poisson2_oil, x)
                self.data_y.append(float(reflect)) # gas
                self.data_x.append(float(n))
                self.data_y_water.append(float(reflect_water)) # water        
                self.data_y_oil.append(float(reflect_oil)) # oil
               
            # Aki
            # for i in range(80):
            #     t = math.pi
            #     x = (i*t)/180
            #     aki = self.reflaction_aki(A, B, C, x)
            #     data_y_aki.append(float(aki))
            #     data_x_aki.append(float(i))

            ######### calculate and show rp #########
            # part of gas
            self.rp = self.data_y[0]
            self.label_rp.set(round(self.rp, 3))
            # part of water
            self.rp_water = self.data_y_water[0]
            self.label_rp_water.set(round(self.rp_water, 3))
            # part of oil
            self.rp_oil = self.data_y_oil[0]
            self.label_rp_oil.set(round(self.rp_oil, 3))
        
            ############ plot Graph tab 1 ############
            self.Change_axis(start_y, stop_y)

            ################################################################ plot Graph tab 2 ################################################################
            #self.plot_graph_VP_VS_tab2(self.vp_vs1, D1, self.vp_vs2, D2) 

            self.plot_graph_vs_density(S1, D1, S2, D2)
            self.plot_graph_vp_density(P1, D1, P2, D2)
            self.plot_graph_vp_poisson(P1, self.poisson1, P2, self.poisson2)
            self.plot_graph_vs_poisson(S1, self.poisson1, S2, self.poisson2)
            ##################################################################################################################################################
        except ValueError:
            print('Please enter number into field')
            msg.showwarning("Graph Warning","Please enter number into field !!!")


    ########################################################################  Formula  ########################################################################
    
    def cal_poisson(self, s_wave, p_wave):
        # (0.5-(s_wave / p_wave)^2)/(1-(s_wave/p_wave)^2)
        try:
            P = (0.5-(s_wave/p_wave)**2)/(1-(s_wave/p_wave)**2)
            return P
        except ZeroDivisionError:
            print('Zero division')
            msg.showwarning("Graph Warning","Please Check number in field (float division by zero)")
        
    def reflection(self, P1, D1, P2, D2, poisson1, poisson2, x):
        ''' AVO Approximation'''
        try:   
            R = ((P2*D2 - P1*D1)/(P2*D2 + P1*D1))*(math.cos(x)**2)+ (poisson2-poisson1)/((1-(poisson2+poisson1)/2)**2)*(math.sin(x)**2)
            return R
        except ZeroDivisionError:
            print('Zero division')
            msg.showwarning("Graph Warning","Please Check number in field (float division by zero)")
     
    def reflaction_aki(self, A, B, C, theta):
        # r = A+ Bsin^2(theta) + Csin^2(theta)*tan^2(theta)
        try:
            R = A + (B*(math.sin(theta)**2)) + (C * (math.sin(theta)**2)*(math.tan(theta)**2))
            return R
        except ZeroDivisionError:
            print('Zero division')
            msg.showwarning("Graph Warning","Please Check number in field (float division by zero)")

    def cal_A(self, P1, P2, D1, D2):
        # A = 0.5 * (((P2-P1)/Pavg)+ ((D2-D1)/Davg))
        try:
            Pavg = (P1 + P2) / 2
            Davg = (D1 + D2) / 2
            A = 0.5 * (((P2-P1)/Pavg)+ ((D2-D1)/Davg))
            return A
        except ZeroDivisionError:
            print('Zero division')
            msg.showwarning("Graph Warning","Please Check number in field (float division by zero)")
    
    def cal_B(self, P1, P2, D1, D2, S1, S2):
        # B = 0.5*((P2-P1)/Pavg) - 2*((Savg/Pavg)**2)*(2*((S2-S1)/Savg)+(D2-D1)/Davg)
        try:
            Pavg = (P1 + P2) / 2
            Davg = (D1 + D2) / 2
            Savg = (S1 + S2) / 2
            B = 0.5*((P2-P1)/Pavg) - 2*((Savg/Pavg)**2)*(2*((S2-S1)/Savg)+(D2-D1)/Davg)
            return B
        except ZeroDivisionError:
            print('Zero division')
            msg.showwarning("Graph Warning","Please Check number in field (float division by zero)")

    def cal_C(self, P1, P2):
        # C = 0.5 * (P2-P1)/Pavg
        try:
            Pavg = (P1 + P2) / 2 
            C = 0.5 * (P2-P1)/Pavg
            return C
        except ZeroDivisionError:
            print('Zero division')
            msg.showwarning("Graph Warning","Please Check number in field (float division by zero)")
    #########################################################################################################################################################################
    
    
    ###############################################################################    Plot   ###############################################################################

    def plot_graph_change_axis(self,x, y_gas, y_water, y_oil, total_y):
        self.a = self.fig.add_subplot(1,1,1)
        self.a.clear()

        self.a.plot(x, y_gas, label='Gas')
        self.a.plot(x, y_water, label = 'Water')
        self.a.plot(x, y_oil, label= 'Oil')
        #self.a.plot(aki_x, aki_y, label='Aki-Richards')
        self.a.legend()
        self.a.grid(True)
        self.a.set_title('Shuey(AVO) and Aki-Richards Approximation')
        self.a.set_xlabel('Incidence Angle(Degrees)', fontsize=8)
        self.a.set_ylabel('Amplitude', fontsize=8)
        self.a.tick_params(axis="y", labelsize=8, rotation=90)
        self.a.tick_params(axis="x", labelsize=8)
        self.a.set_yticks(total_y)

        self.fig.tight_layout()
        self.canvas.draw()

    def plot_graph(self, x, y_gas, y_water, y_oil):
        # AVO
        self.a = self.fig.add_subplot(1,1,1)
        self.a.clear()
        #a.plot(x,y,label=r'$R(\theta) = \frac{\rho_2 V_2 - \rho_1 V_1}{\rho_2 V_2 + \rho_1 V_1}\cos^2(\theta) + \frac{\sigma_2 - \sigma_1}{(1 - \sigma_{avr})^2}\sin^2(\theta)$')
        self.a.plot(x, y_gas, label='Gas')
        self.a.plot(x, y_water, label = 'Water')
        self.a.plot(x, y_oil, label = 'Oil')

        #self.a.plot(aki_x, aki_y, label='Aki-Richards')
        self.a.legend()
        self.a.grid(True)
        self.a.set_title('Shuey(AVO) and Aki-Richards Approximation')
        self.a.set_xlabel('Incidence Angle(Degrees)', fontsize=8)
        self.a.set_ylabel('Amplitude', fontsize=8)
        self.a.tick_params(axis="y", labelsize=8, rotation=90)
        self.a.tick_params(axis="x", labelsize=8)
        self.fig.tight_layout()
        self.canvas.draw()

    def plot_aki(self,x,y):
        # Aki
        b = self.fig2.add_subplot(111)
        b.clear()
        b.plot(x,y)
        b.set_title('Aki-Richards Approximation')
        b.set_xlabel('Incidence Angle(Degrees)', fontsize=8)
        b.set_ylabel('Reflection Coefficient', fontsize=8)
        b.grid(True)
        b.tick_params(axis="y", labelsize=8, rotation=90)
        b.tick_params(axis="x", labelsize=8)
        b.set_xticks([0, 10, 20, 30, 40, 50, 60, 70, 80 ,90])
        self.canvas2.draw()

    def Change_axis(self,start_y, stop_y):
        step = float(self.step.get())
        total_y = []
        if start_y == int(0) and stop_y == int(0):
            self.plot_graph(self.data_x, self.data_y, self.data_y_water, self.data_y_oil)
        else:
            
            for i in self.frange(start_y, stop_y+1,step):
                total_y.append(float(i))
            self.plot_graph_change_axis(self.data_x, self.data_y, self.data_y_water, self.data_y_oil, total_y)
        

    def frange(self,start, stop=None, step=None):
        #Use float number in range() function
        # if stop and step argument is null set start=0.0 and step = 1.0
        if stop == None:
            stop = start + 0.0
            start = 0.0
        if step == None:
            step = 1.0
        while True:
            if step > 0 and start >= stop:
                break
            elif step < 0 and start <= stop:
                break
            yield ("%g" % start) # return float number
            start = start + step

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
####################0
if __name__ == "__main__":
    app = Graph()
    app.mainloop()
