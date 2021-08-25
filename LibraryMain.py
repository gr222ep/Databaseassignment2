from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import Error
import os
py=sys.executable
class Lib(Tk):
    def __init__(self):
        super().__init__()
        self.a = StringVar()
        self.b = StringVar()
        self.maxsize(500, 400)
        self.minsize(500, 400)
        self.state("zoomed")
        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        self.title("LIBRARY MANAGEMENT SYSTEM")


#verifying input
        def chex():
            if len(self.user_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD" )
            elif len(self.pass_text.get()) < 0:
                messagebox.showinfo(" INVALID USERNAME OR PASSWORD")
            else:
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.myCursor = self.conn.cursor()
                    self.myCursor.execute("Select * from admin where id=%s AND password =%s",(self.user_text.get(),self.pass_text.get()))
                    self.pc = self.myCursor.fetchall()
                    self.myCursor.close()
                    self.conn.close()
                    if self.pc:
                        self.destroy()
                        os.system('%s %s' % (py, 'Menu.py'))
                    else:
                        messagebox.showinfo('Error', 'Username and password not found')
                        self.user_text.delete(0, END)
                        self.pass_text.delete(0, END)
                except Exception as ex:
                        print(ex)
        def fp():
            os.system('%s %s' % (py, 'ForgotPassword.py'))

        def check():
            try:
                conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                mycursor = conn.cursor()
                mycursor.execute("Select * from admin")
                z = mycursor.fetchone()
                mycursor.close()
                conn.close()
                if not z:
                    messagebox.showinfo("Error", "Please Register A user")
                    x = messagebox.askyesno("Confirm","Do you want to register a user")
                    if x:
                        self.destroy()
                        os.system('%s %s' % (py, 'Registration.py'))
                else:
                    self.lbleName = Label(self, text="USER LOGIN PAGE",fg = 'BROWN', font=("ARIAL", 24,'bold'))
                    self.lbleName.place(x=100, y=100)
                    self.lbleName1 = Label(self, text="Username",fg = 'red', font=("Times New roman", 18, 'bold'))
                    self.lbleName1.place(x=130, y=150)
                    self.user_text = Entry(self, textvariable=self.a, width=20)
                    self.user_text.place(x=250, y=150)
                    self.lbleName2 = Label(self, text="Password",fg = 'red', font=("Times new roman", 18, 'bold'))
                    self.lbleName2.place(x=130, y=195)
                    self.pass_text = Entry(self, show='*', textvariable=self.b, width=20)
                    self.pass_text.place(x=250, y=190)
                    self.butt = Button(self, text="Login", font=10, width=8, command=chex).place(x=150, y=250)
                    self.butt2 = Button(self, text="Forgot Password",font=8, width=15, command=fp).place(x=150, y=300)
            except Exception as ex:
                print(ex)

        check()

Lib().mainloop()
