from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as ms
import os

mydb=ms.connect(host="localhost",user="root",password="tiger")
mycur=mydb.cursor()
mycur.execute("use custody")

f=open("medicine.txt","r")
s=f.read()
f.close()
    
qry='select * from medicine where orderid=' + str(s)
mycur.execute(qry)
data=mycur.fetchone()
orderid = data[0]
name = data[10]
Email = data[11]
Aug = data[1]
dolo = data[2]
disp = data[3]
ultra= data[4]
mel = data[5]
rifa = data[6]
amryl = data[7]
multi = data[8]
nebi= data[9]

main = Tk()
main.state('zoomed')
main.title("Welcome to Medicine Order")
background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)
        
frame1 = LabelFrame(main, bd=10,width=0,bg="light blue")
frame1.pack(side=TOP,expand=True,fill=X)

label = Label(frame1,bg="light blue",text="YOUR MEDICINE ORDER",width=35,font="Century 20 bold underline")
label.pack()

frame = LabelFrame(main, bd=5, width=50,bg="light blue")
frame.pack(side=LEFT,expand=True,fill=BOTH)

label_0 = Label(frame,text="PATIENT ID:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_0.pack()

label_0 = Label(frame, text=orderid,width=20,font=("Century 18"),pady=2,padx=2)
label_0.pack(pady=2,padx=2)

label_1 = Label(frame, text="NAME:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_1.pack()

label_1a = Label(frame, text=name,width=20,font=("Century 18"),pady=2,padx=2)
label_1a.pack(pady=2,padx=2)


label_2 = Label(frame, text="EMAIL ID:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_2.pack()

label_2a = Label(frame, text=Email,width=20,font=("Century 18"),pady=2,padx=2)
label_2a.pack(pady=2,padx=2)

label_3 = Label(frame, text="AUGMENTIN 625:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_3.pack()

label_3a = Label(frame, text=Aug+" Tablets",width=20,font=("Century 18"),pady=2,padx=2)
label_3a.pack(pady=2,padx=2)

label_4 = Label(frame, text="DOLO 650:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_4.pack()

label_4a = Label(frame, text=dolo+" Tablets",width=20,font=("Century 18"),pady=2,padx=2)
label_4a.pack(pady=2,padx=2)

label_4_5 = Label(frame, text="DISPERINE:",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_4_5.pack()

label_4_5a = Label(frame, text=disp+" Tablets",width=20,font=("Century 18"),pady=2,padx=2)
label_4_5a.pack(pady=2,padx=2)
           

label_5 = Label(frame, text="ULTRACET",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_5.pack()
            
label_5a = Label(frame, text=ultra+" Tablets",width=20,font=("Century 18"),pady=2,padx=2)
label_5a.pack(pady=2,padx=2)

frame3 = LabelFrame(main, bd=5, width=100,bg="light blue")
frame3.pack(side=RIGHT,expand=True,fill=BOTH)
            
label_6 = Label(frame3, text="MELATONIN",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_6.pack()

label_6a = Label(frame3, text=mel+" Tablets",width=20,font=("Century 18"),pady=2,padx=2)
label_6a.pack(pady=2,padx=2)

label_7 = Label(frame3, text="RIFAGUT",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_7.pack()
        
label_7a = Label(frame3, text=rifa+" Tablets",width=20,font=("Century 18"),pady=2,padx=2)
label_7a.pack(pady=2,padx=2)

label_8 = Label(frame3, text="AMRYL 250",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_8.pack()

label_8a = Label(frame3, text=amryl+" Tablets",width=20,font=("Century 18"),pady=2,padx=2)
label_8a.pack(pady=2,padx=2)

label_9 = Label(frame3, text="MultiVitamins",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_9.pack()

label_9a = Label(frame3, text=multi+" Tablets",width=20,font=("Century 18"),pady=2,padx=2)
label_9a.pack(pady=2,padx=2)

label_10 = Label(frame3, text="Nebistar",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_10.pack()

label_10a = Label(frame3, text=nebi+" Tablets",width=20,font=("Century 18"),pady=2,padx=2)
label_10a.pack()

main.mainloop()
