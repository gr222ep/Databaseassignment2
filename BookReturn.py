from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import Error
import os,sys
from datetime import datetime,date
pythonFile = sys.executable
class ret(Tk):
    def __init__(self):
        super().__init__()
        self.title("Book Return Form")
        self.maxsize(420,260)
        self.canvas = Canvas(width=500, height=417)
        self.canvas.pack()
        self.cal = 0
        m = StringVar()

        def days_Gap(dateA, dateB):
            if dateB <= dateA:
                return 0
            else:
                dateA = datetime.strptime(dateA, "%Y-%m-%d")
                dateB = datetime.strptime(dateB, "%Y-%m-%d")
                return abs((dateB - dateA).days)

        def qui():
            if len(m.get()) == '0':
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.conn.cursor()
                    self.pointTo.execute("Select SID from issue where BID = %s", (m.get()))
                    studentID = list(self.pointTo.fetchone())
                    self.pointTo.execute("Select Books_Issued from students where Student_Id = %s", (studentID[0]))
                    gstudentID = list(self.pointTo.fetchone())
                    gstudentID[0] = gstudentID[0] - 1
                    self.pointTo.execute("Select BID from issue where BID = %s",(m.get()))
                    tValue = self.pointTo.fetchone()
                    self.pointTo.execute("Select Fine from students where Student_Id = %s", (studentID[0]))
                    fineCalculation = self.pointTo.fetchone()
                    self.pointTo.execute("Select Return_date from issue where BID = %s and SID = %s", (m.get(), [0]))
                    tValue1 = self.pointTo.fetchone()
                    dayarea = str(date.today())
                    earlyarea = str(tValue[0])
                    self.cal = days_Gap(earlyarea, dayarea)
                    self.cal += int(fineCalculation[0])
                    if dayarea <= earlyarea and int(self.cal) == 0:
                        #self.pointTo.execute("DELETE FROM issue WHERE BID = %s", (m.get()))
                        self.pointTo.execute("update books set Availiability = 1 where Book_Id = %s", (m.get()))
                        self.pointTo.execute("update students set Books_Issued = %s where Student_Id = %s", (gstudentID[0],studentID[0]))
                        self.pointTo.execute("insert into breturns values(%s,%s,%s)", (m.get(),studentID[0],dayarea))
                        self.conn.commit()
                        self.conn.close()
                        messagebox.showinfo('Info', 'Successfully Returned')
                        d = messagebox.askyesno("Confirm", "Return more books%s")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (pythonFile, 'BookReturn.py'))
                        else:
                            self.destroy()
                    elif len(tValue) > 0:
                        if int(self.cal) > 0:
                            messagebox.showinfo('Warning','Please Return/Renew book Timely to avoid termination of id')
                            self.pointTo.execute("Update students set Fine = %s where Student_Id = %s",(int(self.cal), studentID[0]))
                            self.pointTo.execute("DELETE FROM issue WHERE BID = %s", (m.get()))
                            self.pointTo.execute("update books set Availiability = 1 where Book_Id = %s", (m.get()))
                            self.pointTo.execute("update students set Books_Issued = %s where Student_Id = %s", (gstudentID[0],studentID[0]))
                            self.conn.commit()
                            self.conn.close()
                            messagebox.showinfo('Info', 'Succesfully Returned')
                            d = messagebox.askyesno("Confirm", "Return more books%s")
                            if d:
                                self.destroy()
                                os.system('%s %s' % (pythonFile, 'BookReturn.py'))
                            else:
                                self.destroy()
                        else:
                            self.pointTo.execute("DELETE FROM issue WHERE BID = %s", (m.get()))
                            self.pointTo.execute("update books set Availiability = 1 where Book_Id = %s", (m.get()))
                            self.pointTo.execute("update students set Books_Issued = %s where Student_Id = %s", (gstudentID[0],studentID[0]))
                            self.conn.commit()
                            self.conn.close()
                            messagebox.showinfo('Info', 'Successfully Returned')
                            d = messagebox.askyesno("Confirm", "Return more books%s")
                            if d:
                                self.destroy()
                                os.system('%s %s' % (pythonFile, 'BookReturn.py'))
                            else:
                                self.destroy()
                    else:
                        messagebox.showinfo("Oop's", "Book not yet issued till Now.")
                except Exception as ex:
                    print(ex)
        Label(self, text='Book Return Page', fg='red',font=('arial', 28, 'bold')).place(x=40, y=50)
        Label(self, text='Enter Book ID', font=('Comic Scan Ms', 14, 'bold')).place(x=20, y=120)
        Entry(self, textvariable=m, width=40).place(x=165, y=124)
        Button(self, text="Return", width=25, command=qui).place(x=180, y=180)
ret().mainloop()
