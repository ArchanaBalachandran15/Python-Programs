import tkinter as tk

def show_message():
    name=entry.get()
    label_result.config(text=f"hello,{name}!...")

root=tk.Tk()
root.title("My First Tkinter Prog")
root.geometry("600x200")

label=tk.Label(root,text="Hello")
label.pack()

entry=tk.Entry(root)
entry.pack()

button=tk.Button(root,text="Greet",command=show_message)
button.pack()

label_result=tk.Label(root)
label_result.pack()

root.mainloop()

