import numpy as np
from time import sleep
from tkinter import *
#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

class App:
    def __init__(self,root,arr,graph1,graph2,graph3):
        frame=Frame(root)
        self.runningF=False
        self.runningB=False
        self.f = Figure(figsize=(15,3))
        self.a = self.f.add_subplot(131)
        self.b = self.f.add_subplot(332)
        self.c = self.f.add_subplot(335)
        self.d = self.f.add_subplot(338)
        self.e = self.f.add_subplot(133)
        self.time=arr.shape[0]
        self.i=0
        self.btnF = Button(frame,text="Next",command=self.NextStep)
        self.btnF.pack(side="right")
        self.btnB = Button(frame,text="Previous",command=self.LastStep)
        self.btnB.pack(side="left")
        self.btnPF = Button(frame,text="Play Forward",command=self.animate_forward)
        self.btnPF.pack(side="right")
        self.btnPB = Button(frame,text="Play Backward",command=self.animate_backward)
        self.btnPB.pack(side="left")
        self.btnstop = Button(frame,text="Stop",command=self.stopTask)
        self.btnstop.pack()
        
        if (self.i < self.time):
            print(self.i)
            self.img = self.getFrame(self.i,arr)      
            self.pic=self.a.imshow(self.img)
            #self.a.set_title("Time=%d" % self.i)
            self.b.plot(range(self.time),graph1)
            self.bline, =self.b.plot([self.i],graph1[self.i],marker="*")
            #self.b.set_title("Graph 1")
            self.c.plot(range(self.time),graph2)
            self.cline, =self.c.plot([self.i],graph2[self.i],marker="*")
            #self.c.set_title("Graph 2")
            self.d.plot(range(self.time),graph3)
            self.dline, =self.d.plot([self.i],graph3[self.i],marker="*")
            #self.d.set_title("Graph 3")
            self.e.plot(range(self.time),np.zeros(self.time),color="red")
            self.eline,=self.e.plot([self.i,self.i],[-10,10], color="red")
            self.canvas = FigureCanvasTkAgg(self.f, master=root)
            self.canvas.show()
            self.canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
            frame.pack()
            
        #root.after(1,self.contForward)
        #root.after(1,self.contBackward)
    
    def getFrame(self,i, arr):
            if arr.shape[0] <=i:
                return np.zeros([arr.shape[1],arr.shape[2],3])
            else:
                return arr[i]

    def NextStep(self):
            #print ("button pressed")
            if (self.i < self.time-1):
                self.i=self.i+1
            else:
                self.i=self.i
            self.refreshFigures()

            
    def LastStep(self):
            #print ("button pressed")
            if (self.i>0):
                self.i=self.i-1
            else:
                self.i=self.i
            self.refreshFigures()

            
    def PlayForward(self):
            #print ("button pressed")
            self.runningF=True
            
                
    def PlayBackward(self):
            #print ("button pressed")
            self.runningB=True
            

    def stopTask(self):
            self.runningF=False
            self.runningB=False

    def contForward(self):
            if (self.runningF and (self.i < self.time)):
                self.i=self.i+1
                self.refreshFigures()
                #print( "Forward %d" % self.i)
            root.after(1, self.contForward)

    def contBackward(self):
            if (self.runningB and (self.i > 0)):
                self.i=self.i-1
                self.refreshFigures()
                #print( "Backward %d" % self.i)
            root.after(1, self.contBackward)


    def animate_forward(self):
            self.runningF=True
            ani = FuncAnimation(self.f,self.refreshFiguresani,self.iteratorF,blit=True, interval=1,repeat=True)
            self.canvas.draw()

    def iteratorF(self):
            ii=self.i
            while ii<(self.time-1):
                if self.runningF:
                    ii+=1
                yield ii

    def animate_backward(self):
            self.runningB=True
            ani = FuncAnimation(self.f,self.refreshFiguresani,self.iteratorB,blit=True, interval=1,repeat=True)
            self.canvas.draw()

    def iteratorB(self):
            ii=self.i
            while ii>0:
                if self.runningB:
                    ii=ii-1
                yield ii


    def refreshFigures(self):
            self.img = self.getFrame(self.i,arr)
            self.e.cla()
            self.a.cla()
            self.a.imshow(self.img)
            self.a.set_title("Time=%d" % self.i)
            self.b.plot(range(max([0,self.i-2]),min([self.i,self.time])),graph1[max([0,self.i-2]):min([self.i,self.time])],color="red")
            self.c.plot(range(max([0,self.i-2]),min([self.i,self.time])),graph2[max([0,self.i-2]):min([self.i,self.time])],color="red")
            self.c.set_title("Graph 2")
            self.d.plot(range(max([0,self.i-2]),min([self.i,self.time])),graph3[max([0,self.i-2]):min([self.i,self.time])],color="red")
            self.d.set_title("Graph 3")
            self.e.plot(range(self.time),np.zeros(self.time),color="red")
            self.e.plot([self.i,self.i],[-10,10], color="red")
            self.canvas.draw()

    def refreshFiguresani(self,ii):
            self.img = self.getFrame(ii,arr)
            #self.a.imshow(self.img)
            #self.pic.set_title("Time=%d" % ii)
            self.pic.set_data(self.img)
            self.bline.set_data([ii],graph1[ii])
            self.cline.set_data([ii],graph2[ii])
            self.dline.set_data([ii],graph3[ii])
            self.eline.set_data([ii,ii],[-10,10])
            return self.bline, self.cline, self.dline, self.eline, self.pic
        
   
        
            
    
    
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
            arr[i][j][k][0]=i
            arr[i][j][k][1]=i
            arr[i][j][k][2]=i
            

#print (getFrame(2,arr))
#makeWidget(arr,5)
root = Tk()
app=App(root,arr,graph1,graph2,graph3)
root.mainloop()
