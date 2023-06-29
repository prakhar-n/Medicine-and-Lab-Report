from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as ms
import os
import smtplib
import random

mydb=ms.connect(host="localhost",user="root",password="tiger")
mycur=mydb.cursor()
mycur.execute("use custody")

def SaveIt():
    i=0
    while (i!=1):
        id1_info = random.randint(100000,999999)
        qry='select * from PATtest where identity=' + str(id1_info)
        mycur.execute(qry)
        data=mycur.fetchone()
        if data==None:
            i=1
            
    name_info = name.get()
    try:
        dob_info = int(dob.get())
        if dob_info<1 or dob_info>120:
            raise Exception(messagebox.showinfo('info','Please Enter Correct Age'))
    except ValueError:
         messagebox.showinfo('info','Please Enter Correct Age')

    add_info = add.get()
    bg_info = clicked.get()
    email_info = email.get()
    covid_info= var.get()
    ebola_info = var1.get()
    h1n1_info = var2.get()
    sars_info = var3.get()
    mers_info = var4.get()
    infl_info = var5.get()
    

    qry=("insert into PATtest values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')").format(id1_info,name_info,dob_info,add_info,bg_info,email_info,covid_info,ebola_info,h1n1_info,sars_info,mers_info,infl_info)
    mycur.execute(qry)
    mydb.commit()

    prompt_msg = "YOUR TEST RESULTS HAS BEEN UPLOADED Mr./Ms."+ str(name_info) +".\n YOUR PATIENT ID IS:\t " + str(id1_info) + "\n IF ANY UPDATION WILL TAKE PLACE, YOU WILL RECIEVE AN E-MAIL FOR THE SAME.\n FOR FURTHER ASSISTANCE CONTACT: +91-98XXXXXXXX"
    user = 'stayhealthyhospital@gmail.com'
    password = 'fgjiwjvyzeqeksuj'

    reciever = email_info

    subject = "MEDICAL TEST RESULTS"
    message = "Subject: {} \n\n{}".format(subject, prompt_msg)
    send_to = ("{}".format(reciever))

    mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail.ehlo()
    mail.login(user, password)
    mail.sendmail(user, send_to, message)
    messagebox.showinfo('info','Record has been added.\n E-mail has been sent')



main = Tk()
main.state('zoomed')
main.title("Welcome to Medical Reports")

background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)

frame1 = LabelFrame(main, bd=10,width=0,bg="light blue")
frame1.pack(side=TOP,expand=True,fill=X)

label = Label(frame1,bg="light blue",text="PLEASE ENTER THE PATIENT DETAILS",width=35,font="Corbel 20 bold underline")
label.pack()

frame = LabelFrame(main, bd=5, width=50)
frame.pack(side=LEFT,expand=True,fill=BOTH)

label_1 = Label(frame, text="NAME:",width=20,font=("Georgia 20 underline"))
label_1.pack()

name = StringVar()
        
entry_1 = Entry(frame,textvariable=name)
entry_1.pack(pady=2,padx=2)


label_2 = Label(frame, text="AGE:",width=20,font=("Georgia 20 underline"))
label_2.pack()

dob = StringVar()
        
entry_2 = Entry(frame,textvariable=dob)
entry_2.pack(pady=2,padx=2)

label_3 = Label(frame, text="ADDRESS:",width=20,font=("Georgia 20 underline"))
label_3.pack()

add = StringVar()
        
entry_3 = Entry(frame,textvariable=add)
entry_3.pack(pady=10,padx=10)

label_4 = Label(frame, text="BlOOD GROUP:",width=20,font=("Georgia 20 underline"))
label_4.pack()

options = [
    "None",
    "A+",
    "A-",
    "B+",
    "B-",
    "O+",
    "O-",
    "AB+",
    "AB-"
]
  
clicked = StringVar()
  
clicked.set( "None" )
  
drop = OptionMenu( frame , clicked , *options )
drop.pack(pady=10,padx=10)



label_4_5 = Label(frame, text="EMAIL ID:",width=20,font=("Georgia 20 underline"))
label_4_5.pack()

email = StringVar()

entry_4_5 = Entry(frame,textvariable=email)
entry_4_5.pack(pady=10,padx=10)
        

label_5 = Label(frame, text="COVID-19",width=20,font=("Georgia 20 underline"))
label_5.pack()
        
var=StringVar()

Radiobutton(frame, text="Positive", variable=var, value="Positive",tristatevalue="x").pack()       
Radiobutton(frame, text="Negative", variable=var, value="Negative",tristatevalue="x").pack()

frame3 = LabelFrame(main, bd=5, width=100)
frame3.pack(side=RIGHT,expand=True,fill=BOTH)
        
label_6 = Label(frame3, text="EBOLA",width=20,font=("Georgia 20 underline"))
label_6.pack()

var1 = StringVar()

Radiobutton(frame3, text="Positive", variable=var1, value="Positive",tristatevalue="x").pack()       
Radiobutton(frame3, text="Negative", variable=var1, value="Negative",tristatevalue="x").pack()

label_7 = Label(frame3, text="H1N1",width=20,font=("Georgia 20 underline"))
label_7.pack()

var2 = StringVar()

Radiobutton(frame3, text="Positive", variable=var2, value="Positive",tristatevalue="x").pack()       
Radiobutton(frame3, text="Negative", variable=var2, value="Negative",tristatevalue="x").pack()

label_8 = Label(frame3, text="SARS-COV",width=20,font=("Georgia 20 underline"))
label_8.pack()

var3 = StringVar()

Radiobutton(frame3, text="Positive", variable=var3, value="Positive",tristatevalue="x").pack()       
Radiobutton(frame3, text="Negative", variable=var3, value="Negative",tristatevalue="x").pack()

label_9 = Label(frame3, text="MERS-COV",width=20,font=("Georgia 20 underline"))
label_9.pack()

var4 = StringVar()

Radiobutton(frame3, text="Positive", variable=var4, value="Positive",tristatevalue="x").pack()       
Radiobutton(frame3, text="Negative", variable=var4, value="Negative",tristatevalue="x").pack()

label_10 = Label(frame3, text="INFLUENZA",width=20,font=("Georgia 20 underline"))
label_10.pack()

var5 = StringVar()

Radiobutton(frame3, text="Positive", variable=var5, value="Positive",tristatevalue="x").pack()       
Radiobutton(frame3, text="Negative", variable=var5, value="Negative",tristatevalue="x").pack()

        
frame2 = LabelFrame(main, bd=10, bg="light blue", width=0)
frame2.pack(side=BOTTOM,expand=True,fill=X)

Button(frame2, text='Submit', font='20', width=15,bg='dark blue',fg='white',command=SaveIt).pack()
main.mainloop()

