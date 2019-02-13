import tkinter as tk

master = tk.Tk()
master.title("學生登入介面")
master.geometry("200x150+500+200")

label_title = tk.Label(master, text="登入資訊")
label_title.grid(column=1,row=0)
# account
label_acc = tk.Label(master, text="學號")
label_acc.grid(column=0, row=1)

label_pw = tk.Label(master, text="密碼")
label_pw.grid(column=0, row=2)

# entry
entry_acc = tk.Entry(master).grid(column=1, row=1)
entry_pw = tk.Entry(master).grid(column=1, row=2)

master.mainloop()