from tkinter import *
from tkinter import *
from PIL import ImageTk,Image
import os

def operator():
        os.system('pass.py')
        print("Hello")
        
def user():
        os.system('User.py')
        
main = Tk()
main.state('zoomed')
main.title("Welcome to Medical Reports")

background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)

frame1 = LabelFrame(main, bd=10,width=0,bg="light blue", padx=10,pady=5)
frame1.pack(expand=True)

label_0 = Label(frame1,bg="light blue",text="PLEASE SELECT THE DESIRED OPTION",width=30,font="Corbel 25 bold underline")
label_0.pack()

frame = LabelFrame(main, bd=10, bg="light blue", width=00,padx=0,pady=2)
frame.pack(expand='yes')

Button(frame, text='User', font='40', width=25,bg='dark blue',fg='white',command=user).pack()

main.quit()
        
frame2 = LabelFrame(main, bd=10 , bg="light blue",width=0,padx=0,pady=5)
frame2.pack(expand="yes")
                
Button(frame2, text='Operator', font='40', width=25,bg='darkblue',fg='white',command=operator).pack()

main.mainloop()
        


