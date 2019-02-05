from tkinter import *
  
root = Tk() #主視窗
frame = Frame(root) #元件容器#1
frame.pack() 
bottomframe = Frame(root) #元件容器#2
bottomframe.pack( side = BOTTOM ) 

redbutton = Button(frame, text = 'Red', fg ='green') 
redbutton.pack( side = LEFT) 
greenbutton = Button(frame, text = 'Brown', fg='black') 
greenbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text ='Blue', fg ='red') 
bluebutton.pack( side = LEFT ) 

blackbutton = Button(bottomframe, text ='Black', fg ='gray') 
blackbutton.pack( side = BOTTOM) 
root.mainloop() 