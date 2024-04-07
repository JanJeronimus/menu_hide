import tkinter as tk
from tkinter import messagebox

label1        = "Do Secret option"
label1_hidden = "Doit_hidden"
label1_x      = label1_hidden+"_x"                # temporary for toggle function

def toggle_item():
    try:
        file_menu.entryconfig(label1,        label=label1_x)
    except tk.TclError:
        file_menu.entryconfig(label1_hidden, label=label1)
        file_menu.entryconfig(label1, state="normal")
    try:
        file_menu.entryconfig(label1_x,      label=label1_hidden)
        file_menu.entryconfig(label1_hidden, state="disabled")
    except tk.TclError:
        pass

def show_item():
    try:
        file_menu.entryconfig(label1_hidden, label=label1)
        file_menu.entryconfig(label1, state="normal")
    except tk.TclError:
        pass

def hide_item():
    try:
        file_menu.entryconfig(label1, label=label1_hidden)
        file_menu.entryconfig(label1_hidden, state="disabled")
    except tk.TclError:
        pass

def hidden_function():
    message = "Executing Menu item " + label1
    messagebox.showinfo("Message", message)

def exit_program():
    root.destroy()

root = tk.Tk()
root.geometry('720x480')

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar, tearoff=False)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label=label1_hidden, command=hidden_function,state='disabled')  # Default not show
file_menu.add_command(label="Exit", command=exit_program)

toggle_button = tk.Button(root, text="Toggle Item", command=toggle_item, padx=20, pady=20, width=15)
toggle_button.pack(padx=20,pady=20)

show_button = tk.Button(root, text="Show", command=show_item, padx=20, pady=20, width=15)
show_button.pack(padx=20,pady=20)

hide_button = tk.Button(root, text="Hide", command=hide_item, padx=20, pady=20, width=15)
hide_button.pack(padx=20,pady=20)

root.mainloop()
