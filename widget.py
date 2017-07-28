from tkinter import *
#top = tkinter.Tk()
# Code to add widgets will go here...
print ("Testing first window")
#top.mainloop()

m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left pane")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

m3 = PanedWindow(m1, orient=VERTICAL)
m1.add(m3)

top = Label(m2, text="top pane 2")
m2.add(top)

bottom = Label(m2, text="bottom pane 2")
m2.add(bottom)

top = Label(m3, text="top pane 3")
m3.add(top)

bottom = Label(m3, text="bottom pane 3")
m3.add(bottom)

mainloop()


