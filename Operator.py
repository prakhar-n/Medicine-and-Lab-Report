from tkinter import *
from PIL import ImageTk,Image
import os

def OP1():
    os.system('Operator1.py')

def OP2():
    os.system('Operator2_2.py')

def OP3():
    os.system('User1.py')

def OP4():
    os.system('Operator2.py')
        
def OP5():
    os.system('Delete.py')

main = Tk()
main.state('zoomed')
main.title("Welcome to Medical Reports")

background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)

frame1 = LabelFrame(main, bd=10,width=0,bg="light blue", padx=10,pady=5)
frame1.pack(expand=True)

label_0 = Label(frame1,bg="light blue",text="OPERATOR",width=30,font="Corbel 25 bold underline")
label_0.pack()

frame = LabelFrame(main, bd=5, bg="light blue", width=00,padx=0,pady=2)
frame.pack(expand='yes')

Button(frame, text='Enter Records', font='40', width=25,command=OP1,bg='dark blue',fg='white').pack()

frame2 = LabelFrame(main, bd=5 , bg="light blue",width=0,padx=0,pady=2)
frame2.pack(expand="yes")
                
Button(frame2, text='View Records', font='40', width=25,command=OP2,bg='darkblue',fg='white').pack()

frame3 = LabelFrame(main, bd=5, bg="light blue", width=00,padx=0,pady=2)
frame3.pack(expand='yes')

Button(frame3, text='Check Records', font='40', width=25,command=OP3,bg='dark blue',fg='white').pack()

frame4 = LabelFrame(main, bd=5, bg="light blue", width=00,padx=0,pady=2)
frame4.pack(expand='yes')

Button(frame4, text='Update Records', font='40', width=25,command=OP4,bg='dark blue',fg='white').pack()

frame5 = LabelFrame(main, bd=5, bg="light blue", width=00,padx=0,pady=2)
frame5.pack(expand='yes')

Button(frame5, text='Delete Records', font='40', width=25,command=OP5,bg='dark blue',fg='white').pack()

main.mainloop()
        


