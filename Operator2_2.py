from tkinter import ttk

import tkinter as tk

import mysql.connector as ms


mydb=ms.connect(host="localhost",user="root",password="tiger")
mycur=mydb.cursor()
mycur.execute("use custody")


root = tk.Tk()

tree = ttk.Treeview(root, column=("c1", "c2", "c3"), show='headings')

tree.column("#1", anchor=tk.CENTER)

tree.heading("#1", text="PATIENT ID")

tree.column("#2", anchor=tk.CENTER)

tree.heading("#2", text="NAME")

tree.column("#3", anchor=tk.CENTER)

tree.heading("#3", text="E-MAIL")

tree.pack()

qry=("select * from pattest")

mycur.execute(qry)

rows=mycur.fetchall()    

for i in rows:

            k=[]
            k.append(i[0])
            k.append(i[1])
            k.append(i[5])
            tree.insert("", tk.END, values=k)
            
root.mainloop()
