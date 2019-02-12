import tkinter as tk

counter = 0 
def counter_label(label):
  counter = 0
  def count():
    global counter
    counter += 1
    label.config(text=str(counter)) #設定標籤內容
    label.after(1000, count) #隔1000微秒後，執行count函式
  count()
 
 
root = tk.Tk()
root.title("Counting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label) #改變標籤內容
button = tk.Button(root, text='Stop', width=25, command=root.destroy)
button.pack()
root.mainloop()