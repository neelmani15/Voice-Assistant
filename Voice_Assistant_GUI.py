from tkinter import *
from PIL import ImageTk,Image
# Create an instance of Tkinter frame
root = Tk()
# Add a title to tkinter
root.title('Siri Voice Assistant')
# Set a geometry of tkinter frame
root.geometry("1200x600+10+20")
# Load an image in tkinter
img=Image.open("mic.png")
# To addcolor
#root.config(bg="#4fee8d")
# Resize the image
r_img=img.resize((60,150),Image.ANTIALIAS)
m_img=ImageTk.PhotoImage(r_img)
label=Label(root,image=m_img,text='Hello Buddy')
label.pack()
root.mainloop()
