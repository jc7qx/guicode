#_*_ coding:utf-8 _*_

# 導入 tkinter 模組
# 建立主視窗
# 改變視窗屬性
# 增加視窗小元件
# 執行主視窗 mainloop()函式是一個無限迴圈

import tkinter

m = tkinter.Tk()

m.title("my first window")
btn1 = tkinter.Button(m, text="離開", width=25, command=m.destroy)
btn1.pack()

m.mainloop()