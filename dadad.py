from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()

class WindowDraggable():

    def __init__(self, label):
        self.label = label
        label.bind('<ButtonPress-1>', self.StartMove)
        label.bind('<ButtonRelease-1>', self.StopMove)
        label.bind('<B1-Motion>', self.OnMotion)
        label.bind(self.time)
        topLevelWindow = root.winfo_toplevel()
        root.overrideredirect(1)

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def StopMove(self, event):
        self.x = None
        self.y = None

    def OnMotion(self,event):
        x = (event.x_root - self.x - self.label.winfo_rootx() + self.label.winfo_rootx())
        y = (event.y_root - self.y - self.label.winfo_rooty() + self.label.winfo_rooty())
        root.geometry("+%s+%s" % (x, y))
    def time():
        string = strftime('%H:%M:%S')
        the_lable.config(text=string)
        the_lable.after(1000,time)

#the_lable = topLevelWindow.attributes('-topmost', 'true')
#the_lable = WindowDraggable.time()
the_lable = Label(root, font=("ds-digital",80),background ="",foreground="springgreen",width=7)
the_lable.pack(anchor='center')
the_lable = Label(root,text="Drag this shit")
WindowDraggable(the_lable)
the_lable.pack()
root.mainloop()