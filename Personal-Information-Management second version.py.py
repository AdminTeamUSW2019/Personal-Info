from tkinter import *
import tkinter.messagebox as tkMessageBox
#import sqlite3
import tkinter as tk
import tkinter.ttk as ttk

root = Tk()
root.title("Python: Personal information management")
USERNAME = StringVar()
PASSWORD = StringVar()
username="ADMIN"
password="ADMIN"
width = 1024
height = 1000
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#9BE3DE")


def Database():
   conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:\Database1.accdb;')
   cursor = conn.cursor()
   cursor.execute('select * Admin')
   
   for row in cursor.fetchall():


def policydocument():
    global policydoc
    policydoc = Toplevel()
    policydoc.config(bg="#BEEBE9")
    scrollbar = Scrollbar(policydoc)
    scrollbar.pack(side=RIGHT, fill=Y)
    policydoc.title("Personal information Management/policydoc")
    width = 1000
    height = 1000
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    policydoc.geometry("%dx%d+%d+%d" % (width, height, x, y))
    policydoc.resizable(0, 0)
    file = open('PIMPolicyDoc.txt', 'r+')  # Text file i am using
    with open('PIMPolicyDoc.txt') as file:  # Use file to refer to the file object
        data = file.read()  # date=current text in text file
    policy_txt = Text(policydoc, yscrollcommand=scrollbar.set, height=40, width=90)
    policy_txt.insert('1.0', data)
    policy_txt.pack()
    chkValue =BooleanVar()
    chkValue.set(False)
    check_btn=Checkbutton(policydoc, text="I Agree", variable=chkValue).pack()
    #chkAgree.grid(row = 1,column=0)
    #btn_continue = Button(policydoc, Text="Continue", font=('arial', 16), command=ContinuetodataBase(root)).grid()
    #btn_continue.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_continue = Button(policydoc, text="Continue")
    btn_continue.pack(side=TOP, padx=10, pady=10, fill=X)




def callback():
    Acclogin.destroy()
    policydocument()

def Accountlogin():
    global Acclogin
    global lbl_result
    Acclogin =Frame(root, width=800, height=10000, bd=1, relief=SOLID)
    Acclogin.pack(side=TOP)
    lbl_username = Label(Acclogin, text="Username:", font=('arial', 25), bd=1)
    lbl_username.grid(row=0)
    username=Entry(Acclogin, textvariable=USERNAME, font=('arial', 25), width=15)
    username.grid(row=0,column=1)
    lbl_password= Label(Acclogin, text="Password:", font=('arial', 25), bd=1)
    lbl_password.grid(row=1)
    lbl_result = Label(Acclogin, text = "" , font('arial', 18))
    lbl_result.grid(row = 3 , columnspan= 2)
    password = Entry(Acclogin, textvariable=PASSWORD, font=('arial', 25), width=15)
    password.grid(row=1,column=1)
    login_button = Button(Acclogin, text="LOGIN",font=('arial',16),command=callback).grid()
    login_button.pack(padx=20, pady=40)


def cll():
    btn_display.configure(state= DISABLED)
    Accountlogin()

def login(event = None)
    global user_id
    Database()
    if USERNAME.get() == "" or PASSWORD.get()== "":
    	lbl_result.config(text= "Please input your login detials!", fg= "red")
    else:
        cursor.execute("SELECT  * FROM 'Admin' WHERE 'username' = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            cursor.execute("SELECT * FROM `Admin` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
            data = cursor.fetchone()
            user_id = data[0]
            USERNAME.set("")
            PASSWORD.set("")
            lbl_result.config(text="")
            ShowHome()
        else:
            lbl_result.config(text="Invalid username or password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")
    cursor.close()
    conn.close() 



lbl_display = Label(root, text="Personal Information Management", font=('arial', 40), width=800).pack()
btn_display = Button(root, text="ACCOUNT LOGIN", font=('arial', 16), command= cll)
btn_display.pack(fill=tk.X, padx=400, pady=250)


root.mainloop()
