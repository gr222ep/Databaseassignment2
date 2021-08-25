from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from pymysql import Error
from PIL import ImageTk,Image
import os,glob


class Sst(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("Search Student Details")
        self.maxsize(770,320)
        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        l1=Label(self,text="Search Student",font=("Arial",19,'bold')).place(x=290,y=40)
        l = Label(self, text="Search Type", font=("Arial", 14, 'bold')).place(x=180, y=100)
        def writeTofile(data,filename):
            with open(filename,'wb') as file:
                file.write(data)

        def insert(data):
            self.listForm.delete(*self.listForm.get_children())
            for row in data:
                self.listForm.insert("","end",text = row[2], values = (row[1],row[4],row[6]))

        def photo(pic):
            try:
                self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                self.pointTo = self.connection.cursor()
                self.pointTo.execute("Select * from students where Student_Id = %s", (pic))
                pcuteStudents = self.pointTo.fetchone()
                if pcuteStudents[5] != '':
                    photoPath = "TempImages\\" + pcuteStudents[1] + ".jpeg"
                    writeTofile(pcuteStudents[5], photoPath)
                    self.photo = ImageTk.PhotoImage(Image.open("TempImages\\" + pcuteStudents[1] + ".jpeg"))
                    Label(image=self.photo, width=150, height=150).place(x=625, y=20)
                    flist = glob.glob("TempImages\*.jpeg")
                    for file in flist:
                        os.remove(file)
                else:
                    self.photo = ImageTk.PhotoImage(Image.open("TempImages\\48-512.png"))
                    Label(image=self.photo, width=150, height=150).place(x=625, y=20)
            except Error:
                messagebox.showerror("Error", "Something goes wrong")

#clicking the record will open the picture
        def select(a):
            currentItem = self.listForm.focus()
            selectedItem = self.listForm.item(currentItem)
            pic = str(selectedItem['text'])
            photo(pic)


        def ge():
            if (len(g.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(f.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+g.get())
            elif g.get() == 'Name':
                try:
                    self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.connection.cursor()
                    self.pointTo.execute("Select * from students where name like %s",('%'+f.get()+'%'))
                    pcuteStudents = self.pointTo.fetchall()
                    if pcuteStudents:
                        insert(pcuteStudents)
                    else:
                        messagebox.showinfo("Oop's","Name not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")
            elif g.get() == 'ID':
                try:
                    self.connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.connection.cursor()
                    self.pointTo.execute("Select * from students where Student_Id like %s", ('%' + f.get() + '%'))
                    pc = self.pointTo.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's", "Id not found")
                except Exception as ex:
                    print(ex)


        b=Button(self,text="Search",width=8,font=("Arial",8,'bold'),command=ge).place(x=400,y=170)
        c=ttk.Combobox(self,textvariable=g,values=["Name","ID"],width=40,state="readonly").place(x = 310, y = 105)
        en = Entry(self,textvariable=f,width=43).place(x=310,y=145)
        la = Label(self, text="Enter", font=("Arial", 15, 'bold')).place(x=180, y=140)

        def handle(event):
            if self.listForm.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listForm = ttk.Treeview(self, height=3,columns=('Student Name', 'Phone Number', 'No. Of Books Issued'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listForm.yview)
        self.listForm.configure(yscrollcommand=self.vsb.set)
        self.listForm.heading("#0", text='Student ID', anchor='w')
        self.listForm.column("#0", width=100, anchor='w')
        self.listForm.heading("Student Name", text='Student Name')
        self.listForm.column("Student Name", width=200, anchor='center')
        self.listForm.heading("Phone Number", text='Phone Number')
        self.listForm.column("Phone Number", width=200, anchor='center')
        self.listForm.heading("No. Of Books Issued", text='No. Of Books Issued')
        self.listForm.column("No. Of Books Issued", width=200, anchor='center')
        self.listForm.bind("<Button-1>", handle)
        self.listForm.bind("<ButtonRelease-1>",select)
        self.listForm.place(x=40, y=200)
        self.vsb.place(x=743,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))









Sst().mainloop()
