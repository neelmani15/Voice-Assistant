from tkinter import *
import os
import threading
from PIL import ImageTk,Image
#from main import *
# Create an instance of Tkinter frame
root = Tk()
# Add a title to tkinter
root.title('Siri Voice Assistant')
# Set a geometry of tkinter frame
root.geometry("1000x600+10+20")
# Load an image in tkinter
frame1=Frame(root,bg='#9AFEFF',height=250)
frame1.pack(fill=X)
frame2=Frame(root,bg='#806517',height=350)
frame2.pack(fill=X)
img=Image.open("Important\\micimage.jpg")
# To addcolor
#root.config(bg="#4fee8d")
# Resize the image
r_img=img.resize((100,100),Image.ANTIALIAS)
m_img=ImageTk.PhotoImage(r_img)
label2 = Label(frame1,text="SIRI Voice Assistant",font="bold,50")
label2.place(x=420,y=150)
label1=Label(frame2,image=m_img,text='Hello Buddy')
label1.place(x=450,y=20)
def run():
    os.system('main.py')
def thread_run():
    threading.Thread(target=run).start()
def exit():
    exit()
button1=Button(frame2,text="Search",width="15",pady=10,font="bold, 15",command=thread_run,bg="green")
button1.place(x=220,y=180)
button2=Button(frame2,text="Quit",width="15",pady=10,font="bold, 15",command=root.destroy,bg="green")
button2.place(x=600,y=180)
root.mainloop()
