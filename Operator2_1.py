from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as ms
import os
import smtplib

mydb=ms.connect(host="localhost",user="root",password="tiger")
mycur=mydb.cursor()
mycur.execute("use custody")

def SaveIt():
        f=open("test2.txt","r")
        s=f.read()
        f.close()
        qo='"'
        name_info = name.get()
        if len(name_info)>1:
            p="update pattest set name=" + qo + name_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()
            
        dob_info = dob.get()
        if len(dob_info)>1:
            p="update pattest set dob=" + qo + dob_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        add_info = add.get()
        if len(add_info)>1:
            p="update pattest set address=" + qo + add_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        bg_info = bg.get()
        if len(bg_info)>1:
            p="update pattest set bloodgroup=" + qo + bg_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        email_info = email.get()
        if len(email_info)>1:
            p="update pattest set EmailID=" + qo + email_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        covid_info = var.get()
        if len(covid_info)>2:
            p="update pattest set covid19=" + qo + covid_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        ebola_info = var1.get()
        if len(ebola_info)>2:
            p="update pattest set ebola=" + qo + ebola_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        h1n1_info = var2.get()
        if len(h1n1_info)>2:
            p="update pattest set h1n1=" + qo + h1n1_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        sars_info = var3.get()
        if len(sars_info)>2:
            p="update pattest set sarscov=" + qo + sars_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        mers_info = var4.get()
        if len(mers_info)>2:
            p="update pattest set merscov=" + qo + mers_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        infl_info = var5.get()
        if len(infl_info)>2:
            p="update pattest set influenza=" + qo + infl_info + qo
            q=" where identity="+ qo + s + qo
            qry=str(p)+str(q)
            mycur.execute(qry)
            mydb.commit()

        qry='select * from PATtest where identity=' + str(s)
        mycur.execute(qry)
        data=mycur.fetchone()
        idd=data[0]
        namee=data[1]
        email_info2=data[5]
        
        prompt_msg = "YOUR TEST RESULTS HAS BEEN UPDATED Mr./Ms. " + str(namee)+".\n YOUR PATIENT ID IS:\t " + str(idd) + "\n IF ANY FURTHER UPDATION WILL TAKE PLACE, YOU WILL RECIEVE AN E-MAIL FOR THE SAME.\n FOR FURTHER ASSISTANCE CONTACT: +91-98XXXXXXXX"
        user = 'stayhealthyhospital@gmail.com'
        password = 'fgjiwjvyzeqeksuj'
        
        reciever = email_info2

        subject = "MEDICAL TEST RESULTS"
        message = "Subject: {} \n\n{}".format(subject, prompt_msg)
        send_to = ("{}".format(reciever))

        mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        mail.ehlo()
        mail.login(user, password)
        mail.sendmail(user, send_to, message)
        messagebox.showinfo('info','Record has been updated.\n A new E-mail has been sent')

        

main = Tk()
main.state('zoomed')
main.title("Welcome to Medical Reports")

background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)

frame1 = LabelFrame(main, bd=10,width=0,bg="light blue")
frame1.pack(side=TOP,expand=True,fill=X)

label = Label(frame1,bg="light blue",text="PLEASE ENTER THE UPDATED DETAILS",width=35,font="Corbel 20 bold underline")
label.pack()

frame = LabelFrame(main, bd=5, width=50)
frame.pack(side=LEFT,expand=True,fill=BOTH)


label_1 = Label(frame, text="NAME:",width=20,font=("Georgia 20 underline"))
label_1.pack()

name = StringVar()
        
entry_1 = Entry(frame,textvariable=name)
entry_1.pack(pady=2,padx=2)


label_2 = Label(frame, text="DATE OF BIRTH:",width=20,font=("Georgia 20 underline"))
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

bg = StringVar()

entry_4 = Entry(frame,textvariable=bg)
entry_4.pack(pady=10,padx=10)

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

