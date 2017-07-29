import numpy as np
from time import sleep
from tkinter import *
#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class App:
    def __init__(self,root,arr,graph1,graph2,graph3):
        frame=Frame(root)
        self.runningF=False
        self.runningB=False
        self.f = Figure(figsize=(15,3))
        self.a = self.f.add_subplot(151)
        self.b = self.f.add_subplot(152)
        self.c = self.f.add_subplot(153)
        self.d = self.f.add_subplot(154)
        self.e = self.f.add_subplot(155)
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
        self.btnstop = Button(frame,text="Stop",command=self.stopTask)
        self.btnstop.pack()
        
        if (self.i < self.time):
            print(self.i)
            self.img = self.getFrame(self.i,arr)      
            self.a.imshow(self.img)
            self.a.set_title("Time=%d" % self.i)
            self.b.plot(range(max([0,self.i-30]),min([self.i,self.time])),graph1[max([0,self.i-30]):min([self.i,self.time])])
            self.b.set_title("Graph 1")
            self.c.plot(range(max([0,self.i-30]),min([self.i,self.time])),graph2[max([0,self.i-30]):min([self.i,self.time])])
            self.c.set_title("Graph 2")
            self.d.plot(range(max([0,self.i-30]),min([self.i,self.time])),graph3[max([0,self.i-30]):min([self.i,self.time])])
            self.d.set_title("Graph 3")
            self.e.plot(range(self.time),np.zeros(self.time),color="red")
            self.e.plot([self.i,self.i],[-10,10], color="red")
            self.canvas = FigureCanvasTkAgg(self.f, master=root)
            self.canvas.show()
            self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
            frame.pack()
            
        root.after(1,self.contForward)
        root.after(1,self.contBackward)
    
    def getFrame(self,i, arr):
            if arr.shape[0] <=i:
                return np.zeros([arr.shape[1],arr.shape[2],3])
            else:
                return arr[i]

    def NextStep(self):
            print ("button pressed")
            if (self.i < self.time-1):
                self.i=self.i+1
            else:
                self.i=self.i
            self.refreshFigures()

            
    def LastStep(self):
            print ("button pressed")
            if (self.i>0):
                self.i=self.i-1
            else:
                self.i=self.i
            self.refreshFigures()

            
    def PlayForward(self):
            print ("button pressed")
            self.runningF=True
            
                
    def PlayBackward(self):
            print ("button pressed")
            self.runningB=True
            

    def stopTask(self):
            self.runningF=False
            self.runningB=False

    def contForward(self):
            if (self.runningF and (self.i < self.time)):
                self.i=self.i+1
                self.refreshFigures()
                print( "Forward %d" % self.i)
            root.after(1, self.contForward)

    def contBackward(self):
            if (self.runningB and (self.i > 0)):
                self.i=self.i-1
                self.refreshFigures()
                print( "Backward %d" % self.i)
            root.after(1, self.contBackward)
                


    def refreshFigures(self):
            self.img = self.getFrame(self.i,arr)
            self.c.cla()
            self.b.cla()
            self.d.cla()
            self.e.cla()
            self.a.imshow(self.img)
            self.a.set_title("Time=%d" % self.i)
            self.b.plot(range(max([0,self.i-30]),min([self.i,self.time])),graph1[max([0,self.i-30]):min([self.i,self.time])])
            #self.line1.set_xdata(range(max([0,self.i-30]),min([self.i,self.time])))
            #self.line1.set_ydata(graph1[max([0,self.i-30]):min([self.i,self.time])])
            self.b.set_title("Graph 1")
            self.c.plot(range(max([0,self.i-30]),min([self.i,self.time])),graph2[max([0,self.i-30]):min([self.i,self.time])])
            self.c.set_title("Graph 2")
            self.d.plot(range(max([0,self.i-30]),min([self.i,self.time])),graph3[max([0,self.i-30]):min([self.i,self.time])])
            self.d.set_title("Graph 3")
            self.e.plot(range(self.time),np.zeros(self.time),color="red")
            self.e.plot([self.i,self.i],[-10,10], color="red")
            self.canvas.draw()
        
   
        
            
    
    
arr=np.ndarray([326,210,160,3])
graph1=np.ndarray(326)
graph2=np.ndarray(326)
graph3=np.ndarray(326)
for i in range(326):
    graph1[i]=np.cos(i*np.pi/80)
    graph2[i]=np.sin(i*np.pi/50)
    graph3[i]=np.cos(i*np.pi/30)
    for j in range(210):
        for k in range(160):
            arr[i][j][k][0]=i%256
            arr[i][j][k][1]=j%256
            arr[i][j][k][2]=k%256
            

#print (getFrame(2,arr))
#makeWidget(arr,5)
root = Tk()
app=App(root,arr,graph1,graph2,graph3)
root.mainloop()
