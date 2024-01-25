from tkinter import *
import os

def restart():
    os.system("ShutDown /r /t /1")

def restart_time():
    os.system("ShutDown /r /t 20")

def logout():
    os.system("ShutDown -l")

def shutdown():
    os.system("ShutDown /s /t 1")



st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="pink")

r_button = Button(st, text="Restart", font=("Time New Roman",
                  20, "bold"), relief=SUNKEN, cursor="arrow", command=restart)
r_button.place(x=150, y=60, height=50, width=200)

rt_button = Button(st, text="Restart Time", font=(
    "Time New Roman", 20, "bold"), relief=RAISED, cursor="arrow", command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)

lg_button = Button(st, text="Log-out", font=("Time New Roman",
                   20, "bold"), relief=SUNKEN, cursor="arrow", command=logout)
lg_button.place(x=150, y=270, height=50, width=200)

st_button = Button(st, text="Shutdown", font=(
    "Time New Roman", 20, "bold"), relief=RAISED, cursor="arrow", command=shutdown)
st_button.place(x=150, y=370, height=50, width=200)



st.mainloop()
