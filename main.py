from tkinter import *
import math  

BGCOLOR = "#222831"
CANVACOLOR = "#393E46"
TEXTCOLOR="#00ADB5"
BTNCOLOR = "#EEEEEE"
count = 0
total_time = 0
break_on = False
window = Tk()
window.minsize(450,290)
window.title("Break Counter")
window["bg"] = BGCOLOR
window["padx"] = 5

with open("data.txt","r") as file:
    content = int(file.read())
    total_time = content
    
def toggle_timer():
    global break_on
    global total_time
    global count
    if break_on == False:
        canva.configure(bg="#D65A31")
        start_btn.config(text="Stop")
        break_on = True
        counter()
    elif break_on == True:
        canva.configure(bg=CANVACOLOR)
        start_btn.config(text="Start")
        total_time += count
        count = 0
        break_on = False
        formatted_break = time_format(total_time)
        total_time_label["text"] = f"Total break: {formatted_break}"
        with open("data.txt", "w") as file:
            file.write(str(math.floor(total_time)))
        
        

def counter():
    global count
    formatted_time = time_format(count)
    canva.itemconfig(time_counter, text=formatted_time)
    count += 0.1
    if break_on:
        window.after(100,counter)

def time_format(n):
    mins = math.floor(n / 60)
    secs = math.floor(n % 60)
    millis = int((n - int(n)) * 100)  # get the hundredths part

    return f"{mins:02d}:{secs:02d}:{millis:02d}"

def reset_timer():
    global total_time
    total_time = 0
    formatted_break = time_format(total_time)
    total_time_label["text"] = f"Total break: {formatted_break}"
    with open("data.txt", "w") as file:
            file.write(str(total_time))
    

canva = Canvas(width=300,height=200,bg=CANVACOLOR,borderwidth=0, )
time_counter = canva.create_text(150,100,text="00:00",fill="white", font=("Arial",35,"bold"))

header_label = Label(text="Break Counter",fg=TEXTCOLOR,font=("Courier",30,"bold"),bg=BGCOLOR)
start_btn = Button(text="Start",fg="blue",font=("Arial",15,"bold"),command=toggle_timer, padx=5, pady=5)
reset_btn = Button(text="Reset",fg="red",font=("Arial",15,"bold"),command=reset_timer, padx=5, pady=5)
formatted_break = time_format(total_time)
total_time_label = Label(text=f"Total break: {formatted_break}",font=("Arial",20,"bold"), fg="white",bg=BGCOLOR)


header_label.grid(column=1,row=0)
canva.grid(column=1,row=1)
start_btn.grid(column=0,row=2,pady=3)
reset_btn.grid(column=2,row=2,pady=3)
total_time_label.grid(column=1,row=2)

window.mainloop()
