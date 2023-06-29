from tkinter import *
from PIL import ImageTk,Image
import os

def Next():
    os.system('User1.py')
def Med():
    os.system('User_Medicine.py')
    
main = Tk()
main.state('zoomed')
main.title("Welcome to Your Medical Reports")

background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)

frame1 = LabelFrame(main, bd=10,width=15,bg="light blue", padx=10,pady=5)
frame1.pack(expand=True)

label_0 = Label(frame1,bg="light blue",text="PATIENT",width=15,font="Corbel 25 bold underline",padx=5,pady=10)
label_0.pack()

frame = LabelFrame(main, bd=10, bg="light blue", width=00,padx=0,pady=0)
frame.pack(side="top",expand='yes')

Button(frame, text='Check Your Results', font='40', width=25,command=Next,bg='dark blue',fg='white').pack()

frame2 = LabelFrame(main, bd=10, bg="light blue", width=00,padx=0,pady=0)
frame2.pack(side="top",expand='yes')

Button(frame2, text='Order Medicines', font='40', width=25,command=Med,bg='dark blue',fg='white').pack()
                
main.mainloop()
        

         
