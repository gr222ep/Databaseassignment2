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
    pointTo.execute("SELECT issue.BID, books.book_name,books.Author,issue.Issue_date,issue.Return_date FROM issue INNER JOIN books ON issue.BID=books.book_id")
    rowData = pointTo.fetchall()
    for rowData in rowData :
        formatTable.insert("","end",text = rowData [4], values = (rowData [0],rowData [1],rowData [2],rowData [3],rowData [4]))
    connection.close()
# connect to the database
dbCconnection()
root = tk.Tk()
formatTable = ttk.Treeview(root, column=("c1","c2","c3","c4","c5"), show='headings')
formatTable.column("#1", anchor=tk.CENTER)
formatTable.heading("#1", text="Book ID")
formatTable.column("#2", anchor=tk.CENTER)
formatTable.heading("#2", text="Book Name")
formatTable.column("#3", anchor=tk.CENTER)
formatTable.heading("#3", text="Author")
formatTable.column("#4", anchor=tk.CENTER)
formatTable.heading("#4", text="Issue Date")
formatTable.column("#5", anchor=tk.CENTER)
formatTable.heading("#5", text="Return Date")
formatTable.pack()
button1 = tk.Button(text="View", command=ViewContent)
button1.pack(pady=10)
root.mainloop()