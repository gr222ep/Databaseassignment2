from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from pymysql import Error
class Sea(Tk):
    def __init__(self):
        super().__init__()
        mValue = StringVar()
        nValue = StringVar()
        self.title("Search Book")
        self.maxsize(800,500)
        self.minsize(800,500)
        self.canvas = Canvas(width=800, height=500)
        self.canvas.pack()

        l1=Label(self,text="Book Search Page",font=("Arial",20,'bold')).place(x=290,y=20)
        l = Label(self, text="Search Type", font=("Arial", 14, 'bold')).place(x=60, y=96)
        def insert(data):
            self.listForm.delete(*self.listForm.get_children())
            for row in data:
                self.listForm.insert("", 'end', text=row[0], values=(row[1], row[2],row[4], 'Available' if row[3] == 1 else 'Unavailable'))
        def ge():
            if (len(nValue.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(mValue.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+nValue.get())
            elif nValue.get() == 'Book Id':
                try:
                    self.conn = pymysql.connect(host="localhost", user="root", password="root", database="library")
                    self.pointTo = self.conn.cursor()
                    self.pointTo.execute("DROP VIEW booksavialability")
                    self.pointTo.execute("CREATE VIEW booksavialability AS SELECT book_name,Availiability FROM books")

                    self.studentlist = self.pointTo.fetchall()
                    self.pointTo.execute("Select b.Book_Id,b.Book_name,b.Author,b.Availiability,count(iu.sid) from books b,issue iu where iu.BID=%s and  b.Book_Id LIKE %s ", (mValue.get(),'%'+mValue.get()+'%'))
                    self.pc = self.pointTo.fetchall()
                    if self.pc:
                        insert(self.pc)
                    else:
                        messagebox.showinfo("Oop's","Either Book Id is incorrect or it is not available")
                except Exception as ex:
                        print(ex)
        b=Button(self,text="Search",width=15,font=("Arial",10,'bold'),command=ge).place(x=460,y=148)
        c=ttk.Combobox(self,textvariable=nValue,values=["Book Id"],width=40,state="readonly").place(x = 180, y = 100)
        en = Entry(self,textvariable=mValue,width=43).place(x=180,y=155)
        la = Label(self, text="Enter Value", font=("Arial", 14, 'bold')).place(x=60, y=150)

        def handle(event):
            if self.listForm.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listForm = ttk.Treeview(self, height=13,columns=('Book Name', 'Book Author', 'Issued Students','Availability'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listForm.yview)
        self.listForm.configure(yscrollcommand=self.vsb.set)
        self.listForm.heading("#0", text='Book ID', anchor='center')
        self.listForm.column("#0", width=80, anchor='center')
        self.listForm.heading("Book Name", text='Book Name')
        self.listForm.column("Book Name", width=150, anchor='center')
        self.listForm.heading("Book Author", text='Book Author')
        self.listForm.column("Book Author", width=150, anchor='center')

        self.listForm.heading("Issued Students", text='Issued Students')
        self.listForm.column("Issued Students", width=150, anchor='center')


        self.listForm.heading("Availability", text='Availability')
        self.listForm.column("Availability", width=150, anchor='center')
        self.listForm.bind('<Button-1>', handle)
        self.listForm.place(x=40, y=200)
        self.vsb.place(x=763,y=200,height=287)
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

Sea().mainloop()
