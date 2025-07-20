__version__ = "0.1.2"

from tkinter import *
import math  
from counter import Counter

BGCOLOR = "#222831"
CANVACOLOR = "#393E46"
TEXTCOLOR="#00ADB5"
BTNCOLOR = "#EEEEEE"
window = Tk()
window.minsize(360,300)
window.title(f"Break Tracker – {__version__}")
window["bg"] = BGCOLOR
window["padx"] = 5

c = Counter()
    
def toggle_timer():
    if c.is_break == False:
        canva.configure(bg="#D65A31")
        start_btn.config(text="Stop")
        c.is_break = True
        counter()
    elif c.is_break == True:
        canva.configure(bg=CANVACOLOR)
        start_btn.config(text="Start")
        c.total_time += c.count
        c.count = 0
        c.is_break = False
        formatted_break = c.time_format(c.total_time)
        total_time_label["text"] = f"Total break: {formatted_break}"
        c.save_file()

def counter():
    formatted_time = c.time_format(c.count)
    canva.itemconfig(time_counter, text=formatted_time)
    c.count += 0.001
    if c.is_break:
        window.after(1,counter)



def reset_timer():
    c.total_time = 0
    formatted_break = c.time_format(c.total_time)
    total_time_label["text"] = f"Total break: {formatted_break}"
    with open("data.txt", "w") as file:
            file.write(str(c.total_time))
    

header_label = Label(text="Break Counter",fg=TEXTCOLOR,font=("Courier",30,"bold"),bg=BGCOLOR)
canva = Canvas(width=360,height=200,bg=CANVACOLOR,borderwidth=0, )
time_counter = canva.create_text(180,100,text="00:00",fill="white", font=("Arial",35,"bold"))
start_btn = Button(text="Start",fg="blue",font=("Arial",15,"bold"),command=toggle_timer, padx=5, pady=5)
reset_btn = Button(text="Reset",fg="red",font=("Arial",15,"bold"),command=reset_timer, padx=5, pady=5)
formatted_break = c.time_format(c.total_time)
total_time_label = Label(text=f"Total break: {formatted_break}",font=("Arial",20,"bold"), fg="white",bg=BGCOLOR)


header_label.grid(column=1,row=0,columnspan=2)
canva.grid(column=1,row=1,columnspan=2)
total_time_label.grid(column=1,row=2,columnspan=2)
start_btn.grid(column=1,row=3,pady=3)
reset_btn.grid(column=2,row=3,pady=3)


window.mainloop()
