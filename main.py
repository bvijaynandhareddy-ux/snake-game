from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def update_time():
    current_time = strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

clock_label = Label(
    root,
    font=("Arial", 50),
    bg="black",
    fg="cyan"
)

clock_label.pack()

update_time()

root.mainloop()