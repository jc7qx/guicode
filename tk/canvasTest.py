from tkinter import *

# 建立主視窗，master是一個主視窗物件變數
master = Tk()

# 畫布元件可顯示圖形影像，也可佈放視窗元件
w = Canvas(master, width=400, height=320, bg="lightblue") 

# 視窗小元件佈放方式，有pack(), grid(), place()三種方式
w.pack() 
canvas_height=40
canvas_width=100
y = int(canvas_height / 2) 
w.create_line(0, y, canvas_width, y ) 
mainloop()