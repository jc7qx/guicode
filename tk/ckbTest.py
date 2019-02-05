from tkinter import *
master = Tk() 
var1 = IntVar() 
Checkbutton(master, text='男生', variable=var1, activebackground="yellow").grid(row=0, sticky=W) 
var2 = IntVar() 
Checkbutton(master, text='女生', variable=var2, activeforeground="red").grid(row=1, sticky=W) 
mainloop() 