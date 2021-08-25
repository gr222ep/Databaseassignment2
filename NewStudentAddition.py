from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pymysql
from pymysql import Error
import os
import sys
pyCmd = sys.executable
class Add(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(500,417)
        self.minsize(500,417)
        self.title('Add New Student Details')
        self.canvas = Canvas(width=500, height=417)
        self.canvas.pack()

        r = StringVar()
        m = StringVar()
        n = StringVar()
        o = StringVar()
        p = StringVar()
        q = StringVar()
#uploading image
        def convertToBinaryData(filename):
            with open(filename, 'rb') as file:
                blobData = file.read()
            return blobData
#verifying input
        def asi():
            if len(r.get()) < 1:
                messagebox.showinfo("Oop's", "Enter Your library ID")
            elif len(m.get()) < 1:
                messagebox.showinfo("Oop's","Enter Your Student Name")
            elif len(n.get()) < 1:
                messagebox.showinfo("Oop's", "Enter Your Student PId")
            elif len(o.get()) < 1:
                messagebox.showinfo("Oop's", "Enter Your Student year")
            elif len(p.get()) < 10 or len(p.get()) > 10:
                messagebox.showinfo("Oop's", "Enter Your Student Contact Number")
            elif len(q.get()) < 1:
                messagebox.showinfo("Oop's", "Select an Image of id")
            else:
                try:
                    self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.connection.cursor()
                    edit_insert_statement ="Insert into students(Roll_no,name,Student_Id,class,Phone_number,Image) values (%s,%s,%s,%s,%s,%s)"
                    record_statement2 = (r.get(),m.get(),n.get(),o.get(),p.get(),convertToBinaryData(q.get()))
                    pc = self.pointTo.execute(edit_insert_statement,record_statement2)
                    self.connection.commit()
                    if pc:
                        messagebox.showinfo("Done","Student Inserted Successfully")
                        asConfrmMsg = messagebox.askyesno("Confirm","Do you want to add another student?")
                        if asConfrmMsg:
                            self.destroy()
                            os.system('%s %s' % (pyCmd, 'NewStudentAddition.py'))
                        else:
                            self.destroy()
                    else:
                        messagebox.showerror("Error", 'Something goes wrong')
                    self.pointTo.close()
                    self.connection.close()
                except Exception as ex:
                    print(ex)

        # label and input box
        label4 = Label(self, text='Add Student Details', fg='red', font=('Arial bold', 25, 'bold')).place(x=100, y=32)
        lbl = Label(self, text='Library ID:', font=('Arial', 11, 'bold')).place(x=70, y=82)
        S_name = Entry(self, textvariable=r, width=30).place(x=200, y=84)
        label = Label(self, text='Student Name:', font=('', 11, 'bold')).place(x=70, y=130)
        S_name = Entry(self, textvariable=m, width=30).place(x=200, y=132)
        label5 = Label(self, text='Student ID:', font=('Arial', 11, 'bold')).place(x=70, y=180)
        S_ID = Entry(self, textvariable=n, width=30).place(x=200, y=182)
        label6 = Label(self, text='Course/Section:', font=('Arial', 11, 'bold')).place(x=70, y=230)
        S_Class = Entry(self, textvariable=o, width=30).place(x=200, y=232)
        label7 = Label(self, text='Contact Number:', font=('Arial', 11, 'bold')).place(x=70, y=280)
        def fileDialog():
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select A File",filetype = (("jpeg","*.jpg"),("png","*.png"),("All Files","*.*")))
            q.set(filename)
        label8 = Label(self, text="Upload image", font=('Arial', 11, 'bold')).place(x=70, y=330)
        upload_image = Entry(self, textvariable=q, width=30).place(x=200, y=330)
        ZS_phone_number = Entry(self, textvariable=p, width=30).place(x=200, y=282)
        butt = Button(self, text="Browse", width=7, command=fileDialog).place(x=400, y=328)
        S_butt = Button(self, text="Submit",width = 15,command=asi).place(x=230, y=370)

Add().mainloop()
