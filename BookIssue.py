from tkinter import *
from datetime import timedelta, date
from tkinter import messagebox
import pymysql
from pymysql import Error
import os
import sys
py = sys.executable
class issue(Tk):
    def __init__(self):
        super().__init__()
        self.title('LIBRARY SYSTEM MANAGEMENT SYSTEM')
        self.maxsize(420, 280)

        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        p = StringVar()
        q = StringVar()

        # verifying input
        def isb():
            if len(p.get()) == 0 or len(q.get()) == 0:
                messagebox.showinfo("Error", "Please Enter both Book Id/Student ID's")
            else:
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.conn.cursor()
                    self.pointTo.execute("Select Availiability from books where Book_Id = %s", (p.get()))
                    tValue = self.pointTo.fetchone()
                    try:
                        if str(tValue[0]) == '0':
                            messagebox.showinfo("Oop's", "The Given Book is Already Issued")
                        else:
                            self.pointTo.execute("Select Fine from students where Student_Id = %s", (q.get()))
                            findfineValue = list(self.pointTo.fetchone())
                            self.pointTo.execute("Select Books_Issued from students where Student_Id = %s", (q.get()))
                            bookissueList = list(self.pointTo.fetchone())
                            if bookissueList[0] < 3:
                                if findfineValue[0] > 100:
                                    messagebox.showerror('Oops', 'Cannot Issue.Please Pay the Fine')
                                elif findfineValue [0] == 0:
                                    Date_req = date.today() + timedelta(days=3)
                                    todayDate = date.today()
                                    print(Date_req)
                                    self.pointTo.execute("INSERT INTO issue VALUES (%s,%s,%s,%s)",(p.get(), q.get(), todayDate, Date_req))
                                    self.pointTo.execute("UPDATE books set Availiability=0 where Book_Id = %s",(p.get()))
                                    bookissueList[0] =bookissueList[0] + 1

                                    self.pointTo.execute("Update students set Books_Issued = %s where Student_Id = %s", (bookissueList[0], q.get()))

                                    self.conn.commit()
                                    self.conn.close()
                                    messagebox.showinfo('Save', 'Successfully Issued')
                                    conf = messagebox.askyesno("Confirm", "Do you want to issue another book%s")
                                    if conf:
                                        self.destroy()
                                        os.system('%s %s' % (py, 'BookIssue.py'))
                                    else:
                                        self.destroy()
                                elif findfineValue [0] > 0:
                                    Confirm = messagebox.askyesno('Confirm','Are you sure you want to issue.There is a fine')
                                    if Confirm:
                                        Date_req = date.today() + timedelta(days=3)
                                        todayDate = date.today()
                                        self.pointTo.execute("INSERT INTO issue VALUES (%s,%s,%s,%s)", (p.get(), q.get(), todayDate, Date_req))
                                        self.pointTo.execute("UPDATE books set Availiability=0 where Book_Id = %s",  (p.get()))
                                        bookissueList[0] = bookissueList[0] + 1
                                        self.pointTo.execute("Update students set Books_Issued = %s where Student_Id = %s",(bookissueList[0], q.get()))
                                        self.conn.commit()
                                        self.conn.close()
                                        messagebox.showinfo('Save', 'Successfully Issued')
                                        conf = messagebox.askyesno("Confirm", "Do you want to issue another book%s")
                                        if conf:
                                            self.destroy()
                                            os.system('%s %s' % (py, 'BookIssue.py'))
                                        else:
                                            self.destroy()
                                    else:
                                        messagebox.showinfo('Oops', 'Not Issued')
                                elif findfineValue[0] > 100:
                                    messagebox.showerror('Oops', 'Cannot Issue.Please Pay the Fine')
                            else:
                                messagebox.showerror("Can't Issue", "Maximum number of books already issued")
                    except TypeError:
                        messagebox.showinfo("Oop's", "Either BookID or StudentId Not Available")
                except Exception as ex:
                    print(ex)

        # label and input box
        Label(self, text='Issuing New Book', font=('Arial Black', 20)).place(x=85, y=40)
        Label(self, text='Book ID:', font=('Arial', 14), fg='black').place(x=45, y=100)
        Entry(self, textvariable=p, width=40).place(x=160, y=106)
        Label(self, text='Student ID:', font=('Arial', 14), fg='black').place(x=40, y=150)
        Entry(self, textvariable=q, width=40).place(x=160, y=158)
        Button(self, text="ISSUE", width=20, command=isb).place(x=200, y=200)


issue().mainloop()
