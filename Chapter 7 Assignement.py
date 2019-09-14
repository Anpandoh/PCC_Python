from tkinter import *
from time import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.myCanvas = Canvas(width=750, height=750, bg = "light blue")
        self.myCanvas.grid()
        self.myCanvas.create_rectangle(100,200,120,500, fill="grey", outline="grey")
        self.myCanvas.create_rectangle(25,125,195,200, fill = "white", outline = "white")
        #self.myCanvas.create_line(25,150,195,150)
        self.myCanvas.create_arc(25,75,195,175,style = "pieslice", fill = "white",extent = "180", outline = "white")
        self.myCanvas.create_rectangle(85,125,135,175,width="5",outline = "orange",fill="white")
        self.myCanvas.create_oval(85,180,135,190,width = "2.5", outline = "orange")
        self.myCanvas.create_rectangle(95,175,125,180, fill="orange",outline = "orange")

        basketball = self.myCanvas.create_oval(300,300,350,350, fill="orange",width="2.0")
        for count in range(200):
            a = -count
            b = -(0.1*count)**2-10
            c= -count+140
            d= -count+141
            print("c=",c)
            print("d=",d)
            if -b < 200:
                self.myCanvas.coords(basketball, 300+a, 300+b,350+a,350+b)
                self.myCanvas.update()
            else:
                self.myCanvas.coords(basketball, 160+d, 100-c,210+d,150-c)
                self.myCanvas.update()
            sleep(.04)
        
frame01 = MyFrame()
frame01.mainloop()
