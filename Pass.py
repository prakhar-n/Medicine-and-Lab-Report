from tkinter import messagebox
from tkinter import *
from PIL import ImageTk,Image
import os
def dialog1():
    username = user.get()
    password = passw.get()
    if (username == 'admin' and  password == 'password'):
        messagebox.showinfo('info','Correct Login')
        os.system('Pre_Operator.py')
    else:
        messagebox.showinfo('info','Invalid Login')
        
main = Tk()
main.state('zoomed')
main.title("Welcome to Medical Reports")

background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)

frame1 = LabelFrame(main, bd=10,width=0,bg="light blue", padx=10,pady=5)
frame1.pack(expand=True)

Label1 = Label(frame1,bg="white",text = 'Username:')
Label1.pack(padx=15,pady= 5)

user = StringVar()

entry1 = Entry(frame1,textvariable=user)
entry1.pack(padx=15, pady=5)

passw = StringVar()

Label2 = Label(frame1,bg="white",text = 'Password: ')
Label2.pack(padx = 15,pady=6)

entry2 = Entry(frame1,show='*',textvariable=passw)
entry2.pack(padx = 15,pady=7)

btn = Button(frame1, text = 'Check Login',command = dialog1)


btn.pack(side = RIGHT , padx =5)
frame1.pack(padx=100,pady = 19)
main.mainloop()

