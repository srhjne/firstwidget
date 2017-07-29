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
        self.f = Figure(figsize=(9,3))
        self.a = self.f.add_subplot(131)
        self.b = self.f.add_subplot(132)
        self.c = self.f.add_subplot(133)
        self.time=arr.shape[0]
        self.i=0
        self.btnF = Button(frame,text="Next",command=self.NextStep)
        self.btnF.pack(side="right")
        self.btnB = Button(frame,text="Previous",command=self.LastStep)
        self.btnB.pack(side="left")
        self.btnPF = Button(frame,text="Play Forward",command=self.PlayForward)
        self.btnPF.pack(side="right")
        self.btnPB = Button(frame,text="Play Backward",command=self.PlayBackward)
        self.btnPB.pack(side="left")
        #self.btnstop = Button(frame,text="Stop",command=self.pause)
        #self.btnstop.pack()
        if (self.i < self.time):
            print(self.i)
            self.img = self.getFrame(self.i,arr)      
            self.a.imshow(self.img)
            self.a.set_title("Time=%d" % self.i)
            self.b.plot(self.img[1])
            self.b.set_title("RGB values in first line")
            self.c.plot(range(self.time),np.zeros(self.time),color="red")
            self.c.plot([self.i,self.i],[-10,10], color="red")
            self.canvas = FigureCanvasTkAgg(self.f, master=root)
            self.canvas.show()
            self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
            frame.pack()
    
    def getFrame(self,i, arr):
            if arr.shape[0] <=i:
                return np.zeros(arr.shape[1],arr.shape[2])
            else:
                return arr[i]

    def NextStep(self):
            print ("button pressed")
            if (self.i < self.time-1):
                self.i=self.i+1
            else:
                self.i=self.i
            self.img = self.getFrame(self.i,arr)
            self.c.cla()
            self.b.cla()
            self.b = self.f.add_subplot(132)
            self.c = self.f.add_subplot(133)
            self.c.plot(range(self.time),np.zeros(self.time),color="red")
            self.a.imshow(self.img)
            self.a.set_title("Time=%d" % self.i)
            self.b.plot(self.img[1])
            self.b.set_title("RGB values in first line")
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
            self.b = self.f.add_subplot(132)
            self.c = self.f.add_subplot(133)
            self.c.plot(range(self.time),np.zeros(self.time),color="red")
            self.a.imshow(self.img)
            self.a.set_title("Time=%d" % self.i)
            self.b.plot(self.img[1])
            self.b.set_title("RGB values in first line")
            self.c.plot([self.i,self.i],[-10,10], color="red")
            #self.canvas = FigureCanvasTkAgg(f, master=root)
            self.canvas.draw()
            
    def PlayForward(self):
            print ("button pressed")
            while (self.i < self.time):
                self.i=self.i+1
                self.img = self.getFrame(self.i,arr)
                self.c.cla()
                self.b.cla()
                self.b = self.f.add_subplot(132)
                self.c = self.f.add_subplot(133)
                self.c.plot(range(self.time),np.zeros(self.time),color="red")
                self.a.imshow(self.img)
                self.a.set_title("Time=%d" % self.i)
                self.b.plot(self.img[1])
                self.b.set_title("RGB values in first line")
                self.c.plot([self.i,self.i],[-10,10], color="red")
                #self.canvas = FigureCanvasTkAgg(f, master=root)
                self.canvas.draw()
                
    def PlayBackward(self):
            print ("button pressed")
            while (self.i > 0):
                self.i=self.i-1
                self.img = self.getFrame(self.i,arr)
                self.c.cla()
                self.b.cla()
                self.b = self.f.add_subplot(132)
                self.c = self.f.add_subplot(133)
                self.c.plot(range(self.time),np.zeros(self.time),color="red")
                self.a.imshow(self.img)
                self.a.set_title("Time=%d" % self.i)
                self.b.plot(self.img[1])
                self.b.set_title("RGB values in first line")
                self.c.plot([self.i,self.i],[-10,10], color="red")
                #self.canvas = FigureCanvasTkAgg(f, master=root)
                self.canvas.draw()

   
        
            
    
    
arr=np.ndarray([326,210,160,3])
for i in range(326):
    for j in range(210):
        for k in range(160):
            arr[i][j][k][0]=i%256
            arr[i][j][k][1]=j%256
            arr[i][j][k][2]=k%256

#print (getFrame(2,arr))
#makeWidget(arr,5)
root = Tk()
app=App(root,arr)
root.mainloop()
