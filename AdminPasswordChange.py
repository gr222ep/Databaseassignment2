from tkinter import *
import pymysql
from pymysql import Error
from tkinter import messagebox
class Set(Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Update New Password")
        self.maxsize(500,300)
        self.minsize(500,300)
        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        def verify():
            if len(q.get()) == 0:
                messagebox.showinfo("Error","Enter Your Valid User Id")
            elif len(m.get()) < 5 and len(n.get()) < 5 and len(p.get()) < 5:
                messagebox.showinfo("Error","Enter a Valid Password")
            elif n.get() != p.get():
                messagebox.showinfo("Error","Passwords are Mismatched.!")
            else:
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.conn.cursor()
                    self.pointTo.execute("Select password from admin where id = %s",(q.get()))
                    tValue = self.pointTo.fetchone()
                    if tValue:
                        if str(tValue[0]) == m.get():
                            self.pointTo.execute("UPDATE admin SET password = %s WHERE id = %s",(n.get(),q.get()))
                            self.conn.commit()
                            self.conn.close()
                            messagebox.showinfo("Successful","Password Updated successfully")
                        else:
                            messagebox.showinfo("Error","Old Password Does not Match")
                    else:
                        messagebox.showinfo("Error", "The User Doesn't Existed")
                except Exception as ex:
                    print(ex)
            m.set("")
            n.set("")
            p.set("")
            q.set("")
        userid = Label(self, text="User Id", font=('arial', 13, 'bold')).place(x=40, y=50)
        q = StringVar()
        Uentry= Entry(self, textvariable=q, width=30).place(x=250, y=55)
        oldpassword = Label(self,text="Old Password",font=('arial', 13, 'bold')).place(x=40,y=100)
        m=StringVar()
        oldpasswordvalue = Entry(self,show='*',textvariable=m,width = 30).place(x=250,y=105)
        newpassword = Label(self,text="New Password",font=('arial', 13, 'bold')).place(x=40,y=150)
        n=StringVar()
        newpasswordvalue = Entry(self,show='*',textvariable=n,width = 30).place(x=250,y=155)
        reenterPassword = Label(self,text="Re-Enter password",font=('arial', 13, 'bold')).place(x=40,y=200)
        p=StringVar()
        reenterPasswordValue = Entry(self,show='*',textvariable =p,width = 30).place(x=250,y=205)
        updateButton=Button(self,text="Update",width=15,command = verify).place(x=280,y=255)
Set().mainloop()
