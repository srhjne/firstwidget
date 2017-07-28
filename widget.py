from tkinter import *
import numpy as np
from PIL import Image
from tkinter import filedialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure


root=Tk()

arr=np.ndarray([100,100,100])
for i in range(100):
    for j in range(100):
        for k in range(100):
            arr[i][j][k]=(i+j+2*k)

print (arr[50][1])


print ("Testing first window")


#m1 = PanedWindow()
#m1.pack(fill=BOTH, expand=1, ipadx=300, ipady=100)


left = Label(text="left pane", width=30)
#m1.add(left)


f = Figure(figsize=(100,100), dpi=100)
a = f.add_subplot(111)
#a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
def updateImage():
    for i in range(100):
        img = Image.fromarray(arr[i], 'RGB')
        a.imshow(img)
        canvas = FigureCanvasTkAgg(f, left)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        canvas = FigureCanvasTkAgg(f, left)
        canvas.show()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        #m1.add(left)

#canvas = FigureCanvasTkAgg(f, left)
#canvas.show()
#canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)


#toolbar = NavigationToolbar2TkAgg(canvas,left)
#toolbar.update()
#canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
#b = Button(left,compound=BOTTOM, text="Play")
#b.pack()
#m1.add(left)


##m2 = PanedWindow(m1, orient=VERTICAL)
##m1.add(m2)



##top = Label(m2, text="top pane 2",width=30, height=10)
#m2.add(top)

##f = Figure(figsize=(5,5), dpi=100)
##a = f.add_subplot(111)
##a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#a.imshow(img)

##canvas = FigureCanvasTkAgg(f, top)
##canvas.show()
##canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)

##canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
##m2.add(top)

##bottom = Label(m2, text="bottom pane 2")
##m2.add(bottom)

#m3 = PanedWindow(m1, orient=VERTICAL)
#m1.add(m3)

#top = Label(m3, text="top pane 3")
#m3.add(top)

#bottom = Label(m3, text="bottom pane 3")
#m3.add(bottom)
root.after(1000,updateImage)
root.mainloop()


