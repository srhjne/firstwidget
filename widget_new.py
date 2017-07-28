import numpy as np
from time import sleep
from tkinter import *
#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class App:
    def __init__(self,root,arr):
        frame=Frame(root)
        f = Figure()
        self.a = f.add_subplot(221)
        self.b = f.add_subplot(222)
        self.time=arr.shape[2]
        self.i=0
        self.btn = Button(frame,text="Next",command=self.NextStep)
        self.btn.pack(side="left")
        if (self.i < self.time):
            print(self.i)
            self.img = self.getFrame(self.i,arr)      
            self.a.imshow(self.img)
            self.a.set_title(self.i)
            self.b.plot(self.img[1])
            self.canvas = FigureCanvasTkAgg(f, master=root)
            self.canvas.show()
            self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
            frame.pack()
    
    def getFrame(self,i, arr):
            if arr.shape[2] <=i:
                return np.zeros(arr.shape[0],arr.shape[1])
            else:
                return arr[:][:][i]

    def NextStep(self):
            print ("button pressed")
            self.i=self.i+1
            self.img = self.getFrame(self.i,arr)      
            self.a.imshow(self.img)
            self.a.set_title(self.i)
            self.b.plot(self.img[1])
            #self.canvas = FigureCanvasTkAgg(f, master=root)
            self.canvas.draw()
            
            

    def makeWidget(arr,time):
            print (time)
            root=Tk()
            frame=Frame(root)
            f = Figure(figsize=(100,100), dpi=100)
            a = f.add_subplot(221)
            b = f.add_subplot(222)
            for i in range(time):
                print(i)
                img = getFrame(i,arr)      
                a.imshow(img)
                a.set_title(i)
                b.plot(img[1])
                canvas = FigureCanvasTkAgg(f, master=root)
                canvas.show()
                canvas.draw()
                canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
                btn = Button(root,text="Next",command=NextStep)
                btn.pack()
                frame.pack()
                sleep(1)
            root.mainloop()


    
arr=np.ndarray([10,10,10])
for i in range(10):
    for j in range(10):
        for k in range(10):
            arr[i][j][k]=i+j+k

#print (getFrame(2,arr))
#makeWidget(arr,5)
root = Tk()
app=App(root,arr)
root.mainloop()
