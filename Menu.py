from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import Error
import os
import sys
from tkinter import ttk
pyCmnd = sys.executable
class MainWin(Tk):
    def __init__(self):
        super().__init__()
        self.configure(bg='red')
        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        self.maxsize(1320, 768)
        self.minsize(1320, 768)
        self.state('zoomed')
        self.title('LIBRARY MANAGEMENT SYSTEM')
        self.m = StringVar()
        self.n = StringVar()
        self.mymenu = Menu(self)

        # calling scripts
        def a_s():
            os.system('%s %s' % (pyCmnd, 'NewStudentAddition.py'))

        def a_b():
            os.system('%s %s' % (pyCmnd, 'NewBookAddition.py'))

        def r_b():
            os.system('%s %s' % (pyCmnd, 'BookRemove.py'))

        def r_s():
            os.system('%s %s' % (pyCmnd, 'StudentRemove.py'))

        def ib():
            os.system('%s %s' % (pyCmnd, 'BookIssue.py'))

        def rb1():
            os.system('%s %s' % (pyCmnd, 'BookRenewal.py'))

        def ret():
            os.system('%s %s' % (pyCmnd, 'BookReturn.py'))

        def sea():
            os.system('%s %s' % (pyCmnd, 'BookSearch.py'))

        def log():
            self.destroy()
            os.system('%s %s' % (pyCmnd, 'LibraryMain.py'))
            exit()

        def add_user():
            os.system('%s %s' % (pyCmnd, 'viewIssues.py'))

        def rem_user():
            os.system('%s %s' % (pyCmnd, 'RemoveUser.py'))
        def rem1_user():
            os.system('%s %s' % (pyCmnd, 'BookWiseIssues.py'))
        def class_user():
            os.system('%s %s' % (pyCmnd, 'ClassficationUser.py'))

        def cfine():
            os.system('%s %s' % (pyCmnd, 'FineClearence.py'))

        def sest():
            os.system('%s %s' % (pyCmnd, 'SearchStudent.py'))

        # creating table

        self.listForm = ttk.Treeview(self, height=14,columns=('SID', 'Name', 'Fine', 'Book Name', 'Issue Date', 'Return Date'))
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.listForm.yview)
        self.hsb = ttk.Scrollbar(self, orient="horizontal", command=self.listForm.xview)
        self.listForm.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.listForm.heading("#0", text='Book ID', anchor='center')
        self.listForm.column("#0", width=100, minwidth=100, anchor='center')
        self.listForm.heading("#1", text='SID')
        self.listForm.column("#1", width=100, minwidth=100, anchor='center')
        self.listForm.heading("Name", text='Name')
        self.listForm.column("Name", width=150, minwidth=150, anchor='center')
        self.listForm.heading("Fine", text='Fine')
        self.listForm.column("Fine", width=100, minwidth=100, anchor='center')
        self.listForm.heading("Book Name", text='Book Name')
        self.listForm.column("Book Name", width=200, minwidth=200, anchor='center')
        self.listForm.heading("Return Date", text='Return Date')
        self.listForm.column("Return Date", width=125, minwidth=125, anchor='center')
        self.listForm.heading("Issue Date", text='Issue Date')
        self.listForm.heading("Issue Date", text='Issue Date')
        self.listForm.column("Issue Date", width=125, minwidth=125, anchor='center')
        self.listForm.place(x=220, y=360)
        self.vsb.place(x=1123, y=361, height=287)
        self.hsb.place(x=220, y=650, width=922)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

        list1 = Menu(self)
        list1.add_command(label="Student", command=a_s)
        list1.add_command(label="Book", command=a_b)


        list2 = Menu(self)
        list2.add_command(label="Student", command=r_s)
        list2.add_command(label="Book", command=r_b)

        list3 = Menu(self)
        list3.add_command(label="On Students wise", command=add_user)
        list3.add_command(label="On Books wise", command=rem1_user)
        list3.add_command(label="on Classification wise", command=class_user)

        self.mymenu.add_cascade(label='Add', menu=list1)
        self.mymenu.add_cascade(label='Remove', menu=list2)
        self.mymenu.add_cascade(label='Book Issues', menu=list3)
        

        self.config(menu=self.mymenu)

        def ser():
            try:
                self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                self.pointTo = self.connection.cursor()
                self.change = int(self.m.get())
                self.pointTo.execute(
                    "Select issue.BID,issue.SID,students.name,students.Fine,books.Book_name,issue.Issue_date,issue.Return_date from books,students,issue where issue.BID = books.Book_Id and SID = %s",
                    (self.change))
                self.pc = self.pointTo.fetchall()
                if self.pc:
                    self.listForm.delete(*self.listForm.get_children())
                    for row in self.pc:
                        self.listForm.insert("", 'end', text=row[0],values=(row[1], row[2], row[3], row[4], row[5], row[6]))
                else:
                    messagebox.showinfo("Error", "Either ID is wrong or The book is not yet issued on this ID")
            except Exception as ex:
                print(ex)

        def ent():
            try:
                self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                self.pointTo = self.connection.cursor()
                self.pointTo.execute("Select issue.BID,issue.SID,students.name,students.Fine,books.Book_name,issue.Issue_date,issue.Return_date from books,students, issue where issue.BID = books.Book_Id and BID = %s",
                    (self.n.get()))
                self.pc = self.pointTo.fetchall()
                if self.pc:
                    self.listForm.delete(*self.listForm.get_children())
                    for row in self.pc:
                        self.listForm.insert("", 'end', text=row[0],
                                             values=(row[1], row[2], row[3], row[4], row[5], row[6]))
                else:
                    messagebox.showinfo("Error", "Please Enter a valid ID")
            except Exception as ex:
                    print(ex)

        def check():
            try:
                connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                pointTo = connection.cursor()
                pointTo.execute("Select * from admin")
                z = pointTo.fetchone()
                if not z:
                    messagebox.showinfo("Error", "Please Register A user")
                    confirmMessage = messagebox.askyesno("Confirm", "Do you want to register a user")
                    if confirmMessage:
                        self.destroy()
                        os.system('%s %s' % (pyCmnd, 'Registration.py'))
                else:
                    # label and input box
                    self.label3 = Label(self, text='LIBRARY MANAGEMENT SYSTEM', fg='red',
                                        font=('Arial', 30, 'bold'))
                    self.label3.place(x=400, y=22)
                    self.label4 = Label(self, text="STUDENT ID", font=('Arial', 18, 'bold'))
                    self.label4.place(x=80, y=107)
                    self.e1 = Entry(self, textvariable=self.m, width=90).place(x=405, y=110)
                    self.srt = Button(self, text='Search', width=15, font=('arial', 10), command=ser).place(x=1000,
                                                                                                            y=106)
                    self.label5 = Label(self, text="BOOK ID", font=('Arial', 18, 'bold'))
                    self.label5.place(x=95, y=150)
                    self.e2 = Entry(self, textvariable=self.n, width=90).place(x=405, y=160)
                    self.nrt = Button(self, text='Find', width=15, font=('arial', 10), command=ent).place(x=1000, y=150)
                    self.label6 = Label(self, text="INFORMATION DETAILS", font=('Arial', 15, 'underline', 'bold'))
                    self.label6.place(x=510, y=300)
                    self.nutton = Button(self, text='Search Student', width=25, font=('Arial', 10),
                                         command=sest).place(x=240, y=250)
                    self.nutton = Button(self, text='Search Book', width=25, font=('Arial', 10), command=sea).place(
                        x=470, y=250)
                    self.nrt = Button(self, text="Issue Book", width=15, font=('Arial', 10), command=ib).place(x=700,
                                                                                                                  y=250)
                    self.nrt = Button(self, text="Renew Book", width=15, font=('Arial', 10), command=rb1).place(
                        x=850, y=250)
                    self.nrt = Button(self, text="Return Book", width=15, font=('Arial', 10), command=ret).place(
                        x=1000, y=250)
                    self.nrt = Button(self, text="LOGOUT", width=15, font=('Arial', 10), command=log).place(x=1150,
                                                                                                               y=105)
                    self.nrt = Button(self, text="Fine Clear", width=15, font=('Arial', 10), command=cfine).place(
                        x=1150, y=150)
            except Exception as ex:
                print(ex)

        check()


MainWin().mainloop()
