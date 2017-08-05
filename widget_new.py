import numpy as np
import pickle
from time import sleep
from tkinter import *
#import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation

class App:
    def __init__(self,root,arr,graph1,graph2,graph3,map4):
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
            self.a.axes.get_xaxis().set_visible(False)
            self.a.axes.get_yaxis().set_visible(False)
            #self.a.set_title("Time=%d" % self.i)
            self.b.plot(range(self.time),graph1)
            self.b.axes.set_xticklabels([])
            self.bline, =self.b.plot([self.i],graph1[self.i],marker="*")
            #self.b.set_title("Graph 1")
            self.c.plot(range(self.time),graph2)
            self.c.axes.set_xticklabels([])
            self.cline, =self.c.plot([self.i],graph2[self.i],marker="*")
            #self.c.set_title("Graph 2")
            self.d.plot(range(self.time),graph3)
            self.dline, =self.d.plot([self.i],graph3[self.i],marker="*")
            #self.d.set_title("Graph 3")
            self.mapimg = self.getFrame(self.i,map4)
            self.mappic = self.e.imshow(self.mapimg)
            self.e.axes.get_xaxis().set_visible(False)
            self.e.axes.get_yaxis().set_visible(False)
            #self.e.plot(range(self.time),np.zeros(self.time),color="red")
            #self.eline,=self.e.plot([self.i,self.i],[-10,10], color="red")
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
            self.refreshFiguresani(self.i)
            #ani = FuncAnimation(self.f,self.refreshFiguresani,frames=[self.i],blit=True, interval=1,repeat=True)
            self.canvas.draw()

            
    def LastStep(self):
            #print ("button pressed")
            if (self.i>0):
                self.i=self.i-1
            else:
                self.i=self.i
            self.refreshFiguresani(self.i)
            #ani = FuncAnimation(self.f,self.refreshFiguresani,frames=[self.i],blit=True, interval=1,repeat=True)

            
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
            while self.runningF:
                ii=(ii+1)%self.time
                self.i=(self.i+1)%self.time
                yield ii

    def animate_backward(self):
            self.runningB=True
            ani = FuncAnimation(self.f,self.refreshFiguresani,self.iteratorB,blit=True, interval=1,repeat=True)
            self.canvas.draw()

    def iteratorB(self):
            ii=self.i
            while (self.runningB):
                ii=(self.time+ii-1)%self.time
                self.i=(self.time+self.i-1)%self.time
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
            self.mapimg = self.getFrame(self.i,map4)
            self.mappic.set_data(self.mapimg)
            return self.bline, self.cline, self.dline, self.mappic, self.pic
        
   
        
file = open("video2700.pkl","rb")
object_file=pickle.load(file)
file.close() 


graph1=np.ndarray(853)
graph2=np.ndarray(853)
graph3=np.ndarray(853)
    
arr=np.ndarray([853,210,160,3])
map4=np.ndarray([853,84,168,3])
#graph1=np.ndarray(326)
#graph2=np.ndarray(326)
#graph3=np.ndarray(326)
for i in range(853):
    graph1[i]=object_file[i][1]
    graph2[i]=object_file[i][2]
    graph3[i]=object_file[i][3]
    for j in range(210):
        for k in range(160):
            arr[i][j][k][0]=object_file[i][0][j][k][0]
            arr[i][j][k][1]=object_file[i][0][j][k][1]
            arr[i][j][k][2]=object_file[i][0][j][k][2]
    for j in range(84):
        for k in range(168):
            map4[i][j][k][0]=object_file[i][4][j][k]
            map4[i][j][k][1]=object_file[i][4][j][k]
            map4[i][j][k][2]=object_file[i][4][j][k]
            
            

#file = open("video2700.pkl","r")
#object_file=pickle.load(file)
#file.close()

#print (getFrame(2,arr))
#makeWidget(arr,5)
root = Tk()
app=App(root,arr,graph1,graph2,graph3,map4)
root.mainloop()
