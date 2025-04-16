from tkinter import *
import mysql.connector
from tkinter import messagebox
import re

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root@123",
  database="signups"
  )

print(mydb)
mycursor = mydb.cursor()

try:
    mycursor.execute("create database signups")
except:
    print("Database already exist, create a new database!")
finally:
    mycursor.execute("show databases")
    for x in mycursor:
        print(x)

# mycursor.execute("""create table data (
#                  NAME varchar(30),
#                  MOBILE_NO varchar(11),
#                  EMAIL varchar(30),
#                  ADDRESS varchar(80),
#                  AADHAR_CARD varchar(13),
#                  PASSWORD varchar(30),
#                  CONFIRM_PASSWORD varchar(30)
#                  )""")

tk = Tk()
tk.title("WELCOME")
tk.geometry("400x200")

#after hitting signup button
def signuppg():
    tk.withdraw()
    signup = Tk()
    signup.title("SIGN UP")
    signup.geometry("400x400")

# label and entry of signup
    Label(signup, text="NAME").place(x=0,y=10)
    name_e1 = Entry(signup, width = 20)
    name_e1.place(x=130,y=10)

    Label(signup, text="MOBILE NO").place(x=0,y=40)
    mob_e2 = Entry(signup, width = 20)
    mob_e2.place(x=130,y=40)

    Label(signup, text="EMAIL").place(x=0,y=70)
    email_e3 = Entry(signup, width = 20)
    email_e3.place(x=130,y=70)

    Label(signup, text="ADDRESS").place(x=0,y=100)
    address_e4 = Entry(signup, width = 20)
    address_e4.place(x=130,y=100)

    Label(signup, text="AADHAR").place(x=0,y=140)
    aadhar_e5 = Entry(signup, width = 20)
    aadhar_e5.place(x=130,y=140)

    Label(signup, text="PASSWORD").place(x=0,y=170)
    passwrd_e6 = Entry(signup, width = 20)
    passwrd_e6.place(x=130,y=170)

    Label(signup, text="CONFIRM PASSWORD").place(x=0,y=200)
    conpasswrd_e7 = Entry(signup, width = 20)
    conpasswrd_e7.place(x=130,y=200)

    def sign_d():
        if name_e1.get() == "" or mob_e2.get() == "" or email_e3.get() == "" or address_e4.get() == "" or aadhar_e5.get() == "" or passwrd_e6.get() == "" or conpasswrd_e7.get() == "":
            messagebox.showwarning("warning","Enter all credentials !!")

        elif not re.match(r"^[A-Za-z\s'.-]{2,50}$",name_e1.get()):
            messagebox.showinfo("information","Name exceeds the limit")

        elif not re.match(r'^[6-9]{1}[0-9]{9}$',mob_e2.get()):
            messagebox.showinfo("information","Mobile number should be of 10 digits")

        elif not re.match(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email_e3.get()):
            messagebox.showinfo("information","Enter valid Email")

        elif len(address_e4.get())>100:
            messagebox.showinfo("information","Addess exceeds the given limit")

        elif not re.match(r'^\d{12}$',aadhar_e5.get()):
            messagebox.showinfo("information","Enter valid Aadhar number")

        elif not re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}',passwrd_e6.get()):
            messagebox.showinfo("information","Password must contain atleast  8 characters containing 1 uppercase,1 lowercase,1 number and 1 special chartacter")

        elif passwrd_e6.get() != conpasswrd_e7.get():
            messagebox.showerror("error","Password do not match")

        else:
            mycursor.execute("insert into data (NAME,MOBILE_NO,EMAIL,ADDRESS,AADHAR_CARD,PASSWORD,CONFIRM_PASSWORD) values (%s,%s,%s,%s,%s,%s,%s)",([name_e1.get(),mob_e2.get(),email_e3.get(),address_e4.get(),aadhar_e5.get(),passwrd_e6.get(),conpasswrd_e7.get()]))
            mydb.commit()
            messagebox.showinfo("information","SignUp Successfull !")  
            signup.withdraw()
            tk.deiconify()

 # submit button
    subbtn = Button(signup, text="Submit", command=sign_d)
    subbtn.place(x=170,y=250)
   
def loginpg():
    tk.withdraw()
    loginwnd = Tk()
    loginwnd.title ("LOGIN")
    loginwnd.geometry("500x300")

    Label(loginwnd, text="MOBILE NO").place(x=0,y=60)
    mne_e1 = Entry(loginwnd, width=25)
    mne_e1.place(x=120,y=60)

    Label(loginwnd, text="PASSWORD").place(x=0,y=100)
    P_e2= Entry(loginwnd, width=25)
    P_e2.place(x=120,y=100)

    def login_d():
        if mne_e1.get() == "" or P_e2.get() == "":
            messagebox.showinfo("information","Enter Login details !!")
            return
        
        mycursor.execute("SELECT * FROM data WHERE MOBILE_NO = %s AND PASSWORD = %s", (mne_e1.get(), P_e2.get()))
        result = mycursor.fetchone()
        
        if result:
            messagebox.showinfo("Login Successful", "Welcome to the system!")
            loginwnd.withdraw()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials, please try again.")

    def dhaa():
        loginwnd.withdraw()
        tk.deiconify()

    nwacc = Button(loginwnd, text="DON'T HAVE AN ACCOUNT ?!", command=dhaa)
    nwacc.place(x=250,y=150) 

    log = Button(loginwnd, text="LOGIN",command=login_d)
    log.place(x=180,y=150)

# Main Page Label
msgpas = Label(tk, text="\"WE WELCOME YOU\"", font=("Arial", 12), bg="black", fg="white")
msgpas.pack()

#login button
login = Button(tk, text="LOGIN", bg="black", fg="white", command=loginpg)
login.place(x=250,y=100)

#sign up button
signup = Button(tk, text="SIGN UP", bg="black", fg="white", command=signuppg)
signup.place(x=120,y=100)

tk.mainloop()