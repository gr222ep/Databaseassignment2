from tkinter import *
from tkinter import messagebox
import pymysql
import os
import sys
from pymysql import Error

pyCmd = sys.executable

#creating window
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(480,360 )
        self.minsize(480,360)
        self.title('Add Book Information')
        self.canvas = Canvas(width=500, height=500)
        self.canvas.pack()
        m = StringVar()
        n = StringVar()
        p = StringVar()
        #verifying Input
        def b_q():
            if len(m.get()) == 0 or len(n.get()) == 0:
                messagebox.showerror("Error","Please Enter The Details")
            else:
                g = 1
                try:
                    self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.connection.cursor()
                    edit_insert_statement = " INSERT INTO books VALUES (%s,%s,%s,%s)"
                    record_statement2 = (m.get(), n.get(), p.get(), g)
                    self.pointTo.execute(edit_insert_statement,record_statement2)
                    self.connection.commit()
                    messagebox.showinfo('Info', 'Successfully Added')
                    askMessage = messagebox.askyesno("Confirm", "Do you want to add another book?")
                    if askMessage:
                        self.destroy()
                        os.system('%s %s' % (pyCmd , 'NewBookAddition.py'))
                    else:
                        self.destroy()
                except Exception as ex:
                    print(ex)
        Label(self, text='').pack()
        Label(self, text= 'Book Details',fg= 'red',font=('Times New Roman', 20, 'bold')).place(x=140, y=80)
        Label(self, text='').pack()
        Label(self, text='Book Id:',fg='brown', font=('Comic Scan Ms', 10, 'bold')).place(x=60, y=130)
        Entry(self, textvariable=m, width=30).place(x=170, y=132)
        Label(self, text='Book Name:',fg='brown', font=('Comic Scan Ms', 10, 'bold')).place(x=60, y=180)
        Entry(self, textvariable=n, width=30).place(x=170, y=182)
        Label(self, text='Book Author:',fg='brown', font=('Comic Scan Ms', 10, 'bold')).place(x=60, y=230)
        Entry(self, textvariable=p, width=30).place(x=170, y=232)
        Button(self, text="Submit", command=b_q).place(x=245, y=300)
Add().mainloop()
