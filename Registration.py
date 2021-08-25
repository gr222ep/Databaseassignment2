from tkinter import *
from tkinter import messagebox
import re
from tkinter import ttk
import pymysql
from pymysql import Error
import os,sys
pyCmd=sys.executable
class reg(Tk):
    def __init__(self):
        super().__init__()
        self.title("LIBRARY MANAGEMENT SYSTEM")
        self.maxsize(866, 668)
        self.minsize(866, 668)
        self.state("normal")
        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        m = StringVar()
        n = StringVar()
        x = StringVar()
        p = StringVar()
        v = StringVar()
        u = StringVar()
        s = StringVar()
        r = StringVar()

        def insert():
            try:
                self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                self.pointTo = self.connection.cursor()
                confrmMsg = self.pointTo.execute("Insert into admin values (%s,%s,%s,%s,%s,%s,%s)",(m.get(), n.get(), x.get(), p.get(), v.get(), s.get(), r.get()))
                self.connection.commit()
                self.pointTo.close()
                self.connection.close()
                if confrmMsg:
                    messagebox.showinfo("Confirm", "Data Inserted Successfully")
                    self.destroy()
                    os.system('%s %s' % (pyCmd, 'Main.py'))
            except Exception as ex:
                print(ex)
# verify input
        def verifyUserCredentials():
            if(len(m.get())) < 5:
                messagebox.showinfo("Error","Enter User Id\nUser Id should be greater than 5 letters")
            elif (len(n.get())) < 3:
                messagebox.showinfo("Error", "Please Enter Your Full Name")
            elif (len(x.get())) < 8:
                while True:
                    if not re.search("[a-z]", x.get()):
                        flag = -1
                        break
                    elif not re.search("[A-Z]", x.get()):
                        flag = -1
                        break
                    elif not re.search("[0-9]", x.get()):
                        flag = -1
                        break
                    elif not re.search("[_@$]", x.get()):
                        flag = -1
                        break
                    elif re.search("\s", x.get()):
                        flag = -1
                        break
                    else:
                        flag = 0
                        break
                if len(x.get()) == 0:
                    messagebox.showinfo("Error","Please Enter Your Password")
                elif flag == -1:
                    messagebox.showinfo("Error","Minimum 8 characters.\nThe alphabets must be between [a-z]\nAt least one alphabet should be of Upper Case [A-Z]\nAt least 1 number or digit between [0-9].\nAt least 1 character from [ _ or @ or $ ].")
            elif len(p.get()) == 0:
                messagebox.showinfo("Error","Please select a question")
            elif len(v.get()) == 0:
                messagebox.showinfo("Error","Please write an answer")
            elif len(s.get()) == 0 or len(s.get()) > 10 or len(s.get()) < 10:
                messagebox.showinfo("Error","Enter Valid Phone Number")
            elif len(s.get()) == 10:
                if s.get().isdigit():
                    cas = re.fullmatch("[6-9][0-9]{9}", s.get())
                    if cas is None:
                        messagebox.showinfo("Error","Check Your Phone Number")
                    else:
                        insert()
#label and input
        Label(self,text="Library Management System",font=("Arial",25,'bold'),fg="purple").place(x=200,y=80)
        #Label(self,text="Enter your details and click save",font=("Arial",20,'bold'),fg="brown").place(x=200,y=600)
        Label(text = "Library Information",fg='brown',font = ("Arial",13,"bold")).place(x=300,y=220)
        Label( text="Username",fg='brown', font=("Arial", 13, "bold")).place(x=100, y=260)
        Label( text="Name",fg='brown', font=("Arial", 13, "bold")).place(x=100, y=300)
        Label( text="Password",fg='brown', font=("Arial", 13, "bold")).place(x=100, y=340)
        Label( text="Security Question",fg='brown', font=("Arial", 13, "bold")).place(x=100, y=380)
        Label( text="Security Answer",fg='brown', font=("Arial", 13, "bold")).place(x=100, y=420)
        Label( text="Phone",fg='brown', font=("Arial", 13, "bold")).place(x=100, y=460)
        Label( text="City",fg='brown', font=("Arial", 13, "bold")).place(x=100, y=500)
        Entry(textvariable=m,width=60).place(x=250,y=260)
        Entry( textvariable=n, width=60).place(x=250, y=300)
        Entry( show = '*',textvariable=x, width=60).place(x=250, y=340)
        ttk.Combobox( textvariable = p, values=["What is your school name?", "What is your home name?","What is your Father name?", "What is your pet name?"], width=57,state="readonly").place(x=250, y=380)
        Entry( show = '*',textvariable=v, width=60).place(x=250, y=420)
        Entry( textvariable=s, width=60).place(x=250, y=460)
        Entry( textvariable=r, width=60).place(x=250, y=500)
        Button( text="Save", width=10, font=("Arial", 13, "bold"), command=verifyUserCredentials).place(x=300, y=550)
        Button( text="Cancel", width=10, font=("Arial", 13, "bold")).place(x=460, y=550)

reg().mainloop()
