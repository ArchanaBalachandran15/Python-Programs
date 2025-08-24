import tkinter as tk

def Calculator():
    try:
        result=eval(entry.get())
        label_result.config(text="Result: " + str(result))
    except:
        label_result.config(text="Eroor in Exception")

root=tk.Tk()
root.title("Calculator")
root.geometry("600x200")

entry=tk.Entry(root, width=30)
entry.pack()

button=tk.Button(root,text="calculator",command=Calculator).pack()

label=tk.Label(root,text="Hello")
label.pack()

label_result=tk.Label(root)
label_result.pack()

root.mainloop()

