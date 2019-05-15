import tkinter as tk
import matplotlib.pyplot as plt

class GraphGui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.top_fram = tk.Frame(self).pack()
        self.bottom_fram = tk.Frame(self).pack(side = "bottom")

        tk.Label(self.bottom_fram,text="x1 :").pack()
        self.x1 = tk.Entry(self.bottom_fram)
        self.x1.pack()
        
        tk.Label(self.bottom_fram,text="y1 :").pack()
        self.y1 = tk.Entry(self.bottom_fram)
        self.y1.pack()

        tk.Label(self.bottom_fram,text="x2 :").pack()
        self.x2 = tk.Entry(self.bottom_fram)
        self.x2.pack()

        tk.Label(self.bottom_fram,text="y2 :").pack()
        self.y2 = tk.Entry(self.bottom_fram)
        self.y2.pack()

        self.button = tk.Button(self.bottom_fram, text="Plot", command=self.on_button)
        self.button.pack(side='left')

        self.btn_exit = tk.Button(self.bottom_fram, text='Quit', command=self.quit)
        self.btn_exit.pack(side='right')

    def on_button(self):
        data_x1 = float(self.x1.get())
        data_y1 = float(self.y1.get())
        data_x2 = float(self.x2.get())
        data_y2 = float(self.y2.get())

        print("x1: {} y1: {}\nx2: {} y2: {}".format(data_x1, data_y1, data_x2, data_y2))
        self.plot_gui(data_x1, data_y1, data_x2, data_y2)
        
    def plot_gui(self,x1,y1,x2,y2):
         plt.plot([x1,y1,x2,y2])
         plt.show()


app = GraphGui()
app.mainloop()