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

def Punchin():
    i=0
    while (i!=1):
        order_info = random.randint(100000,999999)
        qry='select * from PATtest where identity=' + str(order_info)
        mycur.execute(qry)
        data=mycur.fetchone()
        if data==None:
            i=1
    name_info = name.get()
    email_info=email.get()
    aug_info = clicked_aug.get()
    dolo_info = clicked_dolo.get()
    disp_info = clicked_disp.get()
    ultra_info = clicked_ultra.get()
    mel_info = clicked_mel.get()
    rifa_info = clicked_rifa.get()
    amryl_info = clicked_amryl.get()
    vitam_info = clicked_vitam.get()
    nebi_info = clicked_nebi.get()

    qry=("insert into medicine values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')").format(order_info,aug_info,dolo_info,disp_info,ultra_info,mel_info,rifa_info,amryl_info,vitam_info,nebi_info,name_info,email_info)
    mycur.execute(qry)
    mydb.commit()

    prompt_msg = "YOUR ORDER HAS BEEN PLACED Mr./Ms."+ str(name_info) +".\n YOUR ORDER ID IS:\t " + str(order_info) +"\n YOUR ORDER DETAILS ARE:"+"\n \n DESCRIPTION \t \t QUANTITY" + "\n \n"+"Augmentin 625  \t \t \t"+str(aug_info)+"\nDolo 650     \t  \t\t\t"+str(dolo_info)+"\nDisperine \t  \t\t\t"+str(disp_info)+"\nUltracet   \t  \t \t   \t"+str(ultra_info)+"\nMelatonin \t  \t \t\t"+str(mel_info)+"\nAmryl 250 \t\t \t\t"+str(amryl_info)+"\nMultiVitamins \t \t  \t  \t"+str(vitam_info)+"\nNebistar     \t  \t \t  \t"+str(nebi_info)+"\n \n PLEASE GO THE PHARMACY AND SHOW THIS ORDER ID FOR GOODS AND PAYMENT.\n FOR FURTHER ASSISTANCE CONTACT: +91-98XXXXXXXX"
    user = 'stayhealthyhospital@gmail.com'
    password = 'fgjiwjvyzeqeksuj'

    reciever = email_info

    subject = "MEDICINE ORDER INFO"
    message = "Subject: {} \n\n{}".format(subject, prompt_msg)
    send_to = ("{}".format(reciever))

    mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    mail.ehlo()
    mail.login(user, password)
    mail.sendmail(user, send_to, message)
    messagebox.showinfo('info','Order has been placed.\n E-mail has been sent')


    
main = Tk()
main.state('zoomed')
main.title("Welcome to Medicine Order")
background_image=ImageTk.PhotoImage(Image.open("C:\\Users\\nigam\\Desktop\\NTCC Project\\hEX2.jpg"))
background_label = Label(main, image=background_image)
background_label.place(x=0, y=0)
        
frame1 = LabelFrame(main, bd=10,width=0,bg="light blue")
frame1.pack(side=TOP,expand=True,fill=X)

label = Label(frame1,bg="light blue",text="MEDICINE ORDERING",width=35,font="Century 20 bold underline")
label.pack()

frame = LabelFrame(main, bd=5, width=50,bg="light blue")
frame.pack(side=LEFT,expand=True,fill=BOTH)

label_1 = Label(frame, bg="light blue",text="NAME:",width=20,font=("Georgia 20 underline"))
label_1.pack()

name = StringVar()
        
entry_1 = Entry(frame,textvariable=name)
entry_1.pack(pady=2,padx=2)


label_2 = Label(frame,bg="light blue", text="EMAIL ID:",width=20,font=("Georgia 20 underline"))
label_2.pack()

email = StringVar()

entry_2 = Entry(frame,textvariable=email)
entry_2.pack(pady=10,padx=10)
        

label_3 = Label(frame, text="AUGMENTIN 625 DUO",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_3.pack()

options = [
    "None",
    "15",
    "30",
    "45",
    "60"
]
  
clicked_aug = StringVar()
  
clicked_aug.set( "None" )
  
drop_1 = OptionMenu( frame , clicked_aug , *options )
drop_1.pack(pady=10,padx=10)


label_4 = Label(frame, text="DOLO 650",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_4.pack()

clicked_dolo = StringVar()
  
clicked_dolo.set( "None" )
  
drop_2 = OptionMenu( frame , clicked_dolo , *options )
drop_2.pack(pady=10,padx=10)


label_4_5 = Label(frame, text="DISPERINE",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_4_5.pack()

clicked_disp = StringVar()
  
clicked_disp.set( "None" )
  
drop_3 = OptionMenu( frame , clicked_disp , *options )
drop_3.pack(pady=10,padx=10)


label_5 = Label(frame, text="ULTRACET 550",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_5.pack()
            
clicked_ultra = StringVar()
  
clicked_ultra.set( "None" )
  
drop_4 = OptionMenu( frame , clicked_ultra , *options )
drop_4.pack(pady=10,padx=10)


frame3 = LabelFrame(main, bd=5, width=100,bg="light blue")
frame3.pack(side=RIGHT,expand=True,fill=BOTH)
            
label_6 = Label(frame3, text="MELATONIN",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_6.pack()

clicked_mel = StringVar()
  
clicked_mel.set( "None" )
  
drop_5 = OptionMenu( frame3 , clicked_mel , *options )
drop_5.pack(pady=10,padx=10)

label_7 = Label(frame3, text="RIFAGUT",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_7.pack()
        
clicked_rifa = StringVar()
  
clicked_rifa.set( "None" )
  
drop_6 = OptionMenu( frame3 , clicked_rifa , *options )
drop_6.pack(pady=10,padx=10)


label_8 = Label(frame3, text="AMRYL 250",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_8.pack()

clicked_amryl = StringVar()
  
clicked_amryl.set( "None" )
  
drop_7 = OptionMenu( frame3 , clicked_amryl , *options )
drop_7.pack(pady=10,padx=10)


label_9 = Label(frame3, text="MULTIVITAMINS",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_9.pack()

clicked_vitam = StringVar()
  
clicked_vitam.set( "None" )
  
drop_8 = OptionMenu( frame3 , clicked_vitam , *options )
drop_8.pack(pady=10,padx=10)


label_10 = Label(frame3, text="NEBISTAR",width=20,font=("Georgia 20 underline"),bg="light blue",pady=2,padx=2)
label_10.pack()

clicked_nebi = StringVar()
  
clicked_nebi.set( "None" )
  
drop_9 = OptionMenu( frame3 , clicked_nebi , *options )
drop_9.pack(pady=10,padx=10)

        
frame2 = LabelFrame(main, bd=10, bg="light blue", width=0)
frame2.pack(side=BOTTOM,expand=True,fill=X)

Button(frame2, text='Submit', font='20', width=15,bg='dark blue',fg='white',command=Punchin).pack()

main.mainloop()
