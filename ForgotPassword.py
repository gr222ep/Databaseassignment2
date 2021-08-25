from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from pymysql import Error
class Fp(Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap(r'libico.ico')
        self.maxsize(480, 320)
        self.title("Find Your Password Here")
        self.canvas = Canvas(width=500, height=200)
        self.canvas.pack()

        m = StringVar()
        n = StringVar()
        o = StringVar()
        p = StringVar()
        q = StringVar()

        def ins():
            if (len(p.get())) < 8 or len(q.get()) < 8:
                while True:
                    if not re.search("[a-z]", p.get()):
                        flag = -1
                        break
                    elif not re.search("[A-Z]", p.get()):
                        flag = -1
                        break
                    elif not re.search("[0-9]", p.get()):
                        flag = -1
                        break
                    elif not re.search("[_@$]", p.get()):
                        flag = -1
                        break
                    elif re.search("\s", p.get()):
                        flag = -1
                        break
                    else:
                        flag = 0
                        break
                if len(p.get()) == 0:
                    messagebox.showinfo("Error", "Please Enter Your Password")
                elif flag == -1:
                    messagebox.showinfo("Error",
                                        "Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
            elif p.get() != q.get():
                messagebox.showinfo("Error", "New and retype password are not some")
            else:
                try:
                    self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.connection.cursor()
                    self.pointTo.execute("Update admin set password = ? where id = ?", (q.get(), m.get()))
                    self.connection.commit()
                    self.pointTo.close()
                    self.connection.close()
                    messagebox.showinfo("Confirm", "Password Updated Successfully")
                    self.destroy()
                except Error:
                    messagebox.showerror("Error", "Something Goes Wrong")

        def checkUser():
            if len(m.get()) < 5:
                messagebox.showinfo("Error", "Please Enter User Id")
            elif len(n.get()) == 0:
                messagebox.showinfo("Error", "Please Choose a question")
            elif len(o.get()) == 0:
                messagebox.showinfo("Error", "Please Enter a answer")
            else:
                try:
                    self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.connection.cursor()
                    self.pointTo.execute("Select id,secQuestion,secAnswer from admin where id = ?", (m.get()))
                    pc = self.pointTo.fetchone()
                    if not pc:
                        messagebox.showinfo("Error", "Something Wrong in the Details")
                    elif str(pc[0]) == m.get() or str(pc[1]) == n.get() or str(pc[2]) == o.get():
                        Label(self, text="New Password", font=('arial', 15, 'bold')).place(x=40, y=220)
                        Entry(self, show="*", textvariable=p, width=40).place(x=230, y=224)
                        Label(self, text="Retype Password", font=('arial', 15, 'bold')).place(x=40, y=270)
                        Entry(self, show="*", textvariable=q, width=40).place(x=230, y=274)
                        Button(self, text="Submit", width=15, command=ins).place(x=230, y=324)
                except Error:
                    messagebox.showerror("Error", "Something Goes Wrong")

        # label and input box
        Label(self, text="Enter User Id",  fg='brown', font=('arial', 14, 'bold')).place(x=40, y=20)
        Label(self, text="Security Question",  fg='brown', font=('arial', 14, 'bold')).place(x=40, y=70)
        Label(self, text="Security Answer",  fg='brown', font=('arial', 14, 'bold')).place(x=40, y=120)
        Entry(self, textvariable=m, width=40).place(x=230, y=24)
        ttk.Combobox(self, textvariable=n,
                     values=["What is your school name?", "What is your home name?", "What is your Father name?",
                             "What is your pet name?"], width=37, state="readonly").place(x=230, y=74)
        Entry(self, show="*", textvariable=o, width=40).place(x=230, y=124)
        Button(self, text='Verify', width=15, command=checkUser).place(x=275, y=170)


Fp().mainloop()
