from tkinter import *
from tkinter.ttk import *
from time import strftime


root = Tk()
root.title('My Clock')
root.attributes('-alpha',0.5)

def time():
    string = strftime('%H:%M:%S')
    the_lable.config(text=string)
    the_lable.after(1000,time)


topLevelWindow = root.winfo_toplevel()
root.overrideredirect(1)
the_lable = topLevelWindow.attributes('-topmost', 'true')
the_lable = Label(root, font=("ds-digital",80),background ="",foreground="black",width=7)
the_lable.pack(anchor='center')


time()
mainloop()

