from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as ms
import os

mydb=ms.connect(host="localhost",user="root",password="tiger")
mycur=mydb.cursor()
mycur.execute("use custody")

f=open("test.txt","r")
s=f.read()
f.close()
    
qry='select * from PATtest where identity=' + str(s)
mycur.execute(qry)
data=mycur.fetchone()
id1 = data[0]
name = data[1]
dob = data[2]
add = data[3]
bg = data[4]
email = data[5]
covid= data[6]
ebola = data[7]
h1n1 = data[8]
sars = data[9]
mers = data[10]
infl= data[11]

main = Tk()
main.state('zoomed')
main.title("Welcome to Medical Reports")
background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)
        
frame1 = LabelFrame(main, bd=10,width=0,bg="light blue")
frame1.pack(side=TOP,expand=True,fill=X)

label = Label(frame1,bg="light blue",text="YOUR MEDICAL REPORT",width=35,font="Century 20 bold underline")
label.pack()

frame = LabelFrame(main, bd=5, width=50,bg="light blue")
frame.pack(side=LEFT,expand=True,fill=BOTH)

label_0 = Label(frame,text="PATIENT ID:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_0.pack()

label_0 = Label(frame, text=id1,width=20,font=("Century 18"),pady=2,padx=2)
label_0.pack(pady=2,padx=2)

label_1 = Label(frame, text="NAME:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_1.pack()

label_1a = Label(frame, text=name,width=20,font=("Century 18"),pady=2,padx=2)
label_1a.pack(pady=2,padx=2)


label_2 = Label(frame, text="AGE:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_2.pack()

label_2a = Label(frame, text=dob,width=20,font=("Century 18"),pady=2,padx=2)
label_2a.pack(pady=2,padx=2)

label_3 = Label(frame, text="ADDRESS:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_3.pack()

label_3a = Label(frame, text=add,width=20,font=("Century 18"),pady=2,padx=2)
label_3a.pack(pady=2,padx=2)

label_4 = Label(frame, text="BlOOD GROUP:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_4.pack()

label_4a = Label(frame, text=bg,width=20,font=("Century 18"),pady=2,padx=2)
label_4a.pack(pady=2,padx=2)

label_4_5 = Label(frame, text="EMAIL ID:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_4_5.pack()

label_4_5a = Label(frame, text=email,width=20,font=("Century 18"),pady=2,padx=2)
label_4_5a.pack(pady=2,padx=2)
           

label_5 = Label(frame, text="COVID-19",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_5.pack()
            
label_5a = Label(frame, text=covid,width=20,font=("Century 18"),pady=2,padx=2)
label_5a.pack(pady=2,padx=2)

frame3 = LabelFrame(main, bd=5, width=100,bg="light blue")
frame3.pack(side=RIGHT,expand=True,fill=BOTH)
            
label_6 = Label(frame3, text="EBOLA",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_6.pack()

label_6a = Label(frame3, text=ebola,width=20,font=("Century 18"),pady=2,padx=2)
label_6a.pack(pady=2,padx=2)

label_7 = Label(frame3, text="H1N1",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_7.pack()
        
label_7a = Label(frame3, text=h1n1,width=20,font=("Century 18"),pady=2,padx=2)
label_7a.pack(pady=2,padx=2)

label_8 = Label(frame3, text="SARS-COV",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_8.pack()

label_8a = Label(frame3, text=sars,width=20,font=("Century 18"),pady=2,padx=2)
label_8a.pack(pady=2,padx=2)

label_9 = Label(frame3, text="MERS-COV",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_9.pack()

label_9a = Label(frame3, text=mers,width=20,font=("Century 18"),pady=2,padx=2)
label_9a.pack(pady=2,padx=2)

label_10 = Label(frame3, text="INFLUENZA",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_10.pack()

label_10a = Label(frame3, text=infl,width=20,font=("Century 18"),pady=2,padx=2)
label_10a.pack()

main.mainloop()
