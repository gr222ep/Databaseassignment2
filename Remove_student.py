from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import Error
import os
import sys

py = sys.executable

class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(450,250)
        self.minsize(450,250)
        self.title("Remove Student Details")
        self.canvas = Canvas(width=500, height=417)
        self.canvas.pack()
        a = StringVar()

        def iii():
            if len(a.get()) == 0:
                messagebox.showerror("Error", "Please Enter The Student Id")
            else:
                c = messagebox.askyesno('Remove Book', 'Are You Sure You Want To Remove The Student')
                if c:
                    try:
                        self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                        self.pointTo = self.connection.cursor()
                        self.pointTo.execute("DELETE FROM students WHERE Student_Id = %s", (a.get()))
                        messagebox.showinfo('Remove', 'Successfully Removed')
                        self.connection.commit()
                        self.connection.close()
                        d = messagebox.askyesno("Confirm", "Do you want to remove another student")
                        if d:
                            self.destroy()
                            os.system('%s %s' % (py, 'Remove_student.py'))
                        else:
                            self.destroy()
                    except Error:
                        messagebox.showerror("Error", "Something Goes Wrong")

        self.lb = Label(self, text="Enter Student Id", font=('Arial', 15, 'bold'))
        self.lb.place(x=30, y=70)
        self.e1 = Entry(self, textvariable=a, width=30).place(x=230, y=77)
        self.butt1234 = Button(self, text="Remove", width=20, command=iii).place(x=230, y=120)
Rem().mainloop()
