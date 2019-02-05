from tkinter import *
main = Tk() 
ourMessage ='This is our Messages'
messageVar = Message(main, text = ourMessage, bg='lightblue') 
messageVar.config(width=200) 
messageVar.pack( ) 
main.mainloop( ) 
