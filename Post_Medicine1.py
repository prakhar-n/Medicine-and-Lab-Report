from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os
import mysql.connector as ms

mydb=ms.connect(host="localhost",user="root",password="tiger")
mycur=mydb.cursor()
mycur.execute("use custody")

def Doc():
        q=var1.get()
        qry='select * from medicine where orderid=' + str(q)
        mycur.execute(qry)
        data=mycur.fetchone()
        if data==None:
            messagebox.showinfo('info','Invalid ID. Please try again')
        else:
            a=open("medicine.txt","w")
            a.write(q)
            print("done")
            a.close()
            os.system('Post_Medicine2.py')

main = Tk()
main.state('zoomed')
main.title("Welcome to Medical Reports")

background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)

frame1 = LabelFrame(main, bd=10,width=0,bg="light blue", padx=10,pady=5)
frame1.pack(expand=True)

label_0 = Label(frame1,bg="light blue",text="PLEASE ENTER THE ORDER ID",width=35,font="Corbel 20 bold underline")
label_0.pack()

frame2 = LabelFrame(main, bd=5, bg="light blue", width=00,padx=0,pady=2)
frame2.pack(expand=True)

label_1 = Label(frame2, text="ID:",bg="white",width=15,font=("Georgia 20 underline"))
label_1.pack()

var1 = StringVar()
        
entry_1 = Entry(frame2,bg="white",textvariable=var1,width=40)
entry_1.pack()

frame = LabelFrame(main, bd=10, bg="light blue", width=00,padx=0,pady=2)
frame.pack(expand='yes')

Button(frame, text='Submit', font='20', width=15,bg='dark blue',fg='white',command=Doc).pack()
main.mainloop()

   
