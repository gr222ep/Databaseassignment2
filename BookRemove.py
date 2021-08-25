from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import Error
import os
import sys

py = sys.executable

class rb(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(380,260)
        self.title("Remove Book Details")
        self.canvas = Canvas(width=500, height=500)
        self.canvas.pack()
        m= StringVar()

        def aaa():
            if len(m.get()) == 0:
                messagebox.showerror("Error","Please Enter The Book Id")
            else:
                cnfrmMsg= messagebox.askyesno('Remove Book', 'Are You Sure You Want To Delete The Book')
                if cnfrmMsg:
                    try:
                        self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                        self.pointTo = self.conn.cursor()
                        self.pointTo.execute("DELETE FROM books WHERE Book_Id = %s",(m.get()))
                        messagebox.showinfo('Remove', 'Successfully Removed')
                        self.conn.commit()
                        self.conn.close()
                        dialogMsg = messagebox.askyesno("Confirm","Do you want to remove another book")
                        if dialogMsg:
                            self.destroy()
                            os.system('%s %s' % (py, 'BookRemove.py'))
                        else:
                            self.destroy()
                    except Exception as ex:
                        print(ex)

        lb = Label(self, text="-:Book Id:-",fg='red', font=('Comic Scan Ms', 22, 'bold'))
        lb.place(x=90, y=70)
        e = Entry(self, textvariable=m, width=30).place(x=85, y=135)
        bt = Button(self, text="Delete", width=20, command=aaa).place(x=100, y=170)

rb().mainloop()
