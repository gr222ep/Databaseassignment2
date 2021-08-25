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
    pointTo.execute("SELECT b.book_id,b.book_name,b.author,(SELECT COUNT(*) FROM issue WHERE issue.bid = b.book_id) AS issue_count,(SELECT COUNT(*) FROM breturns WHERE breturns.bid IN (  SELECT bid FROM breturns WHERE breturns.bid = b.book_id ) ) AS breturns_count FROM books AS b ORDER BY breturns_count DESC, issue_count DESC, author DESC")
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
formatTable.heading("#3", text="Author Name")
formatTable.column("#4", anchor=tk.CENTER)
formatTable.heading("#4", text="No.of Book Issues")
formatTable.column("#5", anchor=tk.CENTER)
formatTable.heading("#5", text="No.of Book Returns")
formatTable.pack()
button1 = tk.Button(text="View", command=ViewContent)
button1.pack(pady=10)
root.mainloop()