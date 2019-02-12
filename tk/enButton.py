import tkinter as tk
    
#Button處理函式
def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk() #建立主視窗

frame = tk.Frame(root) #建立視窗框架frame
frame.pack()

#建立QUIT按鈕元件
button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)

#建立slogan按鈕元件,並設計處理函式
slogan = tk.Button(frame,
                   text="Hello",
                   fg="blue",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()