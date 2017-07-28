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
        self.f = Figure()
        self.a = self.f.add_subplot(221)
        self.b = self.f.add_subplot(222)
        self.c = self.f.add_subplot(223)
        self.time=arr.shape[2]
        self.i=0
        self.btnF = Button(frame,text="Next",command=self.NextStep)
        self.btnF.pack(side="right")
        self.btnB = Button(frame,text="Previous",command=self.LastStep)
        self.btnB.pack(side="left")
        if (self.i < self.time):
            print(self.i)
            self.img = self.getFrame(self.i,arr)      
            self.a.imshow(self.img)
            self.a.set_title(self.i)
            self.b.plot(self.img[1])
            self.c.plot(range(self.time),np.zeros(self.time),color="red")
            self.c.plot([self.i,self.i],[-10,10], color="red")
            self.canvas = FigureCanvasTkAgg(self.f, master=root)
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
            if (self.i < self.time-1):
                self.i=self.i+1
            else:
                self.i=self.i
            self.img = self.getFrame(self.i,arr)
            self.c.cla()
            self.b.cla()
            self.b = self.f.add_subplot(222)
            self.c = self.f.add_subplot(223)
            self.c.plot(range(self.time),np.zeros(self.time),color="red")
            self.a.imshow(self.img)
            self.a.set_title(self.i)
            self.b.plot(self.img[1])
            self.c.plot([self.i,self.i],[-10,10], color="red")
            #self.canvas = FigureCanvasTkAgg(f, master=root)
            self.canvas.draw()

    def LastStep(self):
            print ("button pressed")
            if (self.i>0):
                self.i=self.i-1
            else:
                self.i=self.i
            self.img = self.getFrame(self.i,arr)
            self.c.cla()
            self.b.cla()
            self.b = self.f.add_subplot(222)
            self.c = self.f.add_subplot(223)
            self.c.plot(range(self.time),np.zeros(self.time),color="red")
            self.a.imshow(self.img)
            self.a.set_title(self.i)
            self.b.plot(self.img[1])
            self.c.plot([self.i,self.i],[-10,10], color="red")
            #self.canvas = FigureCanvasTkAgg(f, master=root)
            self.canvas.draw()
            
    
    
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
