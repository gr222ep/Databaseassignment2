from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import Error
from datetime import datetime,date
import os
import sys
py = sys.executable
class renew(Tk):
    def __init__(self):
        super().__init__()
        self.title("Book Renewal Form")
        self.canvas = Canvas(width=500, height=417)
        self.canvas.pack()
        self.maxsize(450,300)
        m = StringVar()
        n = StringVar()
        self.cal = 0

        def days_Gap(dateA, dateB):
            dateA = datetime.strptime(dateA, "%Y-%m-%d")
            dateB = datetime.strptime(dateB, "%Y-%m-%d")
            return abs((dateB - dateA).days)

        def qui():
            if len(m.get()) == 0 or len(n.get()) == 0:
                messagebox.showerror("Error","Please Enter both BookId/StudentId's")
            else:
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.conn.cursor()
                    self.pointTo.execute("Select BID from issue where BID = %s",(m.get()))
                    temp = self.pointTo.fetchone()
                    self.pointTo.execute("Select Fine from students where Student_Id = %s", (n.get()))
                    fine = self.pointTo.fetchone()
                    self.pointTo.execute("Select Return_date from issue where BID = %s and SID = %s", (m.get(), n.get()))
                    tValue = self.pointTo.fetchone()
                    if tValue:
                        currentDay = str(date.today())
                        newDay = str(tValue[0])
                        if currentDay < newDay:
                            messagebox.showinfo("Oops", "Your Return Date Has not yet come")
                        else:
                            self.cal = days_Gap(newDay, currentDay)
                            self.cal += int(fine[0])
                        if int(self.cal) >= 100:
                            messagebox.showinfo("Fine", "Your Id is banned.Please pay the fine")
                        elif int(self.cal) > 0:
                            messagebox.showinfo('Warning','Please Return/Renew book Timely to avoid termination of id')
                            self.pointTo.execute("Update students set Fine = %s where Student_Id = %s",(int(self.cal), n.get()))
                            self.pointTo.execute("UPDATE issue set Issue_date = date('now') where BID =%s ", (m.get()))
                            self.pointTo.execute("update issue set Return_date = date('now','+15 days') where BID = %s",(m.get()))
                            self.conn.commit()
                            self.conn.close()
                            messagebox.showinfo('Info', 'Successfully Renewed')
                            c = messagebox.askyesno("Confirm", "Do you want to renew another book%s")
                            if c:
                                self.destroy()
                                os.system('%s %s' % (py, 'BookRenewal.py'))
                            else:
                                self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "The Book is not yet issued")
                except TypeError:
                  messagebox.showerror("Error", "Check The Texts")
                except Exception as ex:
                    print(ex)

        Label(self, text='Book Renewal Page',  fg='red',font=('arial', 29, 'bold')).place(x=55, y=50)
        Label(self, text='Book ID',font=('Comic Scan Ms', 11, 'bold')).place(x=30, y=150)
        Entry(self, textvariable=m, width=40).place(x=170, y=155)
        Label(self, text="Student Id",font=('Comic Scan Ms', 11, 'bold')).place(x=30, y=200)
        Entry(self, textvariable=n, width=40).place(x=170, y=205)
        Button(self, text="Renew", width=25, command=qui).place(x=180, y=240)

renew().mainloop()

