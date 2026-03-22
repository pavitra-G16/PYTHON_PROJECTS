from tkinter import *
import os 

def restart():
    os.system("sudo ShutDown -r now")
def restart_time():
    os.system("sudo ShutDown /r /t 20")
def logout():
    os.system("""
              osascript -e 'tell application"System Events" to log out'
              """)
def shutdown():
    os.system("""osascript -e 'tell app "System Events" to restart'""")




st = Tk()


st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Red")

r_button = Button(st,text="Restart",font=("Time New Roman",20,"bold"),
                  relief=RAISED,cursor="plus",command=restart)
r_button.place(x=200,y=60,height=50,width=200)

rt_button = Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=restart_time)
rt_button.place(x=150,y=170,height=50,width=200)

lg_button = Button(st,text="Log-Out",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=logout)
lg_button.place(x=150,y=270,height=50,width=200)


st_button = Button(st,text="Shut-Down",font=("Time New Roman",20,"bold"),
                   relief=RAISED,cursor="plus",command=shutdown)
st_button.place(x=150,y=370,height=50,width=200)

st.mainloop()

