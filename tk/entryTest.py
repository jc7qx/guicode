from tkinter import *
master = Tk() 
Label(master, text='姓名').grid(row=0) 
Label(master, text='學號').grid(row=1) 
e1 = Entry(master, bg="yellow") 
e2 = Entry(master, bg="lightblue") 
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
mainloop()