from tkinter import ttk
import tkinter as tk
import pymysql
from pymysql import Error
def dbCconnection():
    connection = pymysql.connect(host="localhost", user="root", password="root", database="library")
    pointTo = connection.cursor()
    connection.close()
def ViewContent():
    connection =pymysql.connect(host="localhost", user="root", password="root", database="library")
    pointTo = connection.cursor()
    pointTo.execute("select sid,count(bid) from issue group by sid")
    rowData = pointTo.fetchall()
    for rowData in rowData :
        formatTable.insert("","end",text = rowData [1], values = (rowData [0],rowData [1]))
    connection.close()
# connect to the database
dbCconnection()
root = tk.Tk()
formatTable = ttk.Treeview(root, column=("c1", "c2"), show='headings')
formatTable.column("#1", anchor=tk.CENTER)
formatTable.heading("#1", text="Student ID")
formatTable.column("#2", anchor=tk.CENTER)
formatTable.heading("#2", text="No.of Book Issues")
formatTable.pack()
button1 = tk.Button(text="View", command=ViewContent)
button1.pack(pady=10)
root.mainloop()