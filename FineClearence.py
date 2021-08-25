from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from pymysql import Error
import re
import sys,os
pytnCmd = sys.executable
class Fine(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(440,250)
        self.minsize(440, 250)
        self.title("Fine Clearence Form")
        self.canvas = Canvas(width=450, height=254)
        self.canvas.pack()
        #creating variables
        m = StringVar()
        def clear():
            if len(m.get()) == 0:
                messagebox.showerror("Error","Please Enter The Student Id")
            elif m.get().isdigit():
                try:
                    self.connection =pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.connection.cursor()
                    self.pointTo.execute("Select Student_Id from students")
                    stdntData = self.pointTo.fetchall()
                    liststdntData = list(stdntData)
                    if liststdntData:
                        for sid in liststdntData:

                            if m.get() in sid:
                                print("yes")
                                confirmMsg = messagebox.askyesno("Confirm","Are You Sure you want to clear the fine?")
                                if confirmMsg:

                                    self.pointTo.execute("Update students set Fine=0 where Student_Id= %s",(m.get()))
                                    self.connection.commit()
                                    self.connection.close()
                                    messagebox.showinfo("Successful","All Fine Cleared")
                                    d = messagebox.askyesno("Confirm","Do you want to clear another fine?")
                                    if d:
                                        self.destroy()
                                        os.system('%s %s'% (pytnCmd,'FineClearence.py'))
                                    else:
                                        self.destroy()
                            else:
                                messagebox.showinfo("Oops","The Given Student ID not found")
                    else:
                        messagebox.showerror("Error","Please Check The Student Id")
                except Exception as ex:
                    print(ex)
            else:
                messagebox.showerror("Error","Please Check The Student Id")
        Label(self,text="Enter Student Id", font = ('arial',15,'bold')).place(x=150,y=50)
        Entry(self,textvariable=m,width=40).place(x=105,y=100)
        Button(self, text='Pay Fine', width=20,command = clear).place(x=150, y=130)
Fine().mainloop()
