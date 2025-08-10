__version__ = "0.2.0"

from tkinter import *
from tkinter.ttk import *
import math  
from counter import Counter

BGCOLOR = "#222831"
CANVACOLOR = "#393E46"
TEXTCOLOR="#00ADB5"
BTNCOLOR = "#EEEEEE"
TOASTCOLOR = "#333333"
YT = "white"
d_font = ("Arial",15,"bold")
window = Tk()
window.geometry("390x340")
window.resizable(False,False)
window.title(f"Break Tracker – {__version__}")
window["bg"] = BGCOLOR
window["padx"] = 5
for i in range(3):
    window.columnconfigure(i, weight=1)


c = Counter()

style = Style()
style.theme_use('default')
style.configure("Timer.TButton",foreground=YT,background="#0D5EA6",font=d_font)
style.configure("SettingsB.TButton",foreground=YT,background="#FF4F0F",font=d_font)
style.configure("Settings.TButton",foreground="#FF7A30",background=YT,font=d_font)
style.configure("Settings.TLabel",foreground=YT,background="#FF7A30",font=d_font,padding=(10,5))
style.configure("Window.TLabel",foreground=YT,background=BGCOLOR,font=("Arial",20,"bold"))
style.configure("Header.TLabel",foreground=TEXTCOLOR,background=BGCOLOR,font=("Courier",35,"bold"))
style.configure("Toast.TLabel",foreground=YT,background=TOASTCOLOR,padding=(10, 5),font=("Segoe UI", 35, "bold"))
    
def toggle_timer():
    if c.is_break == False:
        canva.configure(bg="#D65A31")
        start_btn.config(text="Stop")
        c.is_break = True
        counter()
        show_toast(msg="Break started!")
    elif c.is_break == True:
        canva.configure(bg=CANVACOLOR)
        start_btn.config(text="Start")
        c.total_time += c.count
        c.count = 0
        c.is_break = False
        formatted_break = c.time_format(c.total_time)
        total_time_label["text"] = f"Total break: {formatted_break}"
        c.save_file()
        show_toast(msg="Break ended!")

def counter():
    formatted_time = c.time_format(c.count)
    canva.itemconfig(time_counter, text=formatted_time)
    c.count += 0.01
    if c.is_break:
        window.after(10,counter)



def reset_timer():
    c.total_time = 0
    formatted_break = c.time_format(c.total_time)
    total_time_label["text"] = f"Total break: {formatted_break}"
    with open("data.txt", "w") as file:
            file.write(str(c.total_time))
    show_toast()

def open_settings():
    if hasattr(window,"settings_open") and window.settings_open == True:
        return
    window.settings_open = True
    
    settings = Toplevel(window,bg=CANVACOLOR)
    settings.title("Settings")
    settings.minsize(360,300)
    settings.columnconfigure(0, weight=1)
    settings.columnconfigure(1, weight=1)

    reset_label = Label(settings,text="Reset the timer!",style="Settings.TLabel")
    reset_btn = Button(settings,text="Reset",command=reset_timer, style="Settings.TButton")
    format_label = Label(settings,text="Change the format!",style="Settings.TLabel")
    format_btn = Button(settings,text="Format",command=change_time_format, style="Settings.TButton")
    reset_label.grid(row=0,column=0,pady=10,sticky="")
    reset_btn.grid(row=0,column=1,pady=10,sticky="")
    format_label.grid(row=1,column=0,pady=10,sticky="")
    format_btn.grid(row=1,column=1,pady=10,sticky="")
    
    
    settings.protocol("WM_DELETE_WINDOW",lambda: on_close(settings))
    settings.grab_set()

def change_time_format():
    c.change_format()
    total_time_label["text"] = f"Total break: {c.time_format(c.total_time)}"
    canva.itemconfig(time_counter, text=c.time_format(c.count))
    

def on_close(settings_window):
    window.settings_open = False
    settings_window.destroy()

def show_toast(msg="Break time reset!", duration=1500):
    toast = Toplevel(window)
    toast.overrideredirect(True)
    toast.attributes("-topmost", True)
    toast.configure(bg="#333333")
    
    label = Label(toast, text=msg, style="Toast.TLabel")
    label.pack()

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    toast.update_idletasks()
    x = screen_width - toast.winfo_width() - 20
    y = screen_height - toast.winfo_height() - 60
    toast.geometry(f"+{x}+{y}")
    
    toast.after(duration, toast.destroy)

header_label = Label(text="Break Counter",style="Header.TLabel")
canva = Canvas(width=360,height=200,bg=CANVACOLOR,borderwidth=0, )
time_counter = canva.create_text(180,100,text="00:00:00",fill="white", font=("Arial",35,"bold"))
start_btn = Button(text="Start",command=toggle_timer,style="Timer.TButton")
settings_btn = Button(text="Settings",command=open_settings,style="SettingsB.TButton")
formatted_break = c.time_format(c.total_time)
total_time_label = Label(text=f"Total break: {formatted_break}",style="Window.TLabel")


header_label.grid(column=0,row=0,columnspan=3,sticky="n")
canva.grid(column=0,row=1,columnspan=3)
total_time_label.grid(column=0,row=2,columnspan=3)
start_btn.grid(column=0,row=3,pady=3)
settings_btn.grid(column=2,row=3,pady=3)



window.mainloop()
