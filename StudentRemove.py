from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import Error
import os
import sys
pyCmd = sys.executable
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
                confirmMessag = messagebox.askyesno('Remove Book', 'Are You Sure You Want To Remove The Student')
                if confirmMessag:
                    try:
                        self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                        self.pointTo = self.connection.cursor()
                        self.pointTo.execute("DELETE FROM students WHERE Student_Id = %s", (a.get()))
                        messagebox.showinfo('Remove', 'Successfully Removed')
                        self.connection.commit()
                        self.connection.close()
                        dconfirmMsg = messagebox.askyesno("Confirm", "Do you want to remove another student")
                        if dconfirmMsg:
                            self.destroy()
                            os.system('%s %s' % (pyCmd , 'StudentRemove.py'))
                        else:
                            self.destroy()
                    except Exception as ex:
                        print(ex)

        self.label = Label(self, text="Enter Student Id", font=('Arial', 15, 'bold'))
        self.label.place(x=30, y=70)
        self.label = Entry(self, textvariable=a, width=30).place(x=230, y=77)
        self.labelButton = Button(self, text="Delete", width=20, command=iii).place(x=230, y=120)
Rem().mainloop()
