import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.configure(bg="#191970")
root.attributes("-fullscreen", True)  # Start Fullscreen

is_running = False 
number = 0
number_minute = 0
number_hour = 0
control = 0
fullscreen = True
options_color = ["White", "Red", "Blue", "Green", "Black"] # Color Options

def stop_counter():
    global is_running
    is_running = False

def count_numbers():
    global number, is_running
    if not is_running:
        return
    number += 1
    if number >= 60:  
        number = 0
        Number_minute()
    label_number.config(text=str(number))
    root.after(1000, count_numbers)

def Number_minute():
    global number_minute
    number_minute += 1
    if number_minute >= 60:
        number_minute = 0
        Number_hour()
    label_minute.config(text=str(number_minute))

def Number_hour():
    global number_hour
    number_hour += 1
    label_hour.config(text=str(number_hour))
        
def collection():
    start_counter()

def start_counter():
    global is_running
    if not is_running:  
        is_running = True
        count_numbers()

def keyboard_variable(event):
    global control
    if control % 2 == 0:
        button.invoke()
    else:
        stop_button.invoke()
    control += 1

def reset():
    global number_hour, number_minute, number
    number = 0
    number_minute = 0
    number_hour = 0
    label_hour.config(text=str(number_hour))
    label_minute.config(text=str(number_minute))
    label_number.config(text=str(number))

def reset_keyboard(event):
    reset_button.invoke()

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes("-fullscreen", fullscreen)

def optionsF():
    colors = {
        "White": "White",
        "Red": "Red",
        "Blue": "Blue",
        "Green": "Green",
        "Black": "Black"
    }
    background = colors.get(combo.get(), "White")
    text_color = "Gray" if background == "Black" else "White"
    
    root.configure(bg=background)
    for widget in [label_hour, label_minute, label_number, label_version]:
        widget.config(bg=background, fg=text_color)
    for widget in [stop_button, reset_button]:
        widget.config(bg="Gray")

root.bind("<Escape>", toggle_fullscreen)
root.bind("<space>", keyboard_variable)
root.bind("<Return>", reset_keyboard)

combo = ttk.Combobox(root, values=options_color, state="readonly")
combo.set("White")
combo.bind("<<ComboboxSelected>>", lambda e: optionsF())

button = tk.Button(root, text="Başla", command=collection, bg="Gray")
label_hour = tk.Label(root, text=str(number_hour), bg="#191970", fg="White")
label_minute = tk.Label(root, text=str(number_minute), bg="#191970", fg="White")
label_number = tk.Label(root, text=str(number), bg="#191970", fg="White")
stop_button = tk.Button(root, text="Durdur", command=stop_counter, bg="Gray")
reset_button = tk.Button(root, text="Sıfırla", bg="Gray", command=reset)
label_version = tk.Label(root, text="v1.0.1-alpha-beta", bg="#191970", fg="White")

def resize_widgets(event):
    combo.place(relx=0.45, rely=0.1, relwidth=0.1, relheight=0.05)
    button.place(relx=0.45, rely=0.3, relwidth=0.1, relheight=0.05)
    label_hour.place(relx=0.42, rely=0.2, relwidth=0.05, relheight=0.05)
    label_minute.place(relx=0.47, rely=0.2, relwidth=0.05, relheight=0.05)
    label_number.place(relx=0.52, rely=0.2, relwidth=0.05, relheight=0.05)
    stop_button.place(relx=0.45, rely=0.4, relwidth=0.1, relheight=0.05)
    reset_button.place(relx=0.45, rely=0.5, relwidth=0.1, relheight=0.05)
    label_version.place(relx=0.8, rely=0.9, relwidth=0.15, relheight=0.05)

root.bind("<Configure>", resize_widgets)
root.mainloop()
