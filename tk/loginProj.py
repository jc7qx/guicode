import tkinter as tk

master = tk.Tk()
master.title("學生登入介面")
#master.geometry("200x150+500+200")

label_title = tk.Label(master, text="登入資訊")
label_title.grid(column=0, row=0, columnspan=2, padx=3, pady=3)
# account
label_acc = tk.Label(master, text="學號").grid(column=0, row=1, padx=3)
entry_acc = tk.Entry(master).grid(column=1, row=1, padx=3)
label_pw = tk.Label(master, text="密碼").grid(column=0, row=2, padx=3, pady=3)
entry_pw = tk.Entry(master).grid(column=1, row=2, padx=3, pady=10)

#sendBtn = tk.Button(master, text="提交資料").grid(column=0, row=3, padx=3, pady=3)
#resetBtn = tk.Button(master, text="清除資料").grid(column=1, row=3, padx=3, pady=3, sticky=tk.W)

master.mainloop()