from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import Error
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Remove User Details")
        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        a = StringVar()
        def ent():
            dConfirmMessage = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
            if dConfirmMessage:
                try:
                    self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.connection.cursor()
                    print(a.get())
                    self.pointTo.execute("Delete from admin where id = %s",(a.get()))
                    temp = self.pointTo.fetchone()
                    if temp:
                        messagebox.showinfo("Oop's","User Not Found")
                        a.set("")
                    else:
                        self.connection.commit()
                        self.pointTo.close()
                        self.connection.close()
                        messagebox.showinfo("Confirm","User Removed Successfully")
                        a.set("")
                except Exception as ex:
                    print(ex)
        Label(self, text = "Username: ",fg='brown',font=('Arial', 15, 'bold')).place(x = 20,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 160,y = 44)
        Button(self, text='Remove', width=15, font=('arial', 10),command = ent).place(x=200, y = 90)



Rem().mainloop()
