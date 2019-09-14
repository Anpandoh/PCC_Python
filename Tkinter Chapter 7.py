from tkinter import *
from time import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.myCanvas = Canvas(width=300, height=200, bg="blue")
        self.myCanvas.grid()

        #self.myCanvas.create_rectangle(10, 10, 100, 100, fill="magenta")
        #self.myCanvas.create_text(50, 50, text="Hello World")
        #self.myCanvas.update()

        #sleep(1)

        #self.myCanvas.create_rectangle(20, 20, 60, 60)

        #for count in range(10):
         #   space = 10*count
          #  self.myCanvas.create_rectangle(10 + space, 10 + space, 50 + space, 50 + space, fill = "green")
           # self.myCanvas.update()
            #sleep(0.1)

            #self.myCanvas.create_rectangle(10 + space,10 + space, 50 + space, 50 + space, outline="blue", fill = "blue")
        my_rect = self.myCanvas.create_rectangle(10, 10, 50, 50, outline="blue", fill="lime")     
        for count in range(10):
          increment = 10*count
          self.myCanvas.coords(my_rect, 10 + increment, 10 + increment, 50 + increment, 50 + increment)
          self.myCanvas.update()
          sleep(.04)

frame02 = MyFrame()
frame02.mainloop()

